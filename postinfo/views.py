from __future__ import unicode_literals

from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .models import user_upload

def to_upload_info(request):
    return render(request, 'userinfo.html', context={})
def upload_info(request):
    if not request.user.is_authenticated:
        return redirect(reverse('sign_in'))
    redirect_url = request.GET.get('next')
    if redirect_url is None:
        redirect_url = '/'
    if request.method == "POST":
        name = request.POST.get('name')
        genre = request.POST.get('genre')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        email = request.POST.get('email')
        payment = request.POST.get('payment')
        user_upload.objects.create(musician_name=name, musician_genre=genre, musician_contactNumber= contact,
        						   musician_address=address, musician_email=email, musician_priceRate=payment,
        						   owner=request.user)
	return render(request, 'home.html', context={})