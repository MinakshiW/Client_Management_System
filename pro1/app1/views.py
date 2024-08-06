from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm

# Create your views here.
def homeview(request):
    return render(request, 'app1/home.html', {})

def formview(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/a1/sv/')
    return render(request, 'app1/form.html', {'form': form})

def showview(request):
    obj = Client.objects.all()
    return render(request,'app1/show.html', {'obj': obj})

def updateview(request, pk):
    obj = Client.objects.get(id=pk)
    form = ClientForm(instance=obj)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/a1/sv/')
    return render(request, 'app1/form.html', {'form': form})

def deleteview(request, x):
    obj = Client.objects.get(id=x)
    if request.method == 'POST':
        obj.delete()
        return redirect('/a1/sv/')
    return render(request, 'app1/success.html', {'obj': obj})

def searchview(request):
    if request.method == 'POST':
        n = request.POST.get('search')
        print(n)
        obj = Client.objects.filter(name__contains=n)
    return render(request,'app1/show.html', {'obj': obj})

def filterview(request):
    q = request.GET.get('q')
    obj = Client.objects.filter(status=q)
    return render(request, 'app1/show.html', {'obj': obj})