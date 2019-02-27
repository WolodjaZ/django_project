import re

from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse

EXEMPT_URLS = [reverse(settings.LOGIN_URL)] #don't need authorization
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [reverse(url) for url in settings.LOGIN_EXEMPT_URLS]
    EXEMPT_URLS += ['users/reset-password/<uidb64>/<token>/'] 

class LoginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
            response = self.get_response(request)
            return response

    def process_view(self, request, view_func, view_arg, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info
        print(path,'\n')

        url_is_exempt = any(str(url) in path for url in EXEMPT_URLS) #sprawdzić co z tym

        if path == reverse('users:logout'):
            logout(request)
            return redirect('forum:home')

        if request.user.is_authenticated or url_is_exempt or reverse(settings.LOGIN_REDIRECT_URL) == path:
            return None

        elif request.user.is_authenticated and url_is_exempt:
            return redirect(settings.LOGIN_REDIRECT_URL)

        else:
            return redirect(settings.LOGIN_URL)