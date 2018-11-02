


from django.contrib import admin
from .models import Location,Image,Category

# Register your models here.

class ImagesAdmin(admin.ModelAdmin):
    filter_horizontal =('description',)


admin.site.register(Location)
admin.site.register(Image)
admin.site.register(Category)