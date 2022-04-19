from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    print("exc in file utils.py: ", exc)

    response = exception_handler(exc, context)

    if issubclass(type(exc), APIException):
        response.data = {
            'custom_error': True,
            'code': exc.default_code
        }
    # Now add the HTTP status code to the response.

    return response