from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Candidate, Batch, StartPage
from .forms import CandidateForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


class CandidateList(ListView):
    model = Candidate
    template_name = 'GOLOSOVANIE/elections.html'
    context_object_name = 'candidates'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['batches'] = Batch.objects.all()
        return context

    def get_queryset(self):
        return Candidate.objects.filter()


class CandidateByBatch(ListView):
    model = Candidate
    template_name = 'GOLOSOVANIE/batch.html'
    context_object_name = 'candidates'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['batches'] = Batch.objects.all()
        return context

    def get_queryset(self):
        return Candidate.objects.filter(batch_id=self.kwargs['batch_id'])


class CandidateProfile(DetailView):
    model = Candidate
    template_name = 'GOLOSOVANIE/candidate.html'
    context_object_name = 'candidate'


class CreateCandidate(CreateView):
    form_class = CandidateForm
    template_name = 'GOLOSOVANIE/add_candidate.html'
    success_url = reverse_lazy('elections')


def index(request):
    template = loader.get_template('GOLOSOVANIE/index.html')

    home_page = StartPage.objects.first()

    context = {
        'home_page': home_page,
    }

    return HttpResponse(template.render(context, request))

