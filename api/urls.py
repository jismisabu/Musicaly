from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.routers import DefaultRouter

from api import views



router = DefaultRouter()

router.register("album",views.AlbumViewSetView,basename="albums")

router.register("register",views.SignUpView,basename="register")



urlpatterns=[
    path("token/",ObtainAuthToken.as_view()),

    path("tracks/<int:pk>/",views.TrackMixinView.as_view()),

]+router.urls

