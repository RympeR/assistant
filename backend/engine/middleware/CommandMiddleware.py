class CommandMiddleware(object):
    class ResponseMiddleware(object):

        def __call__(self, request):
            setattr(request, '_dont_enforce_csrf_checks', True)
            return request
