from django.conf.urls import url
from TestApp import views
from django.views.generic import TemplateView

urlpatterns =[
    url(r'^$',TemplateView.as_view(template_name='index.html'),name='index'),
    url(r'^about',TemplateView.as_view(template_name='about.html'),name='about'),
    url(r'^candidate_index',TemplateView.as_view(template_name='candidate_index.html'),name='candidate_index'),

    url(r'^candidate/new/$',views.CreateUserView,name='candidate_new'),
    url(r'^candidate/(?P<pk>\d+)$',views.CandidateDetailView.as_view(),name='candidate_detail'),
    url(r'^candidate_list/$',views.CandidateListView.as_view(),name='candidate_list'),


    url(r'^question/(?P<pk>\d+)/edit/$', views.QuestionUpdateView.as_view(), name='question_edit'),
    url(r'^question/(?P<pk>\d+)/remove/$', views.QuestionDeleteView.as_view(), name='question_remove'),
    url(r'^question/new/$', views.CreateQuestionView.as_view(), name='question_new'),
    url(r'^question_list/$',views.QuestionListView.as_view(),name='question_list'),

    url(r'^schedule_list/$',views.TestScheduleListView.as_view(),name='schedule_list'),
    url(r'^schedule/(?P<pk>\d+)/edit/$', views.ScheduleUpdateView.as_view(), name='schedule_edit'),

    url(r'^start_test',views.startaptitudetest,name='start_test')

]
