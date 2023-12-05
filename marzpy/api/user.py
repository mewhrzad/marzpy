from .send_requests import *


class User:
    def __init__(
        self,
        username: str,
        proxies: dict,
        inbounds: dict,
        expire: float,
        data_limit: float,
        data_limit_reset_strategy: str,
        status="",
        used_traffic=0,
        lifetime_used_traffic=0,
        created_at="",
        links=[],
        subscription_url="",
        excluded_inbounds={},
        **kwargs
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


class UserMethods:
    def add_user(self, user: User, token: dict):
        """add new user.

        Parameters:
            user (``api.User``) : User Object

            token (``dict``) : Authorization token

        Returns: `~User`: api.User object
        """
        request = send_request(
            endpoint="user", token=token, method="post", data=user.__dict__
        )

        return User(**request)

    def get_user(self, user_username: str, token: dict):
        """get exist user information by username.

        Parameters:
            user_username (``str``) : username of user

            token (``dict``) : Authorization token

        Returns: `~User`: api.User object
        """
        request = send_request(f"user/{user_username}", token=token, method="get")
        return User(**request)

    def modify_user(self, user_username: str, token: dict, user: object):
        """edit exist user by username.

        Parameters:
            user_username (``str``) : username of user

            token (``dict``) : Authorization token

            user (``api.User``) : User Object

        Returns: `~User`: api.User object
        """
        request = send_request(f"user/{user_username}", token, "put", user.__dict__)
        return User(**request)

    def delete_user(self, user_username: str, token: dict):
        """delete exist user by username.

        Parameters:
            user_username (``str``) : username of user

            token (``dict``) : Authorization token

        Returns: `~str`: success
        """
        send_request(f"user/{user_username}", token, "delete")
        return "success"

    def reset_user_traffic(self, user_username: str, token: dict):
        """reset exist user traffic by username.

        Parameters:
            user_username (``str``) : username of user

            token (``dict``) : Authorization token

        Returns: `~str`: success
        """
        send_request(f"user/{user_username}/reset", token, "post")
        return "success"

    def get_all_users(self, token: dict):
        """get all users list.

        Parameters:
            token (``dict``) : Authorization token

        Returns:
            `~list`: list of users
        """
        request = send_request("users", token, "get")
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

    def reset_all_users_traffic(self, token: dict):
        """reset all users traffic.

        Parameters:
            token (``dict``) : Authorization token

        Returns: `~str`: success
        """
        send_request("users/reset", token, "post")
        return "success"

    def get_user_usage(self, user_username: str, token: dict):
        """get user usage by username.

        Parameters:
            user_username (``str``) : username of user

            token (``dict``) : Authorization token

        Returns: `~dict`: dict of user usage
        """
        return send_request(f"user/{user_username}/usage", token, "get")["usages"]

    def get_all_users_count(self, token: dict):
        """get all users count.

        Parameters:
            token (``dict``) : Authorization token

        Returns: `~int`: count of users
        """
        return self.get_all_users(token)["content"]["total"]
