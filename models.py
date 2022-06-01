from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=50, null=False)
    description = models.TextField()
    founder = models.CharField(max_length=50)
    def __str__(self):
        return self.company_name + "-----" + self.founder + "-----" + self.country

class City(models.Model):
    city_name = models.CharField(max_length=50)
    def __str__(self):
        return self.city_name

class Car(models.Model):
    name_model = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=30, decimal_places=15)
    description = models.TextField()
    created_by = models.DateField(auto_now=True)
    updated_by = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name_model + "---" + str(self.company) + "---" + str(self.city)
