from .send_requests import send_request


class System:
    def __init__(self) -> None:
        pass

    def get_system_stats(self):
        """get server stats.

        Parameters:
            token (``dict``): Authorization token

        Returns:
            `~dict`: server stats
        """
        return send_request(endpoint="system", token=self.token, method="get")

    def get_inbounds(self):
        """get server inbounds.

        Parameters:
            token (``dict``): Authorization token

        Returns:
            `~dict`: server inbounds
        """
        return send_request(endpoint="inbounds", token=self.token, method="get")

    def get_hosts(self):
        """get server hosts.

        Parameters:
            token (``dict``): Authorization token

        Returns:
            `~dict`: server hosts
        """
        return send_request(endpoint="hosts", token=self.token, method="get")

    def modify_hosts(self, data: dict):
        """get server hosts.

        Parameters:
            token (``dict``): Authorization token
            data (``dict``) : new hosts data
        Returns:
            `~dict`: server hosts
        """
        return send_request(endpoint="hosts", token=self.token, method="put", data=data)
