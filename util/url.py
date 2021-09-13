from django.dispatch.dispatcher import logger
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt


def method_dispatch(**table):
    def invalid_method(request, *args, **kwargs):
        logger.warning('Method Not Allowed (%s): %s', request.method, request.path,
                       extra={
                           'status_code': 405,
                           'request': request
                       }
                       )
        return HttpResponseNotAllowed(table.keys())

    def d(request, *args, **kwargs):
        handler = table.get(request.method, invalid_method)
        return handler(request, *args, **kwargs)

    return csrf_exempt(d)
