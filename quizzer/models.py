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
