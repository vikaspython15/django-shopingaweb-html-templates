from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def electronic(request):
    return render(request, 'electronic.html')
def fashion(request):
    return render(request, 'fashion.html')
def jewellery(request):
    return render(request, 'jewellery.html')