from .send_requests import *


class Admin:
    def __init__(self, username: str, password: str, panel_address: str):
        self.username = username
        self.password = password
        self.panel_address = panel_address

    def get_token(self):
        """login for Authorization token

        Returns: `~dict`: Authorization token
        """
        try:
            request_address = f"{self.panel_address}/api/admin/token"
            payload = {"username": self.username, "password": self.password}
            response = requests.post(
                request_address,
                data=payload,
                timeout=3000,
                headers={
                    "Accept": "application/json",
                    "Content-Type": "application/x-www-form-urlencoded",
                },
            )
            response.raise_for_status()  # Raise an exception for non-200 status codes
            result = json.loads(response.content)
            result["panel_address"] = self.panel_address
            return result
        except requests.exceptions.RequestException as ex:
            print(f"Request Exception: {ex}")
            return None
        except json.JSONDecodeError as ex:
            print(f"JSON Decode Error: {ex}")
            return None

    def get_current_admin(self, token: dict):
        """get current admin who has logged in.

        Parameters:
            token (``dict``) : Authorization token

        Returns:
        `~dict`: {"username": "str" , "is_sudo": true}
        """
        return send_request(endpoint="admin", token=token, method="get")

    def create_admin(self, token: dict, data: dict):
        """add new admin.

        Parameters:
            token (``dict``) : Authorization token
            data (``dict``) : information of new admin

        Returns:
        `~dict`: username && is_sudo
        """
        send_request(endpoint="admin", token=token, method="post", data=data)
        return "success"

    def change_admin_password(self, username: str, token: dict, data: dict):
        """change exist admins password.

        *you cant modify sudo admins password*

        Parameters:
            username (``str``) : username of admin
            token (``dict``) : Authorization token
            data (``dict``) : information of new admin

        Returns:
        `~dict`: username && is_sudo
        """
        send_request(
            endpoint=f"admin/{username}",
            token=token,
            method="put",
            data=data,
        )
        return "success"

    def delete_admin(self, username: str, token: dict):
        """delete admin.

        Parameters:
            username (``str``) : username of admin
            token (``dict``) : Authorization token

        Returns:
        `~str`: success
        """
        send_request(endpoint=f"admin/{username}", token=token, method="delete")
        return "success"

    def get_all_admins(self, token: dict):
        """get all admins.

        Parameters:
            token (``dict``) : Authorization token

        Returns:
        `~list`: [{username && is_sudo}]
        """
        return send_request(endpoint=f"admins", token=token, method="get")
