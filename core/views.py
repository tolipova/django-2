from django.shortcuts import render
from .models import Malumot
# Create your views here.
def home(request):
    post = Malumot.objects.all()
    context = {
        'post':post
    }
    return render(request,'index.html',context)