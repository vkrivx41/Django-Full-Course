from django.db import models


class Dog(models.Model):
    name = models.CharField(unique=True, max_length=100)
    image = models.ImageField(upload_to="dogs/")

    def __str__(self) -> str:
        return f"{self.name}"
    
    def delete(self) -> None:
        """
        Overridding the super delete method to delete the image after the dog has been deleted
        """
        self.image.delete()
        super().delete()