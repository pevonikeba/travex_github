from loguru import logger


class CheckAchievementMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        logger.warning('start')
        response = self.get_response(request)
        logger.warning('end')

        # Code to be executed for each request/response after
        # the view is called.

        return response