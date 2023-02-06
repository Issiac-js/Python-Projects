from django.shortcuts import render, get_object_or_404
from .forms import AccountForm, ServiceForm
from .models import Service, Account


# Create your views here.

# This function will render the Home page when requested.
def carMaintenanceTrackerHome(request):
    #returns a render
    return render(request, 'CarMaintenanceTracker/CarMaintenanceTracker_home.html')

def viewHistroy(request):

    account_list = Account.Accounts.all()
    service_list = Service.services.all()
    content = {'account_list': account_list, 'service_list': service_list}

    return render(request, 'CarMaintenanceTracker/CarMaintenanceTracker_history.html', content)

def addEvent(request):
    form = ServiceForm(data=request.POST or None)

    if request.method == 'POST':
        #form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'CarMaintenanceTracker/CarMaintenanceTracker_create.html', context)

def account(request):
    form = AccountForm(data=request.POST or None)
    if request.method == 'POST':
        #form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'CarMaintenanceTracker/CarMaintenanceTracker_account.html', context)

def details(request, pk):
    info = get_object_or_404(Account, pk=pk)
    content = {'info': info}
    return render(request, 'CarMaintenanceTracker/CarMaintenanceTracker_details.html', content)
