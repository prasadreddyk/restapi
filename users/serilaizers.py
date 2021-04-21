from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import User,Employee

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only':True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields=['id','employeeid','name','phone',]
