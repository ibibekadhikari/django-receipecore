from django.db import models

# Create your models here.
class Receipe(models.Model):
#Degingin models, which literally defines table and their field in Django.
#The variballe name should be same in the html field, name= tag.
    receipe_name = models.CharField(max_length=100)
    receipe_description = models.TextField()
    #The python came with error, Module PILLOW must be installed to
    #use IMAGEFIELD.
    """Here in Imagefield, upload_to represents where to upload the photos
       in this case it will upload all the images to receipeimages directory
       if there is no directory then it will upload by creating directory itself."""
    receipe_image = models.ImageField(upload_to="receipeimages")
    """By default, it represents as a object and shows as a object
       in the admin pages inside table so it is defined, just like
       toString() in Java """
    def __str__(self):
        return self.receipe_name