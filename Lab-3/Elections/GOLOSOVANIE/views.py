from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Candidate, Batch, StartPage
from .forms import CandidateForm


def index(request):
    template = loader.get_template('GOLOSOVANIE/index.html')

    home_page = StartPage.objects.get(id=4)

    context = {
        'home_page': home_page,
    }

    return HttpResponse(template.render(context, request))


def elections(request):
    template = loader.get_template('GOLOSOVANIE/elections.html')

    candidates = Candidate.objects.all()
    batches = Batch.objects.all()

    context = {
        'title': 'Голосуй.',
        'candidates': candidates,
        'batches': batches,
    }
    return HttpResponse(template.render(context, request))


def get_batch(request, batch_id):
    template = loader.get_template('GOLOSOVANIE/batch.html')

    try:
        candidates = Candidate.objects.filter(batch_id=batch_id)
    except Candidate.DoesNotExist:
        raise Http404("Данный кандидат уже сидит или расстрелян.")

    batches = Batch.objects.all()

    context = {
        'title': 'Голосуй.',
        'candidates': candidates,
        'batches': batches,
    }
    return HttpResponse(template.render(context, request))


def candidate(request, candidate_id):  # страница не закончена. На ней будет вся инфа по кандидату
    template = loader.get_template('GOLOSOVANIE/candidate.html')

    try:
        candidate = Candidate.objects.get(pk=candidate_id)
    except Candidate.DoesNotExist:
        raise Http404("Данный кандидат уже сидит или расстрелян.")

    context = {
        'candidate': candidate,
    }

    return HttpResponse(template.render(context, request))


def add_candidate(request):
    template = loader.get_template('GOLOSOVANIE/add_candidate.html')

    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
             Candidate.objects.create(**form.cleaned_data)
             return redirect('elections')
        print("HI")
    else:
        form = CandidateForm()

    context = {
        'form': form,
    }

    return HttpResponse(template.render(context, request))


