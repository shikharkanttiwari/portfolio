from django.shortcuts import render
from .models import Job
# import os,sys,inspect
# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
# sys.path.insert(0,parentdir)
# from service import models
def home(request):
    jobs = Job.objects
    # services = Service.objects,'services':services
    return render(request,'job/index.html',{ 'jobs':jobs })
