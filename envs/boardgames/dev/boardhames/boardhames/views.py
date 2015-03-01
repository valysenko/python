__author__ = 'vladyslav'

from django.views.generic.base import View
from django.shortcuts import render_to_response
from datetime import date
class HelloWorldView(View):
    def get(self,request):
        return render_to_response("helloworld.html",
                                  {'date':date.today()})