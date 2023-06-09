from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from forms import FileForm, ResultForm


def index(request):
    fileform = FileForm()
    result = ResultForm()
    return render(request, 'index.html')


