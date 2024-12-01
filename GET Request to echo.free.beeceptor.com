def get_echo_response():
    """
    Sends a GET request to https://echo.free.beeceptor.com and extracts specific headers.

    Returns:
        tuple: A tuple containing the Postman-Token and IP address from the response headers.
    """
    response = requests.get("https://echo.free.beeceptor.com")
    if "Postman-Token" in response.headers and "X-Forwarded-For" in response.headers:
        return response.headers["Postman-Token"], response.headers["X-Forwarded-For"]
    return None, None