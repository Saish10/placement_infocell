from django.shortcuts import render


def homepage(request):
    return render(request, 'main.html')


def computer(request):
    return render(request, "department_detail.html")
