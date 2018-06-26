from django.contrib import admin

from .models import Quiz, Pregunta, Opcion, PreguntaOpcion

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Pregunta)
admin.site.register(Opcion)
admin.site.register(PreguntaOpcion)
