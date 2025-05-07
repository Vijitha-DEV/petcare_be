from django.contrib import admin
from .models import District, DistrictSelection,PetHostel,PetHospital,PetSupplies,PetCategory,Doctor,Appointment

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(DistrictSelection)
class DistrictSelectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'district', 'selected_at')
    readonly_fields = ('selected_at',)

admin.site.register(PetHostel)
admin.site.register(PetHospital)
admin.site.register(PetSupplies)
admin.site.register(PetCategory)
admin.site.register(Doctor)
admin.site.register(Appointment)


