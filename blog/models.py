from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    manufacture_date = models.CharField    (max_length=200)
    stencil_number = models.CharField    (max_length=200)
    revision = models.CharField    (max_length=200)
    ZLNumber = models.CharField    (max_length=200)
    material = models.CharField    (max_length=200)
    manufacture_number = models.CharField    (max_length=200)
    thickness = models.CharField    (max_length=200)

    #['Date of Manufacture', 'Stencil Number', 'Revision', 'ZL Number', 'Material', 'Manufacturer Number', 'Thickness', 'author',]#

    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.manufacture_date, self.stencil_number, self.revision, self.ZLNumber, self.material, self.manufacture_number, self.thickness, self.author
        

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])

    def save(self, *args, **kwargs):
        self.extra_field = "extra field"
        # print(self.body)
        # print(self.title)
        # print(self.author)
        super().save(*args, **kwargs)
    