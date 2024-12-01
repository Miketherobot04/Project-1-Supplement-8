# Project 1 Supplement – 8

## Objective
This project demonstrates the usage of the `requests` module in Python. It includes functions for HTTP GET and POST requests and ensures that each function is well-documented and unit-tested.

## Functions

### `send_get_request(url: str)`
- Sends an HTTP GET request to the specified URL.
- Returns:
  - Dictionary if the response is JSON.
  - Tuple of status code and response text otherwise.
- Raises an exception for client errors (status codes 400–499).

### `get_echo_response()`
- Sends a GET request to `https://echo.free.beeceptor.com`.
- Returns a tuple of:
  - `Postman-Token`
  - IP address from the response headers.

### `post_hello_world()`
- Sends a POST request to `https://echo.free.beeceptor.com` with a JSON object:
  ```json
  {"hello": "world"}