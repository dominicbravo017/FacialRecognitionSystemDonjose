from django.db import models

class Person(models.Model):
    image = models.BinaryField(null=True, blank=True)  # Allow null/empty image
    name = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name or "Unnamed Person"
