from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Candidate, Batch, StartPage
from .forms import CandidateForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.db.models import Count


class CandidateList(ListView):
    model = Candidate
    template_name = 'GOLOSOVANIE/elections.html'
    context_object_name = 'candidates'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['batches'] = Batch.objects.all()
        context['batches'] = Batch.objects.annotate(cnt=Count('candidate'))
        return context

    def get_queryset(self):
        return Candidate.objects.all().select_related('batch', 'slogan')


class CandidateByBatch(CandidateList):
    template_name = 'GOLOSOVANIE/batch.html'

    def get_queryset(self):
        return Candidate.objects.filter(batch_id=self.kwargs['batch_id']).select_related('batch', 'slogan')
    #  select_related используется для оптимизации запросов. Он жадный, то есть заставляет запрос выполниться
    #  прямо сейчас, а не когда понадобятся данные. Хорош в использовании с ForeignKey


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

