from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User,Group
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


##Candidate Model######
class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    login_id = models.CharField(max_length=10,unique=True)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def save(self):
        top = Candidate.objects.select_for_update(nowait=True).order_by('-id')[0]
        self.login_id = 'Can%03d' % (top.id + 1)
        self.password = get_random_string(length=10)
        user = User.objects.create_user(username=self.login_id,
                             email=self.email,
                             password=self.password)
        user.save()
        super(Candidate,self).save()

###Reciever To Add Candidate to Group######

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name="Candidate"))

"""Admin Model
            Currently not implemented"""
class Admin(models.Model):
    login_id = models.CharField(max_length=10,unique=True)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.login_id

class AptitudeQuestion(models.Model):
    ANSWER_CHOICES = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
    )
    image = models.ImageField(null=True,blank=True,upload_to='questionImages')
    statement = models.CharField(max_length=1000)
    option1 = models.CharField(max_length=1000)
    option2 = models.CharField(max_length=1000)
    option3 = models.CharField(max_length=1000)
    option4 = models.CharField(max_length=1000)
    answer = models.IntegerField(choices=ANSWER_CHOICES)

    def __str__(self):
        return self.statement

class TestSchedule(models.Model):
    SUB_CHOICES= (
        ('Aptitude','Aptitude'),
    )
    subject = models.CharField(max_length=20,choices=SUB_CHOICES)
    is_open = models.BooleanField()
    num_questions = models.SmallIntegerField()
    time_limit = models.SmallIntegerField()

    def __str__(self):
        return str(self.subject)

class CandidateScores(models.Model):
    candidate_name = models.ForeignKey('Candidate',on_delete=models.CASCADE)
    date_taken = models.DateTimeField()
    score = models.SmallIntegerField()

    def __str__(self):
        return str(str(self.candidate_name) + " Test Date - " + str(self.date_taken))
