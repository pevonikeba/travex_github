from loguru import logger
from rest_framework.renderers import JSONRenderer
import enum
# import logging
# logger = logging.getLogger('django')
from loguru import logger
from rest_framework.status import is_client_error

from place.utils.utils import SocialAccountError

# logger.warning(renderer_context.get('request').get_full_path())


class CustomRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_content = {}
        request = renderer_context.get('request')
        response = renderer_context.get('response')
        if is_client_error(renderer_context.get('response').status_code):
            response_content['success'] = False
            # logger.warning(renderer_context)
            error = response.data
            logger.warning(response.data)
            detail = data.get('detail')
            if request.path == '/users/' and request.method == 'POST':
                social_account_error = response.data.get(SocialAccountError.ERROR_NAME)
                if social_account_error:
                    error = social_account_error
            elif request.path == '/auth/jwt/create/' and request.method == 'POST':
                social_account_error = response.data.get(SocialAccountError.ERROR_NAME)
                if social_account_error:
                    error = social_account_error
                # else
            elif detail: # elif request.path == '/auth/users/me/' and request.method == 'GET':
                if detail.title() == 'Invalid Username/Password.':
                    error = 'authentication_failed'
                else:
                    error = data['token_error'] or data
            response_content['error'] = error
        else:
            if request.path == '/auth/users/reset_password/' and request.method == 'POST':
                renderer_context.get('response').status_code = 200
            NoneType = type(None)
            if not isinstance(data, str) and not isinstance(data, NoneType) and not isinstance(data, int):
                if "access_token" in data:
                    data['access'] = data.pop('access_token')
                if "refresh_token" in data:
                   data['refresh'] = data.pop('refresh_token')
            response_content['success'] = True
            response_content['data'] = data
        return super(CustomRenderer, self).render(response_content, accepted_media_type, renderer_context)
