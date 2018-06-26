from django.db import models
from django.utils import timezone

class Quiz(models.Model):
    title       = models.CharField(max_length=150)
    text        = models.TextField()
    slug        = models.CharField(max_length=250, unique=True)
    created_at  = models.DateTimeField(default=timezone.now)
    pub_date    = models.DateTimeField(blank=True, null=True)
    author      = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizes'

    def publish(self):
        self.pub_date = timezone.now
        self.save()

    def __str__(self):
        return self.title


class Opcion(models.Model):
    text        = models.CharField(max_length=100)

    class Meta:
        verbose_name        = 'Opcion'
        verbose_name_plural = 'Opciones'

    def __str__(self):
        return self.text


class Pregunta(models.Model):
    title       = models.CharField(max_length=150)
    quiz        = models.ForeignKey('Quiz', on_delete=models.CASCADE)

    class Meta:
        verbose_name        = 'Pregunta'
        verbose_name_plural = 'Preguntas'

    def __str__(self):
        return self.title


class PreguntaOpcion(models.Model):
    pregunta    = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion      = models.ForeignKey(Opcion, on_delete=models.CASCADE)
    correct     = models.BooleanField(default=False)

    class Meta:
        verbose_name    = 'PreguntaOpcion'
        verbose_name_plural = 'PreguntasOpciones'
