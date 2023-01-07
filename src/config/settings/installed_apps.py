INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # libraries
    'django_cleanup',

    # apps
    'apps.common.apps.CommonConfig',
    'apps.catalog.apps.CatalogConfig',
    'apps.comments.apps.CommentsConfig',
    'apps.basket.apps.BasketConfig',
    'apps.authorization.apps.AuthorizationConfig',
    'apps.account.apps.AccountConfig',
    'apps.poster.apps.PosterConfig',
]
