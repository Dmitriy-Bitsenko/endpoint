from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect

from forms import FileForm, ResultForm

import csv

fss = FileSystemStorage(location='endpoint/storage')


def forms(request):
    file = FileForm()
    result = ResultForm()
    return render(request, 'index.html')


def calculation(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            calculation_file(request.FILES['file'])
            return HttpResponseRedirect('')
    else:
        form = FileForm()
    return render(request, 'index.html', {'form': form})


def calculation_file(request):
    with open ('fss') as f:
        print(f)




