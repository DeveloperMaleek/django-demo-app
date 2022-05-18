from django.conf.urls import include
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


urlpatterns = [
    path('api/users/register/', SignUpAuth.as_view()),
    path('api/', include(router.urls)),

]
