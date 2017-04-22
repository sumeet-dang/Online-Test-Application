from django import forms

from TestApp.models import Candidate,Admin,AptitudeQuestion,TestSchedule


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
        model = TestSchedule
        fields = '__all__'
        widgets = {
            'subject' : forms.Select(attrs={'class' : 'AreaClass form-control'}),
            'isopen' : forms.CheckboxInput(attrs={'class' : 'AreaClass form-control'}),
            'num_questions' : forms.NumberInput(attrs={'class' : 'Areaclass form-control'}),
        }
