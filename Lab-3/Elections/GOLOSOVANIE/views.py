from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Candidate


def index(request):
    template = loader.get_template('GOLOSOVANIE/Index.html')

    context = {
        'Title': 'washtub',
    }

    return HttpResponse(template.render(context, request))


def elections(request):
    template = loader.get_template('GOLOSOVANIE/Elections.html')
    candidates = Candidate.objects.all()

    context = {
        'Title': 'ShitPool',
        'Candidates': candidates
    }
    return HttpResponse(template.render(context, request))
