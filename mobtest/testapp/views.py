from django.contrib.auth.models import User
from .serializers import ContractorSerializer, ContractorApplicationSerializer
from rest_framework import viewsets
from .models import Contractor, ContractorApplication


# from rest_framework.decorators import api_view


# It is up to you whether you want to use class based or functional view(s)


class ContractorApplicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contractor to be viewed or edited.
    """

    # TODO left for debugging - change this to Contractor queryset
    queryset = ContractorApplication.objects.all().order_by("-start_date")
    serializer_class = ContractorApplicationSerializer


class ContractorViewSet(viewsets.ModelViewSet):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer


# @api_view(["GET"])
# def get_contractor_applications(request):
#     pass
