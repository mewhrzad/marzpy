from .send_requests import *

async def delete_if_exist(dic,keys:list):
    for key in keys:
        if key in dic:
            del dic[key]
    return dic

class User:
    def __init__(
        self,
        username: str,
        proxies: dict,
        inbounds: dict,  
        data_limit: float,
        data_limit_reset_strategy: str = "no_reset",
        status="",
        expire: float = 0,
        used_traffic=0,
        lifetime_used_traffic=0,
        created_at="",
        links=[],
        subscription_url="",
        excluded_inbounds={},
        note = "",
        on_hold_timeout= 0,
        on_hold_expire_duration = 0,
        sub_updated_at = 0,
        online_at = 0,
        sub_last_user_agent:str = "",
        auto_delete_in_days:int = 0,
        admin=None,
        **_, # Stop causing error when marzban update
        
    ):
        self.username = username
        self.proxies = proxies
        self.inbounds = inbounds
        self.expire = expire
        self.data_limit = data_limit
        self.data_limit_reset_strategy = data_limit_reset_strategy
        self.status = status
        self.used_traffic = used_traffic
        self.lifetime_used_traffic = lifetime_used_traffic
        self.created_at = created_at
        self.links = links
        self.subscription_url = subscription_url
        self.excluded_inbounds = excluded_inbounds
        self.note = note
        self.on_hold_timeout = on_hold_timeout
        self.on_hold_expire_duration = on_hold_expire_duration
        self.sub_last_user_agent = sub_last_user_agent
        self.online_at = online_at
        self.sub_updated_at = sub_updated_at
        self.auto_delete_in_days = auto_delete_in_days
        self.admin = admin
        
class UserMethods:
    async def add_user(self, user: User, token: dict):
        """add new user.

        Parameters:
            user (``api.User``) : User Object

            token (``dict``) : Authorization token

        Returns: `~User`: api.User object
        """
        user.status = "active"
        if user.on_hold_expire_duration:
            user.status = "on_hold"
        request = await send_request(
            endpoint="user", token=token, method="post", data=user.__dict__
        )
        return User(**request)

    async def get_user(self, user_username: str, token: dict):
        """get exist user information by username.

        Parameters:
            user_username (``str``) : username of user

            token (``dict``) : Authorization token

        Returns: `~User`: api.User object
        """
        request = await send_request(f"user/{user_username}", token=token, method="get")
        return User(**request)

    async def modify_user(self, user_username: str, token: dict, user: object):
        """edit exist user by username.

        Parameters:
            user_username (``str``) : username of user

            token (``dict``) : Authorization token

            user (``api.User``) : User Object

        Returns: `~User`: api.User object
        """
        request = await send_request(f"user/{user_username}", token, "put", user.__dict__)
        return User(**request)

    async def delete_user(self, user_username: str, token: dict):
        """delete exist user by username.

        Parameters:
            user_username (``str``) : username of user

            token (``dict``) : Authorization token

        Returns: `~str`: success
        """
        await send_request(f"user/{user_username}", token, "delete")
        return "success"

    async def reset_user_traffic(self, user_username: str, token: dict):
        """reset exist user traffic by username.

        Parameters:
            user_username (``str``) : username of user

            token (``dict``) : Authorization token

        Returns: `~str`: success
        """
        await send_request(f"user/{user_username}/reset", token, "post")
        return "success"
    
    async def revoke_sub(self, user_username: str, token: dict):
        """Revoke users subscription (Subscription link and proxies) traffic by username.

        Parameters:
            user_username (``str``) : username of user

            token (``dict``) : Authorization token

        Returns: `~str`: success
        """
        request = await send_request(f"user/{user_username}/revoke_sub", token, "post")
        return User(**request)
    
    async def get_all_users(self, token: dict, username=None, status=None):
        """get all users list.

        Parameters:
            token (``dict``) : Authorization token

        Returns:
            `~list`: list of users
        """
        endpoint = "users"
        if username:
            endpoint += f"?username={username}"
        if status:
            if "?" in endpoint:
                endpoint += f"&status={status}"
            else:
                endpoint += f"?status={status}"
        request = await send_request(endpoint, token, "get")
        user_list = [
            User(
                username="",
                proxies={},
                inbounds={},
                expire=0,
                data_limit=0,
                data_limit_reset_strategy="",
            )
        ]
        for user in request["users"]:
            user_list.append(User(**user))
        del user_list[0]
        return user_list

    async def reset_all_users_traffic(self, token: dict):
        """reset all users traffic.

        Parameters:
            token (``dict``) : Authorization token

        Returns: `~str`: success
        """
        await send_request("users/reset", token, "post")
        return "success"

    async def get_user_usage(self, user_username: str, token: dict):
        """get user usage by username.

        Parameters:
            user_username (``str``) : username of user

            token (``dict``) : Authorization token

        Returns: `~dict`: dict of user usage
        """
        return await send_request(f"user/{user_username}/usage", token, "get")["usages"]

    async def get_all_users_count(self, token: dict):
        """get all users count.

        Parameters:
            token (``dict``) : Authorization token

        Returns: `~int`: count of users
        """
        return await self.get_all_users(token)["content"]["total"]
