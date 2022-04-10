from rest_framework.renderers import JSONRenderer


class CustomRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_content = {}
        if type(data) is dict and data['custom_error'] == True:
            response_content['success'] = False
            response_content['error'] = data['code'] or 'unknown_error'
        else:
            response_content['success'] = True
            response_content['data'] = data
        return super(CustomRenderer, self).render(response_content, accepted_media_type, renderer_context)
