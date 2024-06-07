from django.db import models


class Brand(models.Model):
    description = models.CharField(max_length=50)
    active = models.BooleanField(default=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
