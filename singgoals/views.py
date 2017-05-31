from django.shortcuts import render
from django.contrib.auth.models import User
from postinfo.models import user_upload

def home(request):
    context = {
        'user_info': user_upload.objects.all().order_by('id')
    }
    return render(request, 'home.html', context=context)