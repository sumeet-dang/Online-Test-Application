from django import forms
from django.contrib.auth.forms import AuthenticationForm
from TestApp.models import (Candidate,Admin,AptitudeQuestion,
                                    TestSchedule,CandidateScores)


class CandidateForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = ['first_name','last_name','email',]

        widgets = {
            'first_name' : forms.TextInput(attrs={'class' : 'textinputclass form-control'}),
            'last_name' : forms.TextInput(attrs={'class' : 'textinputclass form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'textinputclass form-control'}),
            #'login_id' : forms.TextInput(attrs={'class' : 'textinputclass form-control'}),
            #'password' : forms.PasswordInput(attrs={'class' : 'textinputclass form-control'}),
        }


class TeacherForm(forms.ModelForm):

    class Meta:
        model = Admin
        fields = '__all__'

        widgets = {
            'login_id' : forms.TextInput(attrs={'class' : 'textinputclass form-control'}),
            'password' : forms.PasswordInput(attrs={'class' : 'textinputclass form-control'}),
        }

class AptitudeQuestionForm(forms.ModelForm):

    class Meta:
        model = AptitudeQuestion
        fields = '__all__'
        widgets = {
            'image' : forms.FileInput(),
            'statement' : forms.Textarea(attrs={'class' : 'Areaclass form-control'}),
            'option1' : forms.Textarea(attrs={'class' : 'Areaclass form-control'}),
            'option2' : forms.Textarea(attrs={'class' : 'Areaclass form-control'}),
            'option3' : forms.Textarea(attrs={'class' : 'Areaclass form-control'}),
            'option4' : forms.Textarea(attrs={'class' : 'Areaclass form-control'}),
            'answer' : forms.Select(attrs={'class' : 'Areaclass form-control'}),
        }

class TestScheduleForm(forms.ModelForm):

    class Meta:
        max_ques = AptitudeQuestion.objects.count()
        model = TestSchedule
        fields = '__all__'
        widgets = {
            'subject' : forms.Select(attrs={'class' : 'form-control','style':'max-width:70%'}),
            'isopen' : forms.CheckboxInput(attrs={'class' : 'AreaClass form-control'}),
            'num_questions' : forms.NumberInput(attrs={'class' : 'Areaclass form-control','min' : '1', 'max' : '5'}),
            'time_limit' : forms.NumberInput(attrs={'class' : 'Areaclass form-control','min' : '1'}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password', 'type': 'password'}))


class CandidateScoresForm(forms.ModelForm):
    model = CandidateScores
    fields = '__all__'
    widgets = {
        'candidate_name' : forms.TextInput(attrs={'class' : 'textinputclass form-control'}),
        'date_taken' : forms.TextInput(attrs={'class' : 'textinputclass form-control','type' : 'date'}),
        'score' : forms.TextInput(attrs={'class' : 'textinputclass form-control'}),
    }
