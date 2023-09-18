import requests, json, base64


class Subscription:
    def __init__(self) -> None:
        pass

    def subsend_request(sub_link: str, endpoint: str):
        try:
            request_address = f"{sub_link}/{endpoint}"
            headers = {
                "Accept": "application/json",
            }
            response = requests.request("get", request_address, headers=headers)
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
        return Subscription.subsend_request(sub_link, "")

    def get_subscription_info(self, sub_link: str):
        """get user information.

        Parameters:
            token (``dict``): subscription token

        Returns:
            `~dict`: information of user
        """
        return Subscription.subsend_request(sub_link, "info")
