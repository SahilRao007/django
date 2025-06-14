from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("you are in app1 now")

from .models import Data
from .forms import Dataform

def create_view(request):
    context={}

    form=Dataform(request.POST or None)
    if form.is_valid():
        form.save()

    context['form']=form
    return render(request,'create_view.html',context)


def list_view(request):
    context={}
    context['dataset']=Data.objects.all()
    return render(request,'list_view.html',context)

def detail_view(request,id):
    context={}
    context['dataset']=Data.objects.get(id=id)
    return render(request,'detail_view.html',context)

from django.shortcuts import ( get_object_or_404,HttpResponseRedirect)
def update_view(request,id):
    context={}
    obj=get_object_or_404(Data,id=id)
    form=Dataform(request.POST or None,instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/app1/')
    
    context['form']=form
    return render(request,'update_view.html',context)


def delete_view(request,id):
    context={}
    obj=get_object_or_404(Data,id=id)
    form=Dataform(request.POST or None, instance=obj)
    
    if request.method=="POST":
        obj.delete()
        return HttpResponseRedirect("/app1/")
    
    return render(request,"delete_view.html",{'obj':obj})


