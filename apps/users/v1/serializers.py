from rest_framework import serializers
from apps.users.v1.models import User, Driver, Manager

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    license_number = serializers.CharField(required=False)
    employee_id = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password',
            'role',
            'license_number',
            'employee_id',
        ]

    def validate(self, data):
        role = data.get("role")

        if role == "Driver" and not data.get("license_number"):
            raise serializers.ValidationError({
                "license_number": "License number is required for drivers."
            })

        if role == "Manager" and not data.get("employee_id"):
            raise serializers.ValidationError({
                "employee_id": "Employee ID is required for managers."
            })

        return data

    def create(self, validated_data):
        license_number = validated_data.pop("license_number", None)
        employee_id = validated_data.pop("employee_id", None)
        role = validated_data.get("role")

        # Create user including username
        user = User.objects.create_user(
            email=validated_data["email"],
            username=validated_data["username"],
            password=validated_data["password"],
            role=role
        )

        if role == "driver":
            Driver.objects.create(user=user, license_number=license_number)
        elif role == "manager":
            Manager.objects.create(user=user, employee_id=employee_id)

        return user
  
class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'
