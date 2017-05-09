from django.shortcuts import render,redirect
from django.http import HttpRequest
from TestApp.forms import (CandidateForm,TeacherForm,
                            AptitudeQuestionForm,TestScheduleForm,
                            CandidateScoresForm)

from TestApp.models import AptitudeQuestion,Candidate,TestSchedule,CandidateScores
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from functools import wraps


########################################################
###############Custom Decorators########################
########################################################

#Decorator for authentcating Candidates
#Todo : Redirect to new page on false login
def candidate_login(view_func):
    def _decorator(request, *args, **kwargs):
        if(request.user.groups.filter(name__in=['Candidate']).exists()):
            response = view_func(request, *args, **kwargs)
            return response
        else:
            return redirect(reverse('invalid_login'))
    return wraps(view_func)(_decorator)


#Decorator for authentcating admin
#Todo : Redirect to new page on false login
def admin_login(view_func):
    def _decorator(request, *args, **kwargs):
        if(request.user.groups.filter(name__in=['Candidate']).exists()):
            return redirect(reverse('invalid_login'))
        else:
            response = view_func(request, *args, **kwargs)
            return response
    return wraps(view_func)(_decorator)


"""Index check
            Check which group the login belongs to
            and redirect accordingly"""
def Check_privledges(request):
    if(request.user.is_authenticated()):
        if(request.user.groups.filter(name__in=['Candidate']).exists()):
            return render(request,"candidate_index.html")
        else:
            return render(request,"admin_index.html")
    else:
        return redirect(reverse('home'))


########################################################
################User Model Views########################
########################################################
@admin_login
def CreateUserView(request):
    if request.method == "POST":
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('candidate_list'))
    else:
        form = CandidateForm()
    return render(request,'NewUser.html',{'form':form})


class CandidateListView(LoginRequiredMixin,ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'TestApp/index.html'
    template_name='candidate_list.html'
    model = Candidate
    form = CandidateForm


class CandidateDetailView(LoginRequiredMixin,DetailView):
    login_url ='/accounts/login/'
    redirect_field_name = 'TestApp/index.html'
    template_name = 'candidate_detail.html'
    model = Candidate


########################################################
############Question Model Views########################
########################################################

class QuestionDeleteView(LoginRequiredMixin,DeleteView):
    model = AptitudeQuestion
    success_url = reverse_lazy('question_list')
    template_name = 'question_confirm_delete.html'


class QuestionUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'TestApp/index.html'
    template_name = 'question_form.html'
    form_class = AptitudeQuestionForm
    model = AptitudeQuestion

    def get_success_url(self):
        return reverse('question_list')


class QuestionListView(LoginRequiredMixin,ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'TestApp/index.html'
    template_name='question_list.html'
    model = AptitudeQuestion
    form = AptitudeQuestionForm
    #return render(request,'question_list.html',{'form':form})


class CreateQuestionView(LoginRequiredMixin,CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'TestApp/index.html'
    template_name = 'question_form.html'
    form_class = AptitudeQuestionForm
    model = AptitudeQuestion

    def get_success_url(self):
        return reverse('question_list')


class QuestionDetailView(LoginRequiredMixin,DetailView):
    login_url ='/accounts/login/'
    redirect_field_name = 'TestApp/index.html'
    template_name = 'question_detail.html'
    model = AptitudeQuestion


########################################################
############Schedule Model Views########################
########################################################

# class TestScheduleCreateView(LoginRequiredMixin,CreateView):
#     login_url = '/accounts/login/'
#     redirect_field_name = 'TestApp/index.html'
#     template_name = 'schedule_test.html'
#     form_class = TestScheduleForm
#     model = TestSchedule
#
#     def get_success_url(self):
#         return reverse('schedule_list')


class TestScheduleListView(LoginRequiredMixin,ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'TestApp/index.html'
    template_name = 'schedule_list.html'
    form_class = TestScheduleForm
    model = TestSchedule


class ScheduleDeleteView(LoginRequiredMixin,DeleteView):
    model = TestSchedule
    success_url = reverse_lazy('schedule_list')
    template_name = 'schedule_confirm_delete.html'


class ScheduleUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'TestApp/index.html'
    template_name = 'schedule_test.html'
    form_class = TestScheduleForm
    model = TestSchedule

    def get_success_url(self):
        return reverse('schedule_list')

########################################################
############CandidateScore Model Views##################
########################################################

class CandidateScoresListView(LoginRequiredMixin,ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'TestApp/index.html'
    template_name = 'candidatescore_list.html'
    form_class = CandidateScoresForm
    model = CandidateScores


class CandidateScoresDeleteView(LoginRequiredMixin,DeleteView):
    model = CandidateScores
    success_url = reverse_lazy('score_list')
    template_name = 'score_confirm_delete.html'


########################################################
###############Test Screen Views########################
########################################################

@candidate_login
def startaptitudetest(request):
    question_row = TestSchedule.objects.values('num_questions')[0]
    num_questions = question_row['num_questions']
    correct_count = 0
    time_limit_row = TestSchedule.objects.values('time_limit')[0]
    time_limit = time_limit_row['time_limit']
    print(time_limit)
    if request.method == "POST":
        print(request.POST)
        for i in range(num_questions):
            choice = 'chosen' + str(i + 1)
            answer = 'answer' + str(i + 1)
            if(request.POST.get(choice,"5") == request.POST.get(answer)):
                correct_count += 1
        return render(request,'test_result.html',{'score':correct_count})
    else:
        obj = AptitudeQuestion.objects.order_by('?')[:num_questions]
        return render(request,'aptitudetest_screen.html',{'obj':obj,'time_limit':time_limit})

@candidate_login
def select_test(request):
    apti_row = TestSchedule.objects.values('is_open')[0]
    is_apti_scheduled = apti_row['is_open']
    if(is_apti_scheduled == True):
        aptitude_scheduled = "true";
    return render(request,'select_test.html',{'aptitude_scheduled':is_apti_scheduled})
