from .admin import Admin
from .core import Core
from .node import NodeMethods
from .subscription import Subscription
from .system import System
from .template import TemplateMethods
from .user import UserMethods


class Methods(
    Admin, NodeMethods, Subscription, Core, UserMethods, TemplateMethods, System
):
    def __init__(self, username: str, password: str, panel_address: str, proxy: dict | None = None):
        super().__init__(username, password, panel_address, proxy)
