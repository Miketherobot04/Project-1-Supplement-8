def send_get_request(url: str):
    """
    Sends an HTTP GET request to a specified URL.

    Args:
        url (str): The URL to send the GET request to.

    Returns:
        dict or tuple: If the content type is JSON, returns a dictionary of the response.
                       Otherwise, returns a tuple of the status code and response text.

    Raises:
        Exception: If the status code is in the range of 400 to 499.
    """
    response = requests.get(url)
    if 400 <= response.status_code <= 499:
        raise Exception(f"Client error: {response.status_code}")

    if "application/json" in response.headers.get("Content-Type", ""):
        return json.loads(response.text)
    
    return response.status_code, response.text