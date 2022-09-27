from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse


class Post(models.Model):
    manufacture_date = models.CharField    (max_length=200, default =None)
    stencil_number = models.CharField    (max_length=200, default=None)
    revision = models.CharField    (max_length=200, default=None)
    ZLNumber = models.CharField    (max_length=200, default=None)
    material = models.CharField    (max_length=200, default=None)
    manufacture_number = models.CharField    (max_length=200, default=None)
    thickness = models.CharField    (max_length=200, default=None)
    author = models.CharField (max_length=200, default =None)

    def __str__(self):
        return self.manufacture_date, self.stencil_number, self.revision, self.ZLNumber, self.material, self.manufacture_number, self.thickness, self.author
        

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])

    def save(self, *args, **kwargs):
        self.extra_field = "extra field"
        print(self.manufacture_date, self.stencil_number, self.revision, self.ZLNumber, self.material, self.manufacture_number, self.thickness, self.author)
        super().save(*args, **kwargs)
    