from django.db import models

# Create your models here.


#CREATES THE ACCOUNT model

class Account(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    initial_deposit = models.DecimalField(max_digits=15, decimal_places=2)

    #defines the model manager for accounts
    Accounts = models.Manager()

    #allows references to a specific account be returned as the owner's name not the primary key
    def __str__(self):
        return self.first_name + ' ' + self.last_name


TransactionTypes = [('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')]


#Creates the Transaction model
class Transaction(models.Model):
    data = models.DateField()
    type = models.CharField(max_length=10, choices=TransactionTypes)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)



    #Defines the model manager for Transactions
    Transactions = models.Manager()
