import rollbar
from django.utils.deprecation import MiddlewareMixin

class RollbarNotifierMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        rollbar.report_exc_info(extra_data={
            'request': request,
        })