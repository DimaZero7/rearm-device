LOGIN_URL = '/authorization/login/google-oauth2/'
LOGIN_REDIRECT_URL = 'account:account'
LOGOUT_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config['auth']['google_oauth2_key']
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config['auth']['google_oauth2_SECRET']
SOCIAL_AUTH_URL_NAMESPACE = 'social'
