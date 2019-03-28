from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewsForm


def index(request):
    context={}
    return render(request, 'recommendersys/index.html', context)

def upload(request):
    if request.method == "POST":
        reviews_form = ReviewsForm(request.POST, request.FILES)
        if reviews_form.is_valid():
            reviews_form.save()
            return HttpResponseRedirect('recommendersys/index.html')
    else:
        reviews_form = ReviewsForm()
    context={'reviews_form':reviews_form}
    return render(request, 'recommendersys/upload.html', context)
