from django.db import models

# Create your models here.
# make migrations - create changes and store in a file
# migrate - apply the pending changes created by make migrations
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date= models.DateField()

    def __str__(self):
        return self.name
