import time
import logging


logging.basicConfig(
    level=logging.DEBUG
)

logger = logging.getLogger("request_logger")


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        user = request.user if request.user.is_authenticated else "Anon"
        ip = request.META.get("REMOTE_ADDR")

        response = self.get_response(request)

        duration = time.time() - start_time

        logger.info(
            f"Method={request.method} - Path={request.path} | "
            f"User={user} - IP={ip} |"
            f"Status={response.status_code} - Time={duration:.3f}s"
        )

        if duration > 0.5:
            logger.warning(f"Slow Request: {request.path} took {duration:.3f}s")

        if response.status_code == 500:
            logger.error(f"Error Occured: {request.path}")

        return response
    