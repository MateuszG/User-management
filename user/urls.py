from django.conf.urls import patterns, include, url
from django.contrib import admin
from user import views

urlpatterns = patterns('user',
    url(r'^$', views.IndexUsersView.as_view(), name='index'),
    url(r'^add/', views.AddUserView.as_view(), name='add'),
    url(r'^(?P<pk>\d+)/$', views.DetailUserView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit$', views.EditUserView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/delete$', views.DeleteUserView.as_view(),
        name='delete'),

)
