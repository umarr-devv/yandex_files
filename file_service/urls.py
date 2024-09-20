from django.urls import path

from file_service.views import MainPageView, AuthYandexView, AuthCallbackView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('auth/', AuthYandexView.as_view(), name='yandex_auth'),
    path('callback/', AuthCallbackView.as_view())
]
