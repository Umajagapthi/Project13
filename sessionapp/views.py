from django.shortcuts import render
from django.http import HttpResponse
def input(request):
    return render(request,'base.html')
def add(request):
    x=int(request.POST['t1'])
    y=int(request.POST['t2'])
    z=x+y
    request.session['z']=z
    request.session.set_expiry(60)
    return HttpResponse('data submited successfully')
def display(request):
    if request.session.has_key('z'):
        z=request.session['z']
        return HttpResponse("the sum is:"+str(z))
    else:return render(request,'base.html')


# Create your views here.
