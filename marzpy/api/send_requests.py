import json

import aiohttp
from aiohttp import ClientResponseError

from marzpy.api import exceptions


async def send_request(endpoint: str, token, method, data=None):
    try:
        panel_address = token["panel_address"]
        token_type = token["token_type"]
        access_token = token["access_token"]
        request_address = f"{panel_address}/api/{endpoint}"

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"{token_type} {access_token}",
        }
        async with aiohttp.request(
                method=method,
                url=request_address,
                headers=headers,
                data=json.dumps(data)
        ) as response:
            result = await response.json()
            response.raise_for_status()  # Raise an exception for non-200 status codes
            return result

    except ClientResponseError as ex:
        if ex.status != 403:
            detail = result['detail']

            if endpoint.startswith('admin'):
                if ex.status == 409:
                    raise exceptions.AdminAlreadyExists(detail)

                elif ex.status == 404:
                    raise exceptions.AdminNotFound(detail)

                else:
                    raise f"Unknown error : code {ex.status} - message : {detail}"

            elif endpoint.startswith('user_template'):
                raise exceptions.UserNotFound(f"Unknown error : code {ex.status} - message : {detail}")

            elif endpoint.startswith("user"):
                if ex.status == 422:
                    if 'proxies' in detail.keys():
                        error = detail['proxies']

                    elif 'body' in detail.keys():
                        error = detail['body']

                    elif 'status' in detail.keys():
                        error = detail['status']

                    else:
                        error = f"Unknown error : code {ex.status} - message : {detail}"

                    raise exceptions.UserInvalidEntity(error)

                elif ex.status == 409:
                    raise exceptions.UserConflict(detail)

                elif ex.status == 404:
                    raise exceptions.UserNotFound(detail)

            elif endpoint.startswith("node"):
                if ex.status == 422:
                    if 'usage_coefficient' in detail.keys():
                        error = detail['usage_coefficient']
                    else:
                        error = f"Unknown error : code {ex.status} - message : {detail}"

                    raise exceptions.NodeInvalidEntity(error)

                elif ex.status == 409:
                    raise exceptions.NodeConflict(detail)

                elif ex.status == 404:
                    raise exceptions.NodeNotFound(detail)

            else:
                raise exceptions.NotAuthorized("You are not allowed to do this operation")

    except json.JSONDecodeError as ex:
        raise f"JSON Decode Error: {ex}"
