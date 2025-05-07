from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from .models import District, DistrictSelection, PetHostel,PetHospital,PetSupplies,PetCategory, Doctor, Appointment
from .serializers import DistrictSerializer , PetCategorySerializer, DoctorSerializer, AppointmentSerializer ,DistrictSelectionSerializer,PetHostelSerializer,PetSuppliesSerializer,PetHospitalSerializer
from rest_framework import generics


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class HomeView(APIView):
    def get(self, request):
        return Response({'message': 'Welcome to the Home Page!'})

@api_view(['GET'])
def district_list(request):
    qs = District.objects.all().order_by('name')
    serializer = DistrictSerializer(qs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def select_district(request):
    serializer = DistrictSelectionSerializer(data=request.data)
    if serializer.is_valid():
        selection = serializer.save()
        return Response(
            {'message': f'You selected: {selection.district.name}'},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def hostels_by_district(request, district_id):
    try:
        hostels = PetHostel.objects.filter(district_id=district_id)
        serializer = PetHostelSerializer(hostels, many=True, context={'request': request})
        return Response(serializer.data)
    except:
        return Response({'error': 'Error retrieving hostels'}, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def hospitals_by_district(request, district_id):
    try:
        hospitals = PetHospital.objects.filter(district_id=district_id)
        serializer = PetHospitalSerializer(hospitals, many=True, context={'request': request})
        return Response(serializer.data)
    except:
        return Response({'error': 'Error retrieving hospitals'}, status=status.HTTP_400_BAD_REQUEST)    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def supplies_by_district(request, district_id):
    try:
        supplies = PetSupplies.objects.filter(district_id=district_id)
        serializer = PetSuppliesSerializer(supplies, many=True, context={'request': request})
        return Response(serializer.data)
    except:
        return Response({'error': 'Error retrieving supplies'}, status=status.HTTP_400_BAD_REQUEST)    


class PetCategoryListView(generics.ListAPIView):
    queryset = PetCategory.objects.all()
    serializer_class = PetCategorySerializer

class DoctorListView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class AppointmentCreateView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer    
