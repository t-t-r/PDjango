from django.db import models


class Turnaus(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Joukkue(models.Model):
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=300, null=True, blank=True)
    turnaus = models.ForeignKey(
        Turnaus, 
        on_delete=models.CASCADE, 
        null=True, blank=True,
        related_name = 'joukkueet', 
    )

    def __str__(self):
            return  f"{self.name}"


