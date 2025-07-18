"""
微服务数据仓库模块
提供对微服务数据模型的基础操作接口
"""

import json
import uuid
from datetime import datetime
from typing import Dict, List, Optional, Union

from sqlalchemy.exc import SQLAlchemyError

from app.extensions import db
from app.models import Service, ServiceNorm, ServiceSource, ServiceApi, ServiceApiParameter, ServiceApiTool


class ServiceRepository:
    """微服务数据仓库"""

    def _convert_services_list_to_string(self, services_list):
        """
        将服务ID列表转换为逗号分隔的字符串
        
        Args:
            services_list: 服务ID列表，可以是list或None
            
        Returns:
            str: 逗号分隔的服务ID字符串，如果输入为空返回None
        """
        try:
            if not services_list or not isinstance(services_list, list):
                return None
            
            # 过滤掉空值和非字符串值
            valid_ids = []
            for service_id in services_list:
                if isinstance(service_id, str) and service_id.strip():
                    valid_ids.append(service_id.strip())
            
            # 如果没有有效的ID，返回None
            if not valid_ids:
                return None
                
            return ','.join(valid_ids)
            
        except Exception:
            # 如果处理过程中出现任何异常，返回None
            return None

    def get_all_services(self) -> List[Service]:
        """
        获取所有微服务

        Returns:
            List[Service]: 微服务对象列表
        """
        return Service.query.filter_by(deleted=0).all()
    
    def get_all_services_with_dict(self) -> List[Dict]:
        """
        获取所有微服务的字典表示

        Returns:
            List[Dict]: 微服务字典列表
        """
        services = self.get_all_services()
        return [service.to_dict() for service in services]
    
    def get_service_by_id(self, service_id: str) -> Optional[Service]:
        """
        根据ID获取微服务

        Args:
            service_id: 微服务ID

        Returns:
            Optional[Service]: 微服务对象，如果不存在则返回None
        """
        return Service.query.filter_by(id=service_id, deleted=0).first()
    
    def get_service_dict_by_id(self, service_id: str) -> Optional[Dict]:
        """
        根据ID获取微服务的字典表示

        Args:
            service_id: 微服务ID

        Returns:
            Optional[Dict]: 微服务字典，如果不存在则返回None
        """
        service = self.get_service_by_id(service_id)
        return service.to_dict() if service else None
    
    def get_services_by_ids(self, service_ids: List[str]) -> List[Service]:
        """
        根据ID列表批量获取微服务

        Args:
            service_ids: 微服务ID列表

        Returns:
            List[Service]: 微服务对象列表，按输入ID顺序返回，不存在的ID会被跳过
        """
        if not service_ids:
            return []
        
        # 使用IN操作符一次性查询所有服务，性能优化
        services = Service.query.filter(
            Service.id.in_(service_ids),
            Service.deleted == 0
        ).all()
        
        # 创建ID到服务对象的映射以便按输入顺序返回
        services_map = {service.id: service for service in services}
        
        # 按输入ID的顺序返回结果，跳过不存在的ID
        result = []
        for service_id in service_ids:
            if service_id in services_map:
                result.append(services_map[service_id])
        
        return result
    
    def get_services_dict_by_ids(self, service_ids: List[str]) -> List[Dict]:
        """
        根据ID列表批量获取微服务的字典表示

        Args:
            service_ids: 微服务ID列表

        Returns:
            List[Dict]: 微服务字典列表，按输入ID顺序返回，不存在的ID会被跳过
        """
        services = self.get_services_by_ids(service_ids)
        return [service.to_dict() for service in services]
    
    def find_by_name(self, name: str) -> Optional[Service]:
        """
        根据名称查找微服务

        Args:
            name: 微服务名称

        Returns:
            Optional[Service]: 微服务对象，如果不存在则返回None
        """
        return Service.query.filter_by(name=name, deleted=0).first()
    
    def find_by_attribute(self, attribute: str) -> List[Service]:
        """
        根据属性查找微服务

        Args:
            attribute: 微服务属性

        Returns:
            List[Service]: 微服务对象列表
        """
        return Service.query.filter_by(attribute=attribute, deleted=0).all()
    
    def search_by_keyword(self, keyword: str) -> List[Service]:
        """
        根据关键词搜索微服务

        Args:
            keyword: 搜索关键词，匹配服务名称

        Returns:
            List[Service]: 符合条件的微服务对象列表
        """
        return Service.query.filter(
            Service.name.like(f"%{keyword}%"),
            Service.deleted == 0
        ).all()
    
    def create_service(self, service_data: Dict) -> Service:
        """
        创建新微服务

        Args:
            service_data: 包含微服务基本信息的字典

        Returns:
            Service: 创建的微服务对象
        """
        service = Service(**service_data)
        db.session.add(service)
        db.session.commit()
        return service
    
    def create_service_with_relations(self, service_data: Dict) -> Service:
        """
        创建微服务及其关联数据（规范评分、来源信息、API）

        Args:
            service_data: 包含微服务信息的字典，应包括:
                - name: 服务名称
                - attribute: 服务属性
                - type: 服务类型
                - domain: 领域
                - industry: 行业
                - scenario: 场景
                - technology: 技术
                - network: 网络类型
                - port: 端口映射
                - volume: 数据卷映射
                - status: 服务状态
                - number: 服务编号
                - norm: 规范评分列表 (可选)
                - source: 来源信息 (可选)
                - apiList: API列表 (可选)

        Returns:
            Service: 创建的微服务对象

        Raises:
            SQLAlchemyError: 数据库操作错误
        """
        try:
            # 开始数据库事务
            service_id = str(uuid.uuid4())
            current_time = int(datetime.now().timestamp() * 1000) # 毫秒时间戳

            # 创建服务基本信息
            service = Service(
                id=service_id,
                name=service_data.get("name"),
                attribute=service_data.get("attribute", "non_intelligent"),
                type=service_data.get("type", "atomic"),
                domain=service_data.get("domain", "aml"),
                industry=service_data.get("industry", ""),
                scenario=service_data.get("scenario", ""),
                technology=service_data.get("technology", ""),
                network=service_data.get("network", ""),
                port=service_data.get("port", ""),
                volume=service_data.get("volume", ""),
                status=service_data.get("status", "default"),
                number=service_data.get("number", 0),
                create_time=current_time,
                creator_id=service_data.get("creator_id", "")
            )
            db.session.add(service)
            
            # 添加规范评分
            if "norm" in service_data and isinstance(service_data["norm"], list):
                for norm_data in service_data["norm"]:
                    norm = ServiceNorm(
                        id=str(uuid.uuid4()),
                        service_id=service_id,
                        key=norm_data.get("key", ""),
                        score=norm_data.get("score", 0),
                        platform_checked=norm_data.get("platformChecked", 0)
                    )
                    db.session.add(norm)
            
            # 添加来源信息
            if "source" in service_data and isinstance(service_data["source"], dict):
                source_data = service_data["source"]
                source = ServiceSource(
                    id=str(uuid.uuid4()),
                    service_id=service_id,
                    popover_title=source_data.get("popoverTitle", ""),
                    company_name=source_data.get("companyName", ""),
                    company_address=source_data.get("companyAddress", ""),
                    company_contact=source_data.get("companyContact", ""),
                    company_introduce=source_data.get("companyIntroduce", ""),
                    ms_introduce=source_data.get("msIntroduce", ""),
                    company_score=source_data.get("companyScore", 0),
                    ms_score=source_data.get("msScore", 0)
                )
                db.session.add(source)
            
            # 添加API信息
            if "apiList" in service_data and isinstance(service_data["apiList"], list):
                for api_data in service_data["apiList"]:
                    api_id = str(uuid.uuid4())
                    
                    # 处理可能的JSON字符串响应
                    response = None
                    if api_data.get("response"):
                        if isinstance(api_data["response"], dict):
                            response = json.dumps(api_data["response"])
                        else:
                            response = api_data["response"]
                    
                    # 处理可能的JSON字符串示例消息
                    example_msg = None
                    if api_data.get("example_msg"):
                        if isinstance(api_data["example_msg"], (list, dict)):
                            example_msg = json.dumps(api_data["example_msg"])
                        else:
                            example_msg = api_data["example_msg"]
                    
                    api = ServiceApi(
                        id=api_id,
                        service_id=service_id,
                        name=api_data.get("name", ""),
                        url=api_data.get("url", ""),
                        method=api_data.get("method", "GET"),
                        des=api_data.get("des", ""),
                        parameter_type=api_data.get("parameterType", 0),
                        response_type=api_data.get("responseType", 0),
                        is_fake=api_data.get("isFake", False),
                        response=response,
                        response_file_name=api_data.get("responseFileName"),
                        example_msg=example_msg,
                        subtitle=api_data.get("subtitle"),
                        services=self._convert_services_list_to_string(api_data.get("services")),
                        input_name=api_data.get("inputName"),
                        output_name=api_data.get("outputName"),
                        output_visualization=api_data.get("outputVisualization", False),
                        submit_button_text=api_data.get("submitButtonText")
                    )
                    db.session.add(api)
                    
                    # 添加API参数
                    if "parameters" in api_data and isinstance(api_data["parameters"], list):
                        for param_data in api_data["parameters"]:
                            param = ServiceApiParameter(
                                id=str(uuid.uuid4()),
                                api_id=api_id,
                                name=param_data.get("name", ""),
                                type=param_data.get("type", ""),
                                des=param_data.get("des", "")
                            )
                            db.session.add(param)
                    
                    # 添加API工具
                    if "tools" in api_data and isinstance(api_data["tools"], list):
                        for tool_data in api_data["tools"]:
                            tool = ServiceApiTool(
                                id=str(uuid.uuid4()),
                                api_id=api_id,
                                name=tool_data.get("name", ""),
                                description=tool_data.get("description", tool_data.get("des", ""))
                            )
                            db.session.add(tool)
            
            # 提交事务
            db.session.commit()
            return service
        except Exception as e:
            db.session.rollback()
            raise e
    
    def update_service(self, service_id: str, service_data: Dict) -> Optional[Service]:
        """
        更新微服务信息

        Args:
            service_id: 微服务ID
            service_data: 更新的微服务数据

        Returns:
            Optional[Service]: 更新后的微服务对象，如果不存在则返回None
        """
        service = self.get_service_by_id(service_id)
        if not service:
            return None
        
        for key, value in service_data.items():
            if hasattr(service, key):
                setattr(service, key, value)
        
        db.session.commit()
        return service
    
    def update_service_with_relations(self, service_id: str, service_data: Dict) -> Optional[Service]:
        """
        更新微服务及其关联数据（规范评分、来源信息、API）

        Args:
            service_id: 微服务ID
            service_data: 更新的微服务数据

        Returns:
            Optional[Service]: 更新后的微服务对象，如果不存在则返回None

        Raises:
            SQLAlchemyError: 数据库操作错误
        """
        try:
            service = self.get_service_by_id(service_id)
            if not service:
                return None
            
            # 更新服务基本信息
            for key, value in service_data.items():
                if key in ["name", "attribute", "type", "domain", "industry", 
                         "scenario", "technology", "network", "port", 
                         "volume", "status", "number"]:
                    setattr(service, key, value)
            
            # 更新规范评分
            if "norm" in service_data and isinstance(service_data["norm"], list):
                # 删除现有的规范评分
                ServiceNorm.query.filter_by(service_id=service_id).delete()
                
                # 添加新的规范评分
                for norm_data in service_data["norm"]:
                    norm = ServiceNorm(
                        id=str(uuid.uuid4()),
                        service_id=service_id,
                        key=norm_data.get("key", ""),
                        score=norm_data.get("score", 0),
                        platform_checked=norm_data.get("platformChecked", 0)
                    )
                    db.session.add(norm)
            
            # 更新来源信息
            if "source" in service_data and isinstance(service_data["source"], dict):
                # 删除现有的来源信息
                ServiceSource.query.filter_by(service_id=service_id).delete()
                
                # 添加新的来源信息
                source_data = service_data["source"]
                source = ServiceSource(
                    id=str(uuid.uuid4()),
                    service_id=service_id,
                    popover_title=source_data.get("popoverTitle", ""),
                    company_name=source_data.get("companyName", ""),
                    company_address=source_data.get("companyAddress", ""),
                    company_contact=source_data.get("companyContact", ""),
                    company_introduce=source_data.get("companyIntroduce", ""),
                    ms_introduce=source_data.get("msIntroduce", ""),
                    company_score=source_data.get("companyScore", 0),
                    ms_score=source_data.get("msScore", 0)
                )
                db.session.add(source)
            
            # 更新API信息
            if "apiList" in service_data and isinstance(service_data["apiList"], list):
                # 获取现有API的ID
                existing_apis = ServiceApi.query.filter_by(service_id=service_id).all()
                existing_api_ids = [api.id for api in existing_apis]
                
                # 删除相关的参数和工具
                for api_id in existing_api_ids:
                    ServiceApiParameter.query.filter_by(api_id=api_id).delete()
                    ServiceApiTool.query.filter_by(api_id=api_id).delete()
                
                # 删除API
                ServiceApi.query.filter_by(service_id=service_id).delete()
                
                # 添加新的API
                for api_data in service_data["apiList"]:
                    api_id = str(uuid.uuid4())
                    
                    # 处理可能的JSON字符串响应
                    response = None
                    if api_data.get("response"):
                        if isinstance(api_data["response"], dict):
                            response = json.dumps(api_data["response"])
                        else:
                            response = api_data["response"]
                    
                    # 处理可能的JSON字符串示例消息
                    example_msg = None
                    if api_data.get("example_msg"):
                        if isinstance(api_data["example_msg"], (list, dict)):
                            example_msg = json.dumps(api_data["example_msg"])
                        else:
                            example_msg = api_data["example_msg"]
                    
                    api = ServiceApi(
                        id=api_id,
                        service_id=service_id,
                        name=api_data.get("name", ""),
                        url=api_data.get("url", ""),
                        method=api_data.get("method", "GET"),
                        des=api_data.get("des", ""),
                        parameter_type=api_data.get("parameterType", 0),
                        response_type=api_data.get("responseType", 0),
                        is_fake=api_data.get("isFake", False),
                        response=response,
                        response_file_name=api_data.get("responseFileName"),
                        example_msg=example_msg,
                        subtitle=api_data.get("subtitle"),
                        services=self._convert_services_list_to_string(api_data.get("services")),
                        input_name=api_data.get("inputName"),
                        output_name=api_data.get("outputName"),
                        output_visualization=api_data.get("outputVisualization", False),
                        submit_button_text=api_data.get("submitButtonText")
                    )
                    db.session.add(api)
                    
                    # 添加API参数
                    if "parameters" in api_data and isinstance(api_data["parameters"], list):
                        for param_data in api_data["parameters"]:
                            param = ServiceApiParameter(
                                id=str(uuid.uuid4()),
                                api_id=api_id,
                                name=param_data.get("name", ""),
                                type=param_data.get("type", ""),
                                des=param_data.get("des", "")
                            )
                            db.session.add(param)
                    
                    # 添加API工具
                    if "tools" in api_data and isinstance(api_data["tools"], list):
                        for tool_data in api_data["tools"]:
                            tool = ServiceApiTool(
                                id=str(uuid.uuid4()),
                                api_id=api_id,
                                name=tool_data.get("name", ""),
                                description=tool_data.get("description", tool_data.get("des", ""))
                            )
                            db.session.add(tool)
            
            # 提交事务
            db.session.commit()
            return service
        except Exception as e:
            db.session.rollback()
            raise e
    
    def delete_service(self, service_id: str) -> bool:
        """
        删除微服务（软删除）

        Args:
            service_id: 微服务ID

        Returns:
            bool: 是否删除成功
        """
        service = self.get_service_by_id(service_id)
        if not service:
            return False
        
        service.deleted = 1
        db.session.commit()
        return True
    
    def filter_services(self, **filters) -> List[Service]:
        """
        根据条件筛选微服务

        Args:
            **filters: 筛选条件，可包括:
                - attribute: 服务属性（支持多个值）
                - type: 服务类型（支持多个值）
                - domain: 领域（支持多个值）
                - industry: 行业（支持多个值）
                - scenario: 场景（支持多个值）
                - technology: 技术（支持多个值）
                - status: 服务状态（支持多个值）

        Returns:
            List[Service]: 符合条件的微服务对象列表
        """
        query = Service.query.filter_by(deleted=0)
        
        # 应用筛选条件
        valid_filters = ["attribute", "type", "domain", "industry", "scenario", "technology", "status"]
        for key, value in filters.items():
            if key in valid_filters and value is not None:
                # 支持所有条件都能使用多个值
                if isinstance(value, list) and len(value) > 0:
                    query = query.filter(getattr(Service, key).in_(value))
                elif not isinstance(value, list) and value:
                    query = query.filter(getattr(Service, key) == value)
        
        return query.all()
    
    def get_service_norms(self, service_id: str) -> List[ServiceNorm]:
        """
        获取微服务的规范评分列表

        Args:
            service_id: 微服务ID

        Returns:
            List[ServiceNorm]: 规范评分对象列表
        """
        return ServiceNorm.query.filter_by(service_id=service_id).all()
    
    def get_service_source(self, service_id: str) -> Optional[ServiceSource]:
        """
        获取微服务的来源信息

        Args:
            service_id: 微服务ID

        Returns:
            Optional[ServiceSource]: 来源信息对象，如果不存在则返回None
        """
        return ServiceSource.query.filter_by(service_id=service_id).first()
    
    def get_service_apis(self, service_id: str) -> List[ServiceApi]:
        """
        获取微服务的API列表

        Args:
            service_id: 微服务ID

        Returns:
            List[ServiceApi]: API对象列表
        """
        return ServiceApi.query.filter_by(service_id=service_id).all()
    
    def get_api_parameters(self, api_id: str) -> List[ServiceApiParameter]:
        """
        获取API的参数列表

        Args:
            api_id: API ID

        Returns:
            List[ServiceApiParameter]: 参数对象列表
        """
        return ServiceApiParameter.query.filter_by(api_id=api_id).all()

    def update_service_status(self, service_id: str, status: str) -> bool:
        """
        更新微服务状态

        Args:
            service_id: 微服务ID
            status: 新的状态值

        Returns:
            bool: 是否更新成功
        """
        try:
            service = self.get_service_by_id(service_id)
            if not service:
                return False
            
            service.status = status
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False


# 创建单例实例，方便导入使用
service_repository = ServiceRepository()