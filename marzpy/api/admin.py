from .send_requests import *


class Admin:
    def __init__(self, username: str, is_sudo: bool, password: str, telegram_id: int = None, discord_webhook: str = None, ):
        self.username = username
        self.is_sudo = is_sudo
        self.password = password
        self.telegram_id = telegram_id
        self.discord_webhook = discord_webhook


class AdminMethods:
    def __init__(self, username: str, password: str, panel_address: str):
        self.username = username
        self.password = password
        self.panel_address = panel_address

    async def get_token(self):
        """login for Authorization token

        Returns: `~dict`: Authorization token
        """
        try:
            async with aiohttp.request(
                    "post",
                    url=f"{self.panel_address}/api/admin/token",
                    data={"username": self.username, "password": self.password},
            ) as response:
                # response.raise_for_status()  # Raise an exception for non-200 status codes
                result = await response.json()
                result["panel_address"] = self.panel_address
                return result
        except aiohttp.exceptions.RequestException as ex:
            print(f"Request Exception: {ex}")
            return None
        except json.JSONDecodeError as ex:
            print(f"JSON Decode Error: {ex}")
            return None

    async def get_current_admin(self, token: dict):
        """get current admin who has logged in.

        Parameters:
            token (``dict``) : Authorization token

        Returns:
        `~dict`: {"username": "str" , "is_sudo": true}
        """
        return await send_request(endpoint="admin", token=token, method="get")

    async def create_admin(self, token: dict, admin: Admin):
        """add new admin.

        Parameters:
            token (``dict``) : Authorization token
            admin (``Admin``) : information of new admin

        Returns:
        `~dict`: username && is_sudo
        """
        await send_request(endpoint="admin", token=token, method="post", data=admin.__dict__)
        return "success"

    async def modify_admin(self, token: dict, username: str, admin: Admin):
        """change exist admins password.

        *you cant modify sudo admins password*

        Parameters:
            token (``dict``) : Authorization token
            username (``str``) : username of admin
            admin (``Admin``) : information of new admin

        Returns:
        `~dict`: username && is_sudo
        """
        admin_dict = admin.__dict__
        admin_dict.pop('username')
        await send_request(
            endpoint=f"admin/{username}",
            token=token,
            method="put",
            data=admin_dict,
        )
        return "success"

    async def delete_admin(self, token: dict, username: str):
        """delete admin.

        Parameters:
            username (``str``) : username of admin
            token (``dict``) : Authorization token

        Returns:
        `~str`: success
        """
        await send_request(endpoint=f"admin/{username}", token=token, method="delete")
        return "success"

    async def get_all_admins(self, token: dict):
        """get all admins.

        Parameters:
            token (``dict``) : Authorization token

        Returns:
        `~list`: [{username && is_sudo}]
        """
        return await send_request(endpoint=f"admins", token=token, method="get")
