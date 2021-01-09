from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('_blog.urls', namespace='blog')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Customizing admin texts
admin.site.site_header = 'Personal Challenge'
admin.site.index_title = 'Site administrateur, Personal Challenge'
admin.site.site_title = 'Control Panel'