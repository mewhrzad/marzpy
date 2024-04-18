import aiohttp, json


async def send_request(endpoint, token, method, data=None):
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
        data=json.dumps(data),
        raise_for_status=True
        ) as response :
        result = await response.json()
        return result
