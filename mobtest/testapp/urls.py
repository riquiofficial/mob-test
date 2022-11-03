# from django.urls import path
from rest_framework import routers
from django.urls import include, path
from testapp.views import ContractorApplicationViewSet, ContractorViewSet

router = routers.DefaultRouter()
router.register(r"contractor-applications", ContractorApplicationViewSet)
router.register(r"contract", ContractorViewSet)


urlpatterns = [
    path("", include(router.urls)),
    # if functional view(s) desired
    # path("contractor-applications/", contractor_detail)
]
