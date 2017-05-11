from django.conf.urls import url
from TestApp import views
from django.views.generic import TemplateView
from functools import wraps
from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from TestApp.views import admin_login


# def admin_login(view_func):
#     def _decorator(request, *args, **kwargs):
#         if(request.user.groups.filter(name__in=['Candidate']).exists()):
#             return redirect(reverse('invalid_login'))
#         else:
#             response = view_func(request, *args, **kwargs)
#             return response
#     return wraps(view_func)(_decorator)


urlpatterns =[
    url(r'^$',views.Check_privledges,name='index'),
    url(r'^home',TemplateView.as_view(template_name='home.html'),name='home'),
    url(r'^admin_index',login_required(TemplateView.as_view(template_name='admin_index.html')),name='admin_index'),
    url(r'^invalid',TemplateView.as_view(template_name='invalid_login.html'),name='invalid_login'),
    url(r'^candidate_index',login_required(TemplateView.as_view(template_name='candidate_index.html')),name='candidate_index'),
    url(r'^about',TemplateView.as_view(template_name='about.html'),name='about'),
    url(r'^candidate_index',login_required(TemplateView.as_view(template_name='candidate_index.html')),name='candidate_index'),

    url(r'^candidate/new/$',login_required(views.CreateUserView),name='candidate_new'),
    url(r'^candidate/(?P<pk>\d+)$',admin_login(views.CandidateDetailView.as_view()),name='candidate_detail'),
    url(r'^candidate_list/$',admin_login(views.CandidateListView.as_view()),name='candidate_list'),


    url(r'^question/(?P<pk>\d+)/edit/$', admin_login(views.QuestionUpdateView.as_view()), name='question_edit'),
    url(r'^question/(?P<pk>\d+)/remove/$', admin_login(views.QuestionDeleteView.as_view()), name='question_remove'),
    url(r'^question/new/$', admin_login(views.CreateQuestionView.as_view()), name='question_new'),
    url(r'^question_list/$',admin_login(views.QuestionListView.as_view()),name='question_list'),

    url(r'^schedule_list/$',admin_login(views.TestScheduleListView.as_view()),name='schedule_list'),
    url(r'^schedule/(?P<pk>\d+)/edit/$', admin_login(views.ScheduleUpdateView.as_view()), name='schedule_edit'),

    url(r'^score_list/$',admin_login(views.CandidateScoresListView.as_view()),name='score_list'),
    url(r'^score/(?P<pk>\d+)/remove/$', admin_login(views.CandidateScoresDeleteView.as_view()), name='score_remove'),

    url(r'^start_test',login_required(views.startaptitudetest),name='start_test'),
    url(r'^select_test',login_required(views.select_test),name='select_test'),
    url(r'^test_scores',views.display_scores,name='test_scores'),
]
