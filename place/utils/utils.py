from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler
from rest_framework.pagination import PageNumberPagination

from place.models import Place


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    # if issubclass(type(exc), APIException):
    #     print('issubclass')
    #     response.data = {
    #         'custom_error': True,
    #         'code': exc.default_code
    #     }
    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
    return response


def create_section(obj: Place, key: str, icon_name: str, display_type: str, create_children):
    return {
        "title": key.capitalize(),
        "key": key,
        "icon_name": icon_name,
        "display_type": display_type,
        "children": map(create_children, getattr(obj, key).all()),
    }


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000