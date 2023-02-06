from django.db import models

# Create your models here.

CarMake = [('Toyota', 'Toyota'), ('Honda', 'Honda'), ('Nissan', 'Nissan')]

#create account model
class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    make = models.CharField(max_length=25, choices=CarMake)
    carModel = models.CharField(max_length=25)

    #defines the model manager for the Account
    Accounts = models.Manager()

    def __str__(self):
        return self.first_name

#list of car services
CarServices = [('Oil Changee', 'Oil Change'), ('Break Service', 'Break Service'), ('Tire Service', 'Tire Service')]

#create Car details model

class Service(models.Model):
    date = models.DateField()
    service = models.CharField(max_length=50, choices=CarServices)

    #defines the model manager for the service
    services = models.Manager()


    def __str__(self):
        return self.service