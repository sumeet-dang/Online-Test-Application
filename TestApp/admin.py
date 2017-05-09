from django.contrib import admin
from TestApp.models import Candidate,Admin,AptitudeQuestion,TestSchedule,CandidateScores
# Register your models here.

admin.site.register(Candidate)
admin.site.register(Admin)
admin.site.register(AptitudeQuestion)
admin.site.register(TestSchedule)
admin.site.register(CandidateScores)
