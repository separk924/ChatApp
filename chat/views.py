from django.shortcuts import render, redirect
from .forms import InputForm

def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chat/chatPage.html", context)

def homeView(request):
    context = {}
    context['form'] = InputForm ()
    return render(request, "chat/LoginPage.html", context)