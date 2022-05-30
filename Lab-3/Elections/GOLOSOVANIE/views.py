from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Candidate, Batch, StartPage, Slogan, MyUser
from .forms import CandidateForm, UserRegisterForm, UserLoginForm, SloganForm, CreateBatchForm
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.db.models import Count, F
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import login, logout
import logging
from .services import MyThread

logger = logging.getLogger("main_logger")
logger.setLevel(logging.DEBUG)


class CandidateListView(ListView):
    model = Candidate
    template_name = 'GOLOSOVANIE/elections.html'
    context_object_name = 'candidates'
    paginate_by = 10

    logger.info("Engage CandidateList")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['batches'] = Batch.objects.all()
        context['batches'] = Batch.objects.annotate(cnt=Count('candidate'))
        return context

    def get_queryset(self):
        return Candidate.objects.all().select_related('batch', 'slogan')


class MyCandidatesView(View):
    template_name = 'GOLOSOVANIE/my_candidates.html'

    logger.info("Engage MyCandidates")

    def get(self, request):
        candidates = Candidate.objects.filter(creator__username=request.user.username)\
            .select_related('batch', 'slogan')

        context = {
            'candidates': candidates,
        }

        return render(request, self.template_name, context)


class CandidateByBatchView(CandidateListView):
    template_name = 'GOLOSOVANIE/batch.html'

    logger.info("Engage CandidateByBatch")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['batch'] = Batch.objects.get(
            id=self.kwargs['batch_id']
        )
        return context

    def get_queryset(self):
        return Candidate.objects.filter(batch_id=self.kwargs['batch_id']).select_related('batch', 'slogan')
    #  select_related используется для оптимизации запросов. Он жадный, то есть заставляет запрос выполниться
    #  прямо сейчас, а не когда понадобятся данные. Хорош в использовании с ForeignKey


class CandidateProfileView(View):
    template_name = 'GOLOSOVANIE/candidate.html'

    logger.info("Engage CandidateProfile")

    def get(self, request, pk):
        candidate = Candidate.objects.get(pk=pk)
        flag_user = False

        users = MyUser.objects.filter(candidates__in=(candidate,))

        for usr in users:
            if request.user.username == usr.username:
                flag_user = True

        context = {
            'candidate_prof': candidate,
            'flag_user': flag_user,
        }

        return render(request, self.template_name, context)

    def post(self, request, pk):
        cand = Candidate.objects.get(pk=pk)
        cand.support_count = F('support_count') + 1
        usr = MyUser.objects.get(username=request.user.username)

        try:
            users = MyUser.objects.filter(candidates__in=(cand,))
            threads = []

            for user in users:
                thread = MyThread(user.email, 'Your candidate', '{} ({}) has support your candidate'
                                  .format(usr.username, usr.email))
                threads.append(thread)
                thread.start()
        except:
            print('Something went wrong... with email')

        cand.myuser_set.add(usr)
        cand.save()
        return HttpResponseRedirect(reverse('candidate', args=(pk,)))


class UpdateCandidateView(UpdateView):
    model = Candidate
    fields = ['first_name', 'last_name', 'middle_name', 'date_of_birth', 'region', 'description', 'preview']
    template_name = 'GOLOSOVANIE/update_candidate.html'
    success_url = reverse_lazy('elections')
    logger.info("Engage UpdateCandidate")


class CreateCandidateView(LoginRequiredMixin, CreateView):
    form_class = CandidateForm
    template_name = 'GOLOSOVANIE/add_candidate.html'
    success_url = reverse_lazy('elections')
    login_url = '/login/'  # сделать страницу регистрирования
    context_object_name = 'candidate'
    logger.info("Create Candidate")


class AddBatchView(CreateView):
    form_class = CreateBatchForm
    template_name = 'GOLOSOVANIE/add_batch.html'
    success_url = reverse_lazy('elections')
    context_object_name = 'batch'
    logger.info("Create Batch")


class AddSloganView(View):
    template_name = 'GOLOSOVANIE/slog.html'
    next_template = 'GOLOSOVANIE/add_candidate'
    logger.info("Engage AddSlogan")

    def get(self, request):
        context = {
            'form': SloganForm(),
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = SloganForm(request.POST)
        form.save()
        return redirect('add_candidate')


class IndexView(View):
    template_name = 'GOLOSOVANIE/index.html'
    logger.info("Engage Index")

    def get(self, request):
        home_page = StartPage.objects.first()

        context = {
            'home_page': home_page,
        }

        return render(request, self.template_name, context)


class UserRegistryView(View):
    template_name = 'GOLOSOVANIE/register.html'
    logger.info("Engage UserRegistry")

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


class UserLoginView(View):
    template_name = 'GOLOSOVANIE/login.html'
    logger.info("Engage UserLogin")

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


class UserLogoutView(View):
    logger.info("Engage UserLogout")

    def get(self, request):
        logout(request)
        return redirect('index')


class DeleteCandidateView(DeleteView):
    model = Candidate
    success_url = reverse_lazy('elections')
    template_name = 'GOLOSOVANIE/delete_candidate.html'
    logger.info("Engage DeleteCandidate")



