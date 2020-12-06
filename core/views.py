from django.shortcuts import render,HttpResponse,redirect
from .models import *
import datetime


def index(request):
    subscribers = Subscriber.objects.all().order_by('date_joined').reverse()
    payments = Payment.objects.all()
    fees = Fee.objects.all()
    debts = Debt.objects.all().order_by('date').reverse()

    sub_payment=0
    for payment in payments:
        sub_payment += payment.amount

    sub_debt = 0
    for subscriber in subscribers:
        sub_debt += subscriber.debt

    monthly_fees = 0
    for subscriber in subscribers:
        fee = Fee.objects.get(level=subscriber.level)
        monthly_fees += fee.price

    balance = sub_payment - sub_debt
    if balance <0:
        color = 'negative'
    else:
        color = 'positive'

    context = {
        'subscribers':subscribers,
        'monthly_fees':monthly_fees,
        'debts':debts,
        'fees':fees,
        'sub_debt':sub_debt,
        'sub_payment':sub_payment,
        'balance':balance,
        'color':color
    }
    return render(request,'index.html',context)

def subscribers(request):
    subscribers = Subscriber.objects.all()

    context = {
        'subscribers':subscribers,
    }
    return render(request,'subscribers.html',context)


def details(request,id):
    subscriber = Subscriber.objects.get(id=id)
    payments = Payment.objects.filter(subscriber=subscriber)
    fees = Fee.objects.get(level=subscriber.level)

    total_payments = 0
    balance = 0
    debt = 0

    for payment in payments:
        total_payments += payment.amount

    x = subscriber.debt - total_payments

    context ={
        'subscriber':subscriber,
        'payments':payments,
        'total_payments':total_payments,
        'monthly_fees':fees.price,
        'x':x,

    }
    return render(request,'details.html',context)

def new_debt(request):
    subscribers = Subscriber.objects.filter(active=True)
    for subscriber in subscribers:
        fee = Fee.objects.get(level=subscriber.level)
        subscriber.debt += fee.price
        subscriber.save()


    fees = Fee.objects.all()
    monthly_fees =0
    for fee in fees:
        monthly_fees += fee.price 

    debt = Debt(amount=monthly_fees)
    debt.save()
    return redirect('index')


