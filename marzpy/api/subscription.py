import base64
import json

import requests


class Subscription:
    def __init__(self) -> None:
        pass

    def subsend_request(sub_link: str, endpoint: str, proxy: dict | None = None):
        try:
            request_address = f"{sub_link}/{endpoint}"
            headers = {
                "Accept": "application/json",
            }
            response = requests.request(
                "get", request_address, headers=headers, proxies=proxy)
            response.raise_for_status()  # Raise an exception for non-200 status codes
            result = response.content
            if endpoint:
                return json.loads(response.content)
            else:
                return base64.b64decode(result).decode("utf-8")
        except requests.exceptions.RequestException as ex:
            print(f"Request Exception: {ex}")
            return None

    def get_subscription(self, sub_link: str):
        """Unknow usage!"""
        return Subscription.subsend_request(sub_link, "", proxy=self.proxy)

    def get_subscription_info(self, sub_link: str):
        """get user information.

        Parameters:
            token (``dict``): subscription token

        Returns:
            `~dict`: information of user
        """
        return Subscription.subsend_request(sub_link, "info", proxy=self.proxy)
