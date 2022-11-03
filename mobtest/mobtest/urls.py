from django.urls import include, path
from mobtest.views import GroupViewSet, UserViewSet
from rest_framework import routers
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"groups", GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/testapp/", include("testapp.urls")),
]
