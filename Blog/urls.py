from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.index),#index of blog page,routing to the single blog page.
	url(r'^articles/(?P<pageID>[0-9]+)$',views.singlePage),
]