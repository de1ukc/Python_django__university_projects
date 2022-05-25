from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Candidate, Batch, StartPage, Slogan
from .forms import CandidateForm, UserRegisterForm, UserLoginForm, SloganForm
from django.views.generic import ListView, DetailView, CreateView, View
from django.urls import reverse_lazy
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout


class CandidateList(ListView):
    model = Candidate
    template_name = 'GOLOSOVANIE/elections.html'
    context_object_name = 'candidates'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['batches'] = Batch.objects.all()
        context['batches'] = Batch.objects.annotate(cnt=Count('candidate'))
        return context

    def get_queryset(self):
        return Candidate.objects.all().select_related('batch', 'slogan')


class MyCandidates(View):
    template_name = 'GOLOSOVANIE/my_candidates.html'

    def get(self, request):
        candidates = Candidate.objects.filter(creator__username=request.user.username)\
            .select_related('batch', 'slogan')

        context = {
            'candidates': candidates,
        }

        return render(request, self.template_name, context)


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


class CreateCandidate(LoginRequiredMixin, CreateView):
    form_class = CandidateForm
    template_name = 'GOLOSOVANIE/add_candidate.html'
    success_url = reverse_lazy('elections')
    login_url = '/login/'  # сделать страницу регистрирования
    context_object_name = 'candidate'


class AddSlogan(View):
    template_name = 'GOLOSOVANIE/slog.html'
    next_template = 'GOLOSOVANIE/add_candidate'

    def get(self, request):
        context = {
            'form': SloganForm(),
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = SloganForm(request.POST)
        form.save()
        return redirect('add_candidate')




class Index(View):
    template_name = 'GOLOSOVANIE/index.html'

    def get(self, request):
        home_page = StartPage.objects.first()

        context = {
            'home_page': home_page,
        }

        return render(request, self.template_name, context)


class UserRegistry(View):
    template_name = 'GOLOSOVANIE/register.html'

    def get(self, request):
        context = {
            'form': UserRegisterForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            messages.success(request, 'Произошла успешная регистрация. Будь аккуратен на выборах!')
            login(request,user)
            return redirect('elections')
        else:
            messages.error(request, 'Ошибка регистрации')

        context = {
            'form': form
        }

        return render(request, self.template_name, context)


class UserLogin(View):
    template_name = 'GOLOSOVANIE/login.html'

    def get(self, request):
        context = {
            'form': UserLoginForm(),
            'home_page': StartPage.objects.first()
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            #messages.success(request, 'Произошла успешная регистрация. Будь аккуратен на выборах!')
            login(request, user)
            return redirect('elections')
        else:
            messages.error(request, 'Ошибка регистрации')

        context = {
            'form': form
        }

        return render(request, self.template_name, context)


class UserLogout(View):
    def get(self, request):
        logout(request)
        return redirect('index')