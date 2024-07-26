from .send_requests import *


class Template:
    def __init__(
            self,
            name="",
            inbounds={},
            data_limit={},
            expire_duration=0,
            username_prefix="",
            username_suffix="",
            id=None,
    ):
        self.name = name
        self.inbounds = inbounds
        self.data_limit = data_limit
        self.expire_duration = expire_duration
        self.username_prefix = username_prefix
        self.username_suffix = username_suffix
        self.id = id


class TemplateMethods:
    async def get_all_templates(self, token: dict):
        """get all templates list.

        Parameters:
            token (``dict``) : Authorization token

        Returns:
            `~list`: list of templates
        """
        request = await send_request(endpoint="user_template", token=token, method="get")
        template_list = [Template()]
        for user in request:
            template_list.append(Template(**user))
        del template_list[0]
        return template_list

    async def add_template(self, token: dict, template: Template):
        """add new template.

        Parameters:
            token (``dict``) : Authorization token
            template (``api.template object``) : template

        Returns:
            `~object`: information of new template
        """
        request = await send_request(
            endpoint="user_template", token=token, method="post", data=template.__dict__
        )
        return Template(**request)

    async def get_template_by_id(self, token: dict, id: int):
        """get exist template from id.

        Parameters:
            token (``dict``) : Authorization token
            id (``id``) : template id
        Returns:
            `~object`: information of template
        """
        request = await send_request(
            endpoint=f"user_template/{id}", token=token, method="get"
        )

        return Template(**request)

    async def modify_template_by_id(self, token: dict, id: int, template: Template):
        """edit exist template from id.

        Parameters:
            token (``dict``) : Authorization token
            id (``id``) : template id
            template (``object``) template
        Returns:
            `~object`: information of edited template
        """
        request = await send_request(
            endpoint=f"user_template/{id}",
            token=token,
            method="put",
            data=template.__dict__,
        )
        return Template(**request)

    async def delete_template_by_id(self, token: dict, id: int):
        """delete template from id.

        Parameters:
            id (``id``) : template id
            token (``dict``) : Authorization token
        Returns:
            `~str`: success
        """
        await send_request(endpoint=f"user_template/{id}", token=token, method="delete")
        return "success"
