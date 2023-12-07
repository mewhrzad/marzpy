from .api import Methods


class Marzban(Methods):
    def __init__(self, username: str, password: str, panel_address: str, proxy: dict | None = None) -> None:
        super().__init__(username, password, panel_address, proxy)
        self.username = username
        self.password = password
        self.panel_address = panel_address
        self.proxy = proxy
