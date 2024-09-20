from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import generic

from file_service.utils import get_access_token, get_yandex_auth_url


class MainPageView(generic.TemplateView):
    default_template_name = 'main.html'
    after_auth_template_name = 'public_url.html'

    def get(self, request: HttpRequest, *args, **kwargs):
        if request.COOKIES.get('access_token'):
            return render(request, self.after_auth_template_name)
        return render(request, self.default_template_name)
