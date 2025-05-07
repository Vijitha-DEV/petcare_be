from django.db import models

class District(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class DistrictSelection(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='selections')
    selected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.district.name} @ {self.selected_at.isoformat()}"

class PetHostel(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    contact = models.CharField(max_length=20)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="hostels")
    image = models.ImageField(upload_to='hostel_images/', null=True, blank=True)  
    
    def __str__(self):
        return self.name
    

class PetHospital(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    contact = models.CharField(max_length=20)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="hospitals")
    image = models.ImageField(upload_to='hospital_images/', null=True, blank=True)  
    
    def __str__(self):
        return self.name    
    
class PetSupplies(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    contact = models.CharField(max_length=20)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="supplies")
    image = models.ImageField(upload_to='supplies_images/', null=True, blank=True)  
    
    def __str__(self):
        return self.name        
    
# models.py

class PetCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    owner_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    pet_name = models.CharField(max_length=100)
    pet_age = models.IntegerField()
    pet_breed = models.CharField(max_length=100)
    category = models.ForeignKey(PetCategory, on_delete=models.CASCADE)
    appointment_time = models.CharField(max_length=20)
    appointment_date = models.DateField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Appointment for {self.pet_name} with {self.doctor.name}"
    
