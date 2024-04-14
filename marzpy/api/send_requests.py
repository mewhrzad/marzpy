import aiohttp, json


async def send_request(endpoint, token, method, data=None):
    try:
        panel_address = token["panel_address"]
        token_type = token["token_type"]
        access_token = token["access_token"]
        request_address = f"{panel_address}/api/{endpoint}"
        headers = {
            "accept": "application/json",
            "Authorization": f"{token_type} {access_token}",
        }
        async with aiohttp.request(
            method=method,
            url=request_address,
            headers=headers,
            data=json.dumps(data)
            ) as response :
            response.raise_for_status()  # Raise an exception for non-200 status codes
            result = await response.json()
            return result
    except aiohttp.exceptions.RequestException as ex:
        if response.content:
            raise Exception(f"Request Exception: { await response.content }")
        else:
            raise ex
    except json.JSONDecodeError as ex:
        raise f"JSON Decode Error: {ex}"