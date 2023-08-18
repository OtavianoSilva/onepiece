from django.db import models

class Saga(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self) -> str:
        return self.name

class Arc(models.Model):
    name = models.CharField(max_length=60, unique=True)
    filler = models.BooleanField(default=False)
    saga = models.ForeignKey(Saga, on_delete=models.CASCADE, default=0)

    text_color = models.CharField(max_length=10, default="#000000")
    background_color = models.CharField(max_length=10, default="#000000")
    background_shadow = models.CharField(max_length=10, default="#000000")
    background_image = models.ImageField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class Episode(models.Model):
    number = models.IntegerField(unique=True)
    title = models.CharField(max_length=80, unique=True)
    year = models.IntegerField()
    arc = models.ForeignKey(Arc, on_delete=models.CASCADE)

    filler = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.number} - {self.title}"

class Chapter(models.Model):
    number = models.IntegerField(unique=True)
    title = models.CharField(max_length=80)
    year = models.IntegerField()
    arc = models.ForeignKey(Arc, on_delete=models.CASCADE)

    spoiler = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.number} - {self.title}"
    
