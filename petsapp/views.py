from django.shortcuts import render
from.models import Pet

# Create your views here.

def pets_list(request):
    pets_data = Pet.objects.all()
    data = {'pets_d':pets_data}
    return render(request,'petsapp/list.html',data)
