from django.db import models

class Arc(models.Model):
    name = models.CharField(max_length=60)
    background_color = models.CharField(max_length=10, default="#0000000")
    background_shadow = models.CharField(max_length=10, default="#0000000")

    background_image = models.ImageField()

    def __str__(self) -> str:
        return self.name

class Chapter(models.Model):
    number = models.IntegerField(unique=True)
    title = models.CharField(max_length=80, unique=True)
    year = models.IntegerField()
    arc = models.ForeignKey(Arc, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return 'chap. ' + str(self.number)
    
