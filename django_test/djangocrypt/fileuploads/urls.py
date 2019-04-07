from django.conf.urls import url
from . import views

app_name = 'file_uploads'

urlpatterns = [
    url(r'^$', views.file_list, name="list"),
    url(r'^create/$', views.fileupload_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$',views.file_detail, name="detail"),
]

