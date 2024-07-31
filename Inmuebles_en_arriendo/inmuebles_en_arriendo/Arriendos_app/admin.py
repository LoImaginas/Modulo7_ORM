from django.contrib import admin
from .models import Inmueble, Comuna, Region

# Register your models here.
admin.site.register(Inmueble)
admin.site.register(Comuna)
admin.site.register(Region)