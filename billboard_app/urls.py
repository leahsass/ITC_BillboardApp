from django.conf.urls import url
from . import views
from django.contrib.auth import views as authviews


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_post/$', views.new_post, name='new_post'),
    url(r'^login/$', authviews.login, name='login'),
    url(r'^logout/$', authviews.logout, {'next_page': '/'}, name='logout'),
    url(r'^register/$', views.register, name='register'),

]