from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from .models import Detail
from django.contrib import messages


def index(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        email=request.POST.get('email')
        allObjects=Detail.objects.all()
        val={'allObjects':allObjects}
        for i in allObjects:
            user, eid = str(i).split(", ")
            if user==fname:
                template = loader.get_template('polls/display.html')
                return HttpResponseBadRequest(template.render(),status=405)
            if email==eid:
                template = loader.get_template('polls/email.html')
                return HttpResponseBadRequest(template.render(),status=405)
    
        s=Detail(user_name=fname, email_id=email)
        s.save()
        messages.success(request, 'Form submission successful')
    return render(request,'polls/index.html')

def details(request):
    all_detail=Detail.object.all()
    context={all_detail:"all_detail"}
    return render(request,'polls/display.html', context)

def wrong_url(request):
    return render(request, 'polls/error.html')
