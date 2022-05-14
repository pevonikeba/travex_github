from loguru import logger
from rest_framework.renderers import JSONRenderer


class CustomRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_content = {}
        if data.get('status_code'):
            response_content['success'] = False
            response_content['error'] = data['status_code'] or 'unknown_error'
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
