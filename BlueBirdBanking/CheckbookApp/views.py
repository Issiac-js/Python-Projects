from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse #new import
from .forms import AccountForm, TransactionForm #new import
from .models import Account, Transaction

# Create your views here.

#This function will render the Home page when requested
def home(request):
    form = TransactionForm(data=request.POST or None) # retrieve Transaction form
    #check if request method is POST
    if request.method == 'POST':
        pk = request.POST['account']#if the form is submitted retrieve which account user wants to view
        return balance(request, pk) #call balance function to render that account's Balance Sheet
    content = {'form': form} # pass content to the template in a directory
    #adds content of form to page
    return render(request, 'checkbook/index.html', content)

#This function will render the Create New Acoount page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None) # Retrieve the Account forms
    #checks if request method is POST
    if request.method =='POST':
        if form.is_valid(): #Check to see if the submitted form is valid and if so, save the form
            form.save() #saves new account
            return redirect('index')#returns user back to homepage
    content = {'form': form} # saves content to the template as dictionary
    #adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)

#This function will render the Balence page when requested
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk) # retrieve the requested account using its primary key
    transactions = Transaction.Transactions.filter(account=pk) #retrieve all of that account's transactions
    current_total = account.initial_deposit #creates account total variable, starting with inital deposit value
    table_contents = {} #Create dictionary into which transaction information will be placed
    for t in transactions: #loop through transactions and determine which is a deposit or Withdrawal
        if t.type == 'Deposit':
            current_total += t.amount #if deposit add amount to balence
            table_contents.update({t: current_total}) # add transaction and total to the dictionary
        else:
            current_total -= t.amount #If withdrawal subtract amount from balance
            table_contents.update({t: current_total}) # add transaction and total to the dictionary
    #Pass account , account total balance, and transaction information to the template
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}

    return render(request, 'checkbook/BalanceSheet.html', content)

#This function will render the Transaction page when requested
def transaction(request):
    form = TransactionForm(data=request.POST or None) # Retrieve the Account forms
    #checks if request method is POST
    if request.method =='POST':
        if form.is_valid(): #Check to see if the submitted form is valid and if so, save the form
            pk = request.POST['account'] #retrieve which account the transaction was for
            form.save() #saves new account
            return balance(request, pk) # Renders Balance of the accounts Balance Sheet
    content = {'form': form} # saves content to the template as dictionary
    #adds content of form to page
    return render(request, 'checkbook/AddTransaction.html', content)
