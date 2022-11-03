from rest_framework.serializers import(           
    ModelSerializer
)

from testapp.models import (Contractor, ContractorApplication)
from django.contrib.auth.models import User

class UserPublicSerializer(ModelSerializer):
    class Meta:
        model = User 
        fields = [
            'id',
            'username',
        ]

        read_only_fields = ['username']


class ContractorSerializer(ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    class Meta:
        model = Contractor
        fields = [
            "id",
            "user",
            "phone",
            "nationality",
            "comment",
            "pay_rate",
        ]


class ContractorApplicationSerializer(ModelSerializer):
    
    class Meta:
        model = ContractorApplication
        fields = [
            "id",
            "contractor",
            "job_name", 
            "start_date",
            "end_date",
        ]
