from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^tags/(?P<tag>[А-Я]{1}[а-я]+)/$', views.texts_tag, name='texts_tag'),
    url(r'^clusters/(?P<cluster_id>[1-9]+)/$', views.texts_cluster, name='texts_cluster')
]