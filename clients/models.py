from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(blank=False, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=9)
    mobile_phone = models.CharField(max_length=14)
    active = models.BooleanField()

    def __str__(self):
        return f"{self.name} ({self.id}) [{self.active}] :: CPF {self.active} RG {self.rg} :: contact: {self.email} {self.mobile_phone}"
