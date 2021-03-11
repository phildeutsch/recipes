from django.utils import translation
from django.utils.deprecation import MiddlewareMixin

class MyLocaleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated and request.user.profile.language:
            translation.activate(request.user.profile.language)
            request.LANGUAGE_CODE = translation.get_language()
