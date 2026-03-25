from django.http import JsonResponse, HttpResponse
from django.conf import settings


class GlobalHandleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if getattr(settings, 'MAINTENANCE_MODE', False):
            if not request.user.is_staff:
                return HttpResponse("<h1>Site Under Maintenance</h1>", status=503)
            
        response = self.get_response(request)

        if response.status_code == 500:
            return JsonResponse({
                'detail': "An error occurred, try again later.",
                'success': False
            }, status=500)

        return response
    