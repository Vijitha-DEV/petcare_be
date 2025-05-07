from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


from .views import district_list, select_district

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('districts/',district_list,    name='district_list'),
    path('select-district/', select_district,  name='select_district'),
    path('hostels/<int:district_id>/', views.hostels_by_district),
    path('hospitals/<int:district_id>/', views.hospitals_by_district),
    path('supplies/<int:district_id>/', views.supplies_by_district),

    path('categories/', views.PetCategoryListView.as_view(), name='categories'),
    path('doctors/', views.DoctorListView.as_view(), name='doctors'),
    path('appointments/', views.AppointmentCreateView.as_view(), name='appointments'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


