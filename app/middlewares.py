from django.utils.deprecation import MiddlewareMixin
from .models import AccessLog


class AccessLogMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path.startswith('/admin') or request.path.startswith('/static') or request.path.startswith('/media'):
            return None
        AccessLog.objects.create(
            user=request.user if request.user.is_authenticated else None,
            view=request.resolver_match.view_name,
            path=request.path,
            method=request.method,
            ip=request.META.get('REMOTE_ADDR')
        )
        return None
