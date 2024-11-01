from rest_framework import serializers
from .models import onGoingProjects,resourceRequest,LoginPage , makeObjection

class onGoingPrjSerializer(serializers.ModelSerializer):
    class Meta:
        model = onGoingProjects
        fields = '__all__'
        #['id', 'prjName', 'prjDescription', 'prjAgency', 'prjAgencyLicense', 'prjFinance']
    
class resourceRequestSerilizer(serializers.ModelSerializer):
    class Meta:
        model = resourceRequest
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    class Meta:
        model = LoginPage
        fields = '__all__'
class makeObjectionSerilizer(serializers.ModelSerializer):
    class Meta:
        model = makeObjection
        fields = '__all__'