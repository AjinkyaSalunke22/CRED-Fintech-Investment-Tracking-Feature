# Author: Ajinkya Salunke 
# Date: 19 Feb 2024


from random import randint
from django.shortcuts import redirect, render
from cred_app.models import Stocks

# Create your views here.

def add_stock(request):

    if request.method == "POST":
        # print(request.POST, "==========\n\n")

        stock_name = request.POST.get('stock_name')
        stock_price = request.POST.get('stock_price')

        qs = Stocks.objects.create(stock_name=stock_name, stock_price=stock_price)

        # print(qs.id, "=================== \n\n")


        if qs:
            return redirect('/retrive')


    else:
        return render(request, 'add_stock.html')
    

def retrive(request):
    qs = Stocks.objects.all()

    market_price = randint(100, 1000)

    for stock in qs:
        stock.difference = market_price - stock.stock_price

    context = {
        'stock_data': qs,
        'market_price': market_price
    }

    return render(request, 'retrive.html', context)



def delete_stock(request, id):
    # print(id, '================')

    qs = Stocks.objects.filter(id=id).delete()

    if qs:
        return redirect('/retrive')