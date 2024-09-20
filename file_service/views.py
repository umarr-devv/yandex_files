from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import generic

from file_service.utils import get_access_token, get_yandex_auth_url, get_files_by_public_key


class MainPageView(generic.TemplateView):
    main_page_template = 'main.html'
    public_url_template = 'public_url.html'
    files_list_template = 'files_list.html'

    def get(self, request: HttpRequest, *args, **kwargs):
        if request.COOKIES.get('access_token'):
            return render(request, self.public_url_template)
        return render(request, self.main_page_template)

    def post(self, request: HttpRequest, *args, **kwargs):
        public_key = request.POST.get('public_key')
        access_token = request.COOKIES.get('access_token')

        files_response = get_files_by_public_key(public_key, access_token)
        if files_response.status_code == 200:
            return render(request, self.files_list_template, context={
                'title': 'Список файлов',
                'files': files_response.json()['_embedded']['items']
            })


class AuthYandexView(generic.View):

    def get(self, request: HttpRequest, *args, **kwargs):
        return redirect(get_yandex_auth_url())


class AuthCallbackView(generic.View):
    def get(self, request: HttpRequest, *args, **kwargs):
        access_token = get_access_token(request.GET.get('code'))

        redirect_response = redirect('main_page')
        redirect_response.set_cookie('access_token', access_token, max_age=60)
        return redirect_response
