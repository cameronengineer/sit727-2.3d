from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F
from pprint import pprint

from .models import Unit, Submission

def index(request):
    unit_list = Unit.objects.all()
    pprint(unit_list)
    context = {"unit_list": unit_list}
    return render(request, "ontrack/index.html", context)

def submissions(request, unit_id):
    pprint(Submission.objects.filter(unit=unit_id))
    submission_list = Submission.objects.filter(unit=unit_id)
    pprint(submission_list)
    context = {"submission_list": submission_list}
    return render(request, "ontrack/submissions.html", context)
