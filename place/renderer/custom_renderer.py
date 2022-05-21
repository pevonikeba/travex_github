from loguru import logger
from rest_framework.renderers import JSONRenderer
import enum


class FullPath(enum.Enum):
    reset_password = '/auth/users/reset_password/'

# logger.warning(renderer_context.get('request').get_full_path())


class CustomRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_content = {}
        logger.info('here')
        if isinstance(data, dict) and data.get('status_code'):
            response_content['success'] = False
            error = 'unknown_error'
            detail = data.get('detail')
            if detail:
                if detail.title() == 'Invalid Username/Password.':
                    error = 'authentication_failed'
                else:
                    error = data['token_error'] or data
            response_content['error'] = error
            # response_content['message'] = data
            # response_content['token_error'] = or 'unknown_error'
        else:
            NoneType = type(None)
            if not isinstance(data, str) and not isinstance(data, NoneType) and not isinstance(data, int):
                if "access_token" in data:
                    data['access'] = data.pop('access_token')
                if "refresh_token" in data:
                   data['refresh'] = data.pop('refresh_token')
            response_content['success'] = True
            response_content['data'] = data
        return super(CustomRenderer, self).render(response_content, accepted_media_type, renderer_context)
