from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from fileuploads import views as fileuploads_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^fileuploads/',include('fileuploads.urls')),
    url(r'^about/$', views.about),
    url(r'^$', fileuploads_views.file_list,name="home"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
