from flask import Blueprint
from flask_restx import Api

from app.api.namespaces.algorithm_service_ns import api as algorithm_service_ns
from app.api.namespaces.auth_ns import api as auth_ns
from app.api.namespaces.health_ns import api as health_ns
from app.api.namespaces.user_ns import api as user_ns

# 创建蓝图
api_bp = Blueprint("api", __name__)

# 创建API
api = Api(
    api_bp,
    version="1.0",
    title="ioeb项目后端 API",
    description="ioeb项目后端 API接口",
    doc="/docs",  # 将Swagger文档设置在/api/docs路径下
    # 自定义Swagger UI样式
    specs_route="/docs/",
)

# 注册命名空间
api.add_namespace(health_ns)
api.add_namespace(user_ns)
api.add_namespace(algorithm_service_ns)
api.add_namespace(auth_ns, path="/auth")  # 添加认证命名空间
