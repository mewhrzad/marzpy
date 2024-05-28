from .send_requests import send_request


class System:
    def __init__(self) -> None:
        pass

    async def get_system_stats(self, token: dict):
        """get server stats.

        Parameters:
            token (``dict``): Authorization token

        Returns:
            `~dict`: server stats
        """
        return await send_request(endpoint="system", token=token, method="get")

    async def get_inbounds(self, token: dict):
        """get server inbounds.

        Parameters:
            token (``dict``): Authorization token

        Returns:
            `~dict`: server inbounds
        """
        return await send_request(endpoint="inbounds", token=token, method="get")

    async def get_hosts(self, token: dict):
        """get server hosts.

        Parameters:
            token (``dict``): Authorization token

        Returns:
            `~dict`: server hosts
        """
        return await send_request(endpoint="hosts", token=token, method="get")

    async def modify_hosts(self, token: dict, data: dict):
        """get server hosts.

        Parameters:
            token (``dict``): Authorization token
            data (``dict``) : new hosts data
        Returns:
            `~dict`: server hosts
        """
        return await send_request(endpoint="hosts", token=token, method="put", data=data)
