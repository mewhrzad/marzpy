import aiohttp, json, base64


class Subscription:
    def __init__(self) -> None:
        pass

    async def subsend_request(sub_link: str, endpoint: str):
        async with aiohttp.request(
            method="get",
            url = f"{sub_link}/{endpoint}",
            headers={"Accept": "application/json"},
            raise_for_status=True,
            ) as response : 
            result = await response.text()
            if endpoint:
                return await response.json()
            else:
                return base64.b64decode(result).decode("utf-8")

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