"""
微服务服务模块
处理微服务相关的业务逻辑
"""

from typing import Dict, List, Optional, Tuple

from sqlalchemy.exc import SQLAlchemyError

from app.repositories.service_repository import ServiceRepository
from app.extensions import db


class ServiceServiceError(Exception):
    """微服务服务错误"""


class ServiceService:
    """微服务服务类"""

    def __init__(self):
        """初始化微服务服务"""
        self.service_repository = ServiceRepository()

    def get_all_services(self) -> List[Dict]:
        """
        获取所有微服务

        Returns:
            List[Dict]: 微服务列表，每个微服务以字典形式表示
        """
        try:
            return self.service_repository.get_all_services_with_dict()
        except Exception as e:
            raise ServiceServiceError(f"获取微服务列表失败: {str(e)}")

    def get_service_by_id(self, service_id: str) -> Dict:
        """
        根据ID获取微服务

        Args:
            service_id: 微服务ID

        Returns:
            Dict: 微服务信息字典

        Raises:
            ServiceServiceError: 微服务不存在时抛出
        """
        try:
            service_dict = self.service_repository.get_service_dict_by_id(service_id)
            if not service_dict:
                raise ServiceServiceError(f"微服务ID {service_id} 不存在")
            return service_dict
        except Exception as e:
            if isinstance(e, ServiceServiceError):
                raise
            raise ServiceServiceError(f"获取微服务失败: {str(e)}")

    def get_services_by_attribute(self, attribute: str) -> List[Dict]:
        """
        根据属性获取微服务列表

        Args:
            attribute: 微服务属性

        Returns:
            List[Dict]: 符合条件的微服务列表
        """
        try:
            services = self.service_repository.find_by_attribute(attribute)
            return [service.to_dict() for service in services]
        except Exception as e:
            raise ServiceServiceError(f"查询微服务失败: {str(e)}")

    def create_service(self, service_data: Dict) -> Dict:
        """
        创建新微服务

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
            Dict: 创建的微服务信息

        Raises:
            ServiceServiceError: 创建过程中出错
        """
        if not service_data.get("name"):
            raise ServiceServiceError("服务名称不能为空")

        try:
            # 使用仓库层创建服务及其关联数据
            service = self.service_repository.create_service_with_relations(service_data)
            return service.to_dict()
        except SQLAlchemyError as e:
            raise ServiceServiceError(f"创建微服务失败: {str(e)}")
        except Exception as e:
            raise ServiceServiceError(f"创建微服务过程中出错: {str(e)}")

    def update_service(self, service_id: str, service_data: Dict) -> Dict:
        """
        更新微服务信息

        Args:
            service_id: 微服务ID
            service_data: 更新的微服务数据

        Returns:
            Dict: 更新后的微服务信息

        Raises:
            ServiceServiceError: 更新过程中出错
        """
        try:
            # 检查服务是否存在
            service = self.service_repository.get_service_by_id(service_id)
            if not service:
                raise ServiceServiceError(f"微服务ID {service_id} 不存在")
            
            # 使用仓库层更新服务及其关联数据
            updated_service = self.service_repository.update_service_with_relations(service_id, service_data)
            return updated_service.to_dict()
        except SQLAlchemyError as e:
            raise ServiceServiceError(f"更新微服务失败: {str(e)}")
        except Exception as e:
            if isinstance(e, ServiceServiceError):
                raise
            raise ServiceServiceError(f"更新微服务过程中出错: {str(e)}")

    def delete_service(self, service_id: str) -> bool:
        """
        删除微服务（软删除）

        Args:
            service_id: 微服务ID

        Returns:
            bool: 是否删除成功

        Raises:
            ServiceServiceError: 删除过程中出错
        """
        try:
            # 检查服务是否存在
            service = self.service_repository.get_service_by_id(service_id)
            if not service:
                raise ServiceServiceError(f"微服务ID {service_id} 不存在")
            
            # 使用仓库层删除服务
            success = self.service_repository.delete_service(service_id)
            if not success:
                raise ServiceServiceError(f"删除微服务失败")
            return True
        except Exception as e:
            if isinstance(e, ServiceServiceError):
                raise
            raise ServiceServiceError(f"删除微服务失败: {str(e)}")

    def search_services(self, keyword: str) -> List[Dict]:
        """
        搜索微服务

        Args:
            keyword: 搜索关键词，匹配服务名称

        Returns:
            List[Dict]: 符合条件的微服务列表
        """
        try:
            services = self.service_repository.search_by_keyword(keyword)
            return [service.to_dict() for service in services]
        except Exception as e:
            raise ServiceServiceError(f"搜索微服务失败: {str(e)}")

    def filter_services(self, **filters) -> List[Dict]:
        """
        根据条件筛选微服务

        Args:
            **filters: 筛选条件，可包括:
                - attribute: 服务属性
                - type: 服务类型
                - domain: 领域
                - industry: 行业
                - scenario: 场景
                - technology: 技术
                - status: 服务状态

        Returns:
            List[Dict]: 符合条件的微服务列表
        """
        try:
            services = self.service_repository.filter_services(**filters)
            return [service.to_dict() for service in services]
        except Exception as e:
            raise ServiceServiceError(f"筛选微服务失败: {str(e)}")


# 创建单例实例，方便导入使用
service_service = ServiceService() 