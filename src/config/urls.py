from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.common.urls')),
    path('admin/', admin.site.urls),
    path('catalog/', include('apps.catalog.urls')),
    path('comments/', include('apps.comments.urls')),
    path('basket/', include('apps.basket.urls')),
    path('authorization/', include('apps.authorization.urls')),
    path('account/', include('apps.account.urls')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += staticfiles_urlpatterns()
