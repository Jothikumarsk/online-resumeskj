
from django.http import HttpResponse
from django.shortcuts import render
from .models import Summary, WorkExperience, Skills, SocialMedia, Education, Awards


def index(request):
    summary = Summary.objects.all()
    skills = Skills.objects.all()
    workexperience = WorkExperience.objects.all()
    socialmedia = SocialMedia.objects.all()
    education = Education.objects.all()
    awards = Awards.objects.all()
    

   # print (Executive_summary)
     #'Skills' : skills,
     # 'Work_Experience' : workexperience,
      #'Social_Media': socialmedia,
      #'Education' : education 
   
   
    return render(request,'index.html', {
      'content': summary,
       'work': workexperience,
       'skill': skills,
       'Social_Media': socialmedia,
       'Education' : education,
       'Awards' : awards
    })



