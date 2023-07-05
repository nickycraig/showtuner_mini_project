from django.db import models

# Create your models here.
class Composer(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    bio = models.CharField(max_length=1500)
    verified_artist = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]

class Show(models.Model):
    title = models.CharField(max_length=150)
    year = models.IntegerField(default=0)
    composer = models.ForeignKey(Composer, on_delete=models.CASCADE, related_name="shows")

    def __str__(self):
        return self.title
    
class Favorite(models.Model):
    title = models.CharField(max_length=150)
    shows = models.ManyToManyField(Show)

    def __str__(self):
        return self.title