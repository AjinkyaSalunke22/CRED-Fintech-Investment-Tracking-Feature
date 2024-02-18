from django.shortcuts import render

# Create your views here.

def add_stock(request):

    if request.method == "POST":
        print(request.POST, "==========\n\n")
    else:
        return render(request, 'add_stock.html')