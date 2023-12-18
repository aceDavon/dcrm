from django.db import models


class Customer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    verified_at = models.DateTimeField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=15)

    def __str__(self) -> str:
        return (f"{self.first_name} {self.last_name}")
