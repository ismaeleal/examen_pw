from django.contrib import admin

# Register your models here.
from .models import Mesa, Circuscricion, Partido, Resultado


admin.site.register(Mesa)
admin.site.register(Circuscricion)
admin.site.register(Partido)
admin.site.register(Resultado)
