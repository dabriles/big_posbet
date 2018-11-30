from django.contrib import admin
from .models import equipo
from .models import goles
from .models import equipo_ciudad


# Register your models here.

admin.site.register(equipo)
admin.site.register(goles)
admin.site.register(equipo_ciudad)


