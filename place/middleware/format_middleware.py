import json

from django.core.handlers.wsgi import WSGIRequest
from django.utils.deprecation import MiddlewareMixin
from rest_framework.exceptions import ErrorDetail
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnList


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response


class FormatMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        super().__init__(get_response)
        # One-time configuration and initialization.

    def process_response(self, request, response):
        print('request: ', type(request))
        print('response: ', type(response.content))


