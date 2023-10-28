from django.shortcuts import render, redirect
from .forms import InputForm
from django.contrib.auth import login
from django.contrib import messages

def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chat/chatPage.html", context)

def homeView(request):
    context = {}
    context['form'] = InputForm ()
    return render(request, "chat/LoginPage.html", context)

def register_request(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("chat-page")
        messages.error(request, "Registration failed.")
    form = InputForm()
    return render(request=request, template_name="chat/RegisterPage.html", context={"register_form":form})