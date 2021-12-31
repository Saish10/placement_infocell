from django.shortcuts import render

from django.http import HttpResponse


def homepage(request):
    return render(request, 'main.html')


def departments(request):
    return render(request, "departments.html")


def computer(request):
    return render(request, "computer.html")
