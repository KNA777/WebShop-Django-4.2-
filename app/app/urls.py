from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls

from .settings import DEBUG, MEDIA_URL, MEDIA_ROOT

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('goods.urls', namespace='goods')),
    path('user/', include('users.urls', namespace='users')),

]

if DEBUG:
    urlpatterns += debug_toolbar_urls()
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
