from django.shortcuts import render,redirect
from .models import NewData,valid
from .forms import DataForm,validform
from django.http import HttpRequest,HttpResponse
# Create your views here.

def home_view(request):
    if request.method=='POST':
        form=DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form=DataForm()
    
    return render(request,'home.html',{'form':form})


def home(request):
    if request.method=='POST':
        details=validform(request.POST)

        if details.is_valid():
            post=details.save(commit=False)
            post.save()
            return HttpResponse('data submitted successfully')
        else:
            return render(request,'validhome.html',{'form':details})
    else:
        form=validform(None)
        return render(request,'validhome.html',{'form':form})
        
