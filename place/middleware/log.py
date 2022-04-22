from loguru import logger
import time
import socket
import json
from django.core.mail import send_mail

from travex import settings


class APILogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        log_data = {}

        # Only logging "*/api/*" patterns
        if "/api/" in str(request.get_full_path()):
            req_body = json.loads(request.body.decode("utf-8")) if request.body else {}
            log_data["request_body"] = req_body

            # request passes on to controller
            response = self.get_response(request)

            log_data[">>>>>>>>>"] = ">>>>>>>>>"
            log_data["remote_address"] = request.META["REMOTE_ADDR"]
            log_data["server_hostname"] = socket.gethostname()
            log_data["request_method"] = request.method
            log_data["request_path"] = request.get_full_path()
            log_data["run_time"] = time.time() - start_time
            log_data["<<<<<<<<<<"] = "<<<<<<<<<<"

            # add runtime to our log_data
            if response and response["content-type"] == "application/json":
                response_body = json.loads(response.content.decode("utf-8"))
                log_data["response_body"] = response_body

            # logger.info(log_data)

            if request.method == "POST":
                send_mail(
                    'Logging from travex',
                    str(log_data),
                    settings.EMAIL_HOST_USER,
                    ['arslion@yandex.ru'],
                    fail_silently=False,
                )

        return response