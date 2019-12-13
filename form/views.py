from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import FieldForm
from .models import FeedbackForm
from django.contrib.auth import authenticate

# Create your views here.

def contact(request):
    return render(request, 'contact/index.html')

def feedback(request):   
    if request.user.is_authenticated:
        context = {
            'page_title' : "FEEDBACK FORM",
            'feedback_forms': FieldForm
        }
        if request.method == 'GET':
            feedback_forms = FieldForm()
            context['feedback_forms'] = feedback_forms
            return render(request, 'feedbackform/index.html', context)
        else:
            received_form = FieldForm(request.POST)
            if received_form.is_valid():
                received_form.save()
                return render(request, 'success/index.html')
            else:
                context['feedback_forms'] = received_form
                return render(request, 'feedbackform/index.html', context)
    else:
        return redirect('form:contact')