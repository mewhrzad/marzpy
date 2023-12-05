from .send_requests import *


class Node:
    def __init__(
        self,
        name="",
        address="",
        port=0,
        api_port=0,
        certificate="",
        id=0,
        xray_version="",
        status="",
        message="",
    ):
        self.name = name
        self.address = address
        self.port = port
        self.api_port = api_port
        self.certificate = certificate
        self.id = id
        self.xray_version = xray_version
        self.status = status
        self.message = message


class NodeMethods:
    def __init__(self) -> None:
        pass

    def add_node(self, node: Node):
        """add new node.

        Parameters:
            token (``dict``): Authorization token

            node (``api.Node``): node object

        Returns:
            `~object`: information of new node
        """
        return Node(
            **send_request(
                endpoint="node", token=self.token, method="post", data=node.__dict__
            )
        )

    def get_node_by_id(self, id: int):
        """get exist node from id.

        Parameters:
            id (``int``): id of node

            token (``dict``): Authorization token

        Returns:
            `~object`: information of new node
        """
        return Node(
            **send_request(endpoint=f"node/{id}", token=self.token, method="get")
        )

    def modify_node_by_id(self, id: int, node: object):
        """edit exist node from id.

        Parameters:
            id (``int``): id of node

            token (``dict``): Authorization token

            node (``api.Node``): node object

        Returns:
            `~object`: information of new node
        """
        request = send_request(
            endpoint=f"node/{id}", token=self.token, method="put", data=node.__dict__
        )
        return Node(**request)

    def delete_node(self, id: int):
        """delete node from id.

        Parameters:
            id (``int``): id of node

            token (``dict``): Authorization token

        Returns:
            `~str`: success
        """
        send_request(endpoint=f"node/{id}", token=self.token, method="delete")
        return "success"

    def get_all_nodes(self):
        """get all nodes.

        Parameters:
            token (``dict``): Authorization token

        Returns:
            `~list of objects`: [Node]
        """
        request = send_request(endpoint="nodes", token=self.token, method="get")
        node_list = [Node()]
        for node in request:
            node_list.append(Node(**node))
        del node_list[0]
        return node_list

    def reconnect_node(self, id: int):
        """reconnect from id.

        Parameters:
            id (``int``): id of node

            token (``dict``): Authorization token

        Returns:
            `~str`: success
        """
        request = send_request(
            endpoint=f"node/{id}/reconnect", token=self.token, method="post"
        )

        return "success"

    def get_nodes_usage(self):
        """get all nodes usage.

        Parameters:
            token (``dict``): Authorization token

        Returns:
            `~dict`: "usage" : []
        """
        request = send_request(endpoint="nodes/usage", token=self.token, method="get")
        return request["usages"]
