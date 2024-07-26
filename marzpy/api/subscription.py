import base64

import aiohttp


class Subscription:
    def __init__(self) -> None:
        pass

    async def subsend_request(sub_link: str, endpoint: str):
        try:
            async with aiohttp.request(
                    method="get",
                    url=f"{sub_link}/{endpoint}",
                    headers={"Accept": "application/json"}
            ) as response:
                await response.raise_for_status()  # Raise an exception for non-200 status codes
                result = await response.content
            if endpoint:
                return await response.json
            else:
                return base64.b64decode(result).decode("utf-8")
        except aiohttp.exceptions.RequestException as ex:
            print(f"Request Exception: {ex}")
            return None

    async def get_subscription(self, sub_link: str):
        """Unknow usage!"""
        return await Subscription.subsend_request(sub_link, "")

    async def get_subscription_info(self, sub_link: str):
        """get user information.

        Parameters:
            token (``dict``): subscription token

        Returns:
            `~dict`: information of user
        """
        return await Subscription.subsend_request(sub_link, "info")
