from rest_framework.exceptions import ValidationError, APIException
from requests import Response


def handle_bitget_response(response: Response) -> list:
    """
    Handle Bitget API response.

    Parameters:
        response (requests.Response): The response object returned by a Bitget API call.

    Returns:
        dict: Parsed JSON data if the response is successful and the API code equals "00000".

    Raises:
        Exception: If the response status is not 200, the JSON is invalid,
                   or the API returns an error code.
    """
    try:
        data = response.json()
    except ValueError:
        raise APIException("Invalid JSON response received from Bitget API.")

    # Check HTTP status code and Bitget API specific code
    if response.status_code not in [200, 201] or data.get("code") != "00000":
        error_message = data.get("msg", "Unknown error")
        raise ValidationError(
            f"Bitget API error: {error_message} (status: {response.status_code})"
        )

    return data.get("data", [])
