from .api import Methods


class Marzban(Methods):
    def __init__(self, username: str, password: str, panel_address: str) -> None:
        super().__init__(username, password, panel_address)
        self.username = username
        self.password = password
        self.panel_address = panel_address
