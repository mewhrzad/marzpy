from .send_requests import *


class Core:
    def __init__(self) -> None:
        pass

    async def get_xray_core(self, token: dict):
        """get xray core.

        Parameters:
            token (``dict``): Authorization token

        Returns:
            `~dict`: xray core
        """
        return await send_request(endpoint="core", token=token, method="get")

    async def restart_xray_core(self, token: dict):
        """restart xray core.

        Parameters:
            token (``dict``): Authorization token

        Returns:
            `~str`: success
        """
        await send_request(endpoint="core/restart", token=token, method="post")
        return "success"

    async def get_xray_config(self, token: dict):
        """get xray config.

        Parameters:
            token (``dict``): Authorization token

        Returns:
            `~dict`: xray config
        """
        return await send_request(endpoint="core/config", token=token, method="get")

    async def modify_xray_config(self, token: dict, config: json):
        """edit xray config.

        Parameters:
            token (``dict``): Authorization token
            config (``json``): json of new config

        Returns:
            `~str`: success
        """
        await send_request(endpoint="core/config", token=token, method="put", data=config)
        return "success"