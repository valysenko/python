from django.shortcuts import render


"""Renders index page
"""
def home(request):
    return render(request, "main/home.html")