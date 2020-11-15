from django.shortcuts import render,HttpResponse,redirect
from .models import *
import datetime


def index(request):
    subscribers = Subscriber.objects.all()
    fees = Fee.objects.all()
    debts = Debt.objects.all()

    monthly_fees = 0
    for fee in fees:
        monthly_fees += fee.price
    context = {
        'subscribers':subscribers,
        'monthly_fees':monthly_fees,
        'debts':debts,
    }
    return render(request,'index.html',context)




def details(request,id):
    subscriber = Subscriber.objects.get(id=id)
    payments = Payment.objects.filter(subscriber=subscriber)
    fees = Fee.objects.all()

    monthly_fees = 0
    total_payments = 0
    balance = 0
    debt = 0

    for fee in fees:
        monthly_fees += fee.price
    for payment in payments:
        total_payments += payment.amount

    x = subscriber.debt - total_payments

    context ={
        'subscriber':subscriber,
        'payments':payments,
        'total_payments':total_payments,
        'monthly_fees':monthly_fees,
        'x':x,

    }
    return render(request,'details.html',context)

def new_debt(request):
    fees = Fee.objects.all()
    subscribers = Subscriber.objects.filter(active=True)
    monthly_fees = 0
    for fee in fees:
        monthly_fees += fee.price
    for subscriber in subscribers:
        subscriber.debt += monthly_fees
        subscriber.save()
    debt = Debt(amount=monthly_fees)
    debt.save()
    return redirect('index')


