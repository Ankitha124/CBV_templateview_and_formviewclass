from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from app.forms import*
from django.http import HttpResponse

# Create your views here.


# inserting by using TemplateView class

class TempdataRender(TemplateView):
    template_name='TempdataRender.html' # html page name which we have to render


    def get_context_data(self, **kwargs):  #method overriding from parent class 
        ECDO=super().get_context_data(**kwargs)  # chaining 
        SFO=StudentForm()  # collecting student form object
        ECDO['SFO']=SFO   #adding context to empty context dictionary
        return ECDO   #returning the object with data
    
    def post(self,request): #check for the post method
        SFD=StudentForm(request.POST) #collect the data from user
        if SFD.is_valid(): #validate the data 
            SFD.save()  # save the data 
            return HttpResponse('<h1> data is inserted</h1>')


#inserting by using FormView class
        
class StudentFormViewInsert(FormView):# inherit the FormView class 
    template_name='StudentFormViewInsert.html' #htmlpage name

    form_class=StudentForm # it will perform get_context, called by super(),creates form object, context will be added as value and return 

    def form_valid(self, form): #check for post method, collect the data and valid the data
        form.save() #save the collected data 
        return HttpResponse('<h1> data is inserted</h>')
    

    
    




