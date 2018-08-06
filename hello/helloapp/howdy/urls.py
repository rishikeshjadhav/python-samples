from django.conf.urls import url
from howdy import views

urlpatterns = [
    url('^$', views.HomePageView.as_view()),
    url('^about/$', views.AboutPageView.as_view()),
]
