from .send_requests import *


class Core:
    def __init__(self) -> None:
        pass

    def get_xray_core(self):
        """get xray core.

        Parameters:
            token (``dict``): Authorization token

        Returns:
            `~dict`: xray core
        """
        return send_request(endpoint="core", token=self.token, method="get")

    def restart_xray_core(self):
        """restart xray core.

        Parameters:
            token (``dict``): Authorization token

        Returns:
            `~str`: success
        """
        send_request(endpoint="core/restart", token=self.token, method="post")
        return "success"

    def get_xray_config(self):
        """get xray config.

        Parameters:
            token (``dict``): Authorization token

        Returns:
            `~dict`: xray config
        """
        return send_request(endpoint="core/config", token=self.token, method="get")

    def modify_xray_config(self, config: json):
        """edit xray config.

        Parameters:
            token (``dict``): Authorization token
            config (``json``): json of new config

        Returns:
            `~str`: success
        """
        send_request(
            endpoint="core/config", token=self.token, method="put", data=config
        )
        return "success"
