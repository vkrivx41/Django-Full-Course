from collections import defaultdict
import time

from django.http import JsonResponse


class RateLimitMiddleware:
    RATE_LIMIT = 5
    WINDOW = 60  # number of seconds

    def __init__(self, get_response):
        self.get_response = get_response
        self.requests = defaultdict(list)

    def __call__(self, request):
        user = self.user if request.user.is_authenticated else "Anon"
        ip = request.META.get("REMOTE_ADDR")

        start = time.time()
        cache_key = f"{ip}:{user}"

        timestamps = self.requests[cache_key]

        self.requests[cache_key] = [
            t for t in timestamps if start - t < self.WINDOW
        ]

        if len(self.requests[cache_key]) >= self.RATE_LIMIT:
            return JsonResponse({
                "detail": "Too many requests",
                "success": False
            }, status=429)

        self.requests[cache_key].append(start)

        response = self.get_response(request)

        duration = time.time() - start

        print(f"Request took: {duration:.3f}s")
        
        return response
