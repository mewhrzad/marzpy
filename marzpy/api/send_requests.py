import aiohttp, json

import aiohttp.client_exceptions
import aiohttp.http_exceptions


async def send_request(endpoint, token, method, data=None):
    try:
        print(json.dumps(data))
        panel_address = token["panel_address"]
        token_type = token["token_type"]
        access_token = token["access_token"]
        request_address = f"{panel_address}/api/{endpoint}"
        headers = {
            "accept": "application/json",
            "Authorization": f"{token_type} {access_token}",
            "Content-Type": "application/json"
        }
        async with aiohttp.request(
            method=method,
            url=request_address,
            headers=headers,
            data=json.dumps(data),
            raise_for_status=True,
            ) as response :
            return await response.json()
    except json.JSONDecodeError as ex:
        raise f"JSON Decode Error: {ex}"