def post_hello_world():
    """
    Sends a POST request to https://echo.free.beeceptor.com with a JSON object.

    Returns:
        dict: The response from the server.
    """
    payload = {"hello": "world"}
    response = requests.post("https://echo.free.beeceptor.com", json=payload)
    return response.json() if "application/json" in response.headers.get("Content-Type", "") else response.text