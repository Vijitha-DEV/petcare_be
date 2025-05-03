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
    


