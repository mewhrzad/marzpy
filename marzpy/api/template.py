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
    def get_all_templates(self, token: dict):
        """get all templates list.

        Parameters:
            token (``dict``) : Authorization token

        Returns:
            `~list`: list of templates
        """
        request = send_request(endpoint="user_template", token=token, method="get")
        template_list = [Template()]
        for user in request:
            template_list.append(Template(**user))
        del template_list[0]
        return template_list

    def add_template(self, template: Template, token: dict):
        """add new template.

        Parameters:
            token (``dict``) : Authorization token
            template (``api.template object``) : template

        Returns:
            `~object`: information of new template
        """
        request = send_request(
            endpoint="user_template", token=token, method="post", data=template.__dict__
        )
        return Template(**request)

    def get_template_by_id(self, id: int, token: dict):
        """get exist template from id.

        Parameters:
            id (``id``) : template id
            token (``dict``) : Authorization token
        Returns:
            `~object`: information of template
        """
        request = send_request(
            endpoint=f"user_template/{id}", token=token, method="get"
        )

        return Template(**request)

    def modify_template_by_id(self, id: int, token: dict, template: Template):
        """edit exist template from id.

        Parameters:
            id (``id``) : template id
            token (``dict``) : Authorization token
            template (``object``) template
        Returns:
            `~object`: information of edited template
        """
        request = send_request(
            endpoint=f"user_template/{id}",
            token=token,
            method="put",
            data=template.__dict__,
        )
        return Template(**request)

    def delete_template_by_id(self, id: int, token: dict):
        """delete template from id.

        Parameters:
            id (``id``) : template id
            token (``dict``) : Authorization token
        Returns:
            `~str`: success
        """
        send_request(endpoint=f"user_template/{id}", token=token, method="delete")
        return "success"
