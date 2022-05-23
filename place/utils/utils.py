import enum

from loguru import logger
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler
from rest_framework.pagination import PageNumberPagination

from place.models import Place

# import logging

# logger = logging.getLogger('django')
from loguru import logger


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
    # path = context.get('request').path
    # if path == '/auth/jwt/create/':
    #     # logger.info(response.data)
    #     pass
    # logger.warning(f'{exc}:::{context}')
    # logger.info(dir(context.get('request')))

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['token_error'] = ''
        response.data['status_code'] = response.status_code
        try:
            if response.data.get("messages")[0].get("token_class").title() == "Accesstoken" and \
                    response.data.get("messages")[0].get("token_class").code == "token_not_valid":
                response.data["token_error"] = "access_" + response.data.get("messages")[0].get("token_class").code
        except:
            try:
                if response.data.get('detail').code == 'token_not_valid':
                    response.data["token_error"] = "refresh_token_not_valid"
            except:
                pass

    return response


class SocialAccountError:
    ERROR_NAME = 'social_account_error'
    GOOGLE = 'need_google_sign_in'
    APPLE = 'need_apple_sign_in'
    MULTIPLE = 'need_social_sign_in'
    NO_ERROR = ''


def check_has_social_account_error_msg(social_account_brands: dict):
    return social_account_brands.get(SocialAccountError.ERROR_NAME)


def get_social_account_brands(user):
    social_account_error = SocialAccountError.ERROR_NAME
    social_account_brands = []
    if user:
        for social_account in user.socialaccount_set.all():
            social_account_brands.append(social_account.get_provider_account().get_brand().get('name'))
    if social_account_brands:
        if len(social_account_brands) > 1:
            return {social_account_error: SocialAccountError.MULTIPLE}
        elif 'Google' in social_account_brands:
            return {social_account_error: SocialAccountError.GOOGLE}
        elif 'Apple' in social_account_brands:
            return {social_account_error: SocialAccountError.APPLE}
    return {social_account_error: SocialAccountError.NO_ERROR}


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
