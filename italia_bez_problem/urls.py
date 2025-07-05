from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language

# URLs that will have language prefix (e.g., /it/admin/, /en/admin/, /it/home/)
urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls), # Admin URL now included in i18n_patterns
    path('', include('main.urls')),
    # Add other i18n-prefixed URLs here if needed
)

# URLs that do NOT have a language prefix (e.g., for setting language)
urlpatterns += [
    path('i18n/setlang/', set_language, name='set_language'),
]

# Static and media files serving for development (will be handled by Nginx in production)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
