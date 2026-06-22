import time


class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # здесь — до view
        start = time.time()
        ip = request.META.get("REMOTE_ADDR")

        response = self.get_response(request)

        user = request.user.username if request.user.is_authenticated else "anonymous"
        duration = int((time.time() - start) * 1000)
        print(f"{request.method} {request.path} {ip} {user} {duration}ms")

        return response
