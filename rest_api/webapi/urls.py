from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from webapi import views

urlpatterns = [
	url(r'^players/$', views.PlayerList.as_view()),
	url(r'^players/(?P<pk>[0-9]+)/$', views.PlayerDetail.as_view()),
	url(r'^teams/$', views.TeamList.as_view()),
	url(r'^teams/(?P<pk>[0-9]+)/$', views.TeamDetail.as_view()),
	url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]