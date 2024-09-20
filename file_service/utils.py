import requests
from requests import Response

from config import settings


def get_access_token(code: str) -> str:
    token_response = requests.post(settings.YANDEX_TOKEN_URL, data={
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': settings.CLIENT_ID,
        'client_secret': settings.CLIENT_SECRET,
        'redirect_uri': settings.REDIRECT_URI
    }).json()
    return token_response.get('access_token')


def get_yandex_auth_url():
    return f"{settings.YANDEX_OAUTH_URL}?response_type=code&client_id={settings.CLIENT_ID}&redirect_uri={settings.REDIRECT_URI}"


def get_files_by_public_key(public_key: str, access_token: str) -> Response:
    return requests.get(
        settings.YANDEX_PUBLIC_API_URL, params={'public_key': public_key},
        headers={'Authorization': f'OAuth {access_token}'}
    )
