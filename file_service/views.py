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


class AuthYandexView(generic.View):

    def get(self, request: HttpRequest, *args, **kwargs):
        return redirect(get_yandex_auth_url())


class AuthCallbackView(generic.View):
    def get(self, request: HttpRequest, *args, **kwargs):
        access_token = get_access_token(request.GET.get('code'))

        redirect_response = redirect('main_page')
        redirect_response.set_cookie('access_token', access_token, max_age=60)
        return redirect_response
