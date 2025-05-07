from rest_framework import serializers
from django.contrib.auth.models import User
from .models import District, DistrictSelection,PetHostel,PetHospital,PetSupplies,PetCategory, Doctor, Appointment

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name']

class DistrictSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistrictSelection
        fields = ['id', 'district', 'selected_at']
        read_only_fields = ['id','selected_at']

class PetHostelSerializer(serializers.ModelSerializer):
    district = DistrictSerializer(read_only=True)
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = PetHostel
        fields = ['id', 'name', 'address', 'contact', 'district', 'image']
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None
    
class PetHospitalSerializer(serializers.ModelSerializer):
    district = DistrictSerializer(read_only=True)
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = PetHospital
        fields = ['id', 'name', 'address', 'contact', 'district', 'image']
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None 
       
class PetSuppliesSerializer(serializers.ModelSerializer):
    district = DistrictSerializer(read_only=True)
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = PetSupplies
        fields = ['id', 'name', 'address', 'contact', 'district', 'image']
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None    
    
class PetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PetCategory
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'    
