from django.shortcuts import render, redirect
from .forms import TransactionForm, DateForm
from .models import Transaction,Date
import datetime



def home(request):
    title = 'Welcome to Hazi traders'
    add_transaction = 'Add Transaction'
    show_transaction = 'Show Transaction'

    context ={
        "title":title,
        "add_transaction":add_transaction,
        "show_transaction":show_transaction,
    }
    return render(request,'home.html',context)


def transaction(request):
    form = TransactionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/transaction')

    queryset = Transaction.objects.all()
    qs=queryset.filter(Date=datetime.date.today())

    total_balance=0;
    for item in qs:
        item.Sold =item.Sale_able-item.Bounce
        item.Balance=item.Price*item.Sold
        total_balance=total_balance+item.Balance

    context ={
        "form":form,
        "queryset":qs,
        "total_balance":total_balance
    }
    return render(request,'transaction.html',context)

def show_transaction(request):
    date_on = request.GET.get('date_on')
    qs = Transaction.objects.all()
    queryset=qs.filter(Date=date_on)
    qss = Date.objects.all()
    queryset1=qss.filter(date=date_on)
    context ={
      "queryset":queryset,
      "Date":date_on,
    "queryset1": queryset1

    }
    return render(request,'show.html',context)

def root(request):
    form = DateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/transaction')

    context ={
        "form":form
    }
    return render(request,'root.html',context)