from .admin import Admin
from .node import NodeMethods
from .subscription import Subscription
from .core import Core
from .user import UserMethods
from .template import TemplateMethods
from .system import System


class Methods(
    Admin, NodeMethods, Subscription, Core, UserMethods, TemplateMethods, System
):
    def __init__(self, username: str, password: str, panel_address: str):
        super().__init__(username, password, panel_address)
