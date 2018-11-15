from django.urls import path

from .views import AboutPageView, HomePageView, MorePageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('more/', MorePageView.as_view(), name='more'),
]
