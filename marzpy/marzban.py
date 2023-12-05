from .api import Methods
from .api import Admin


class Marzban(Methods):
    def __init__(self, username: str, password: str, panel_address: str) -> None:
        super().__init__(username, password, panel_address)
        self.username = username
        self.password = password
        self.panel_address = panel_address

    @property
    def token(self):
        return Methods.get_token(
            Admin(self.username, self.password, self.panel_address)
        )
