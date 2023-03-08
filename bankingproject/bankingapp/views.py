from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from datetime import date
# Create your views here.


from django.shortcuts import render, redirect, get_object_or_404

from .forms import MemberCreationForm, UserRegisterForm
from .models import Register, Branch


def index(request):
    return render(request, "index.html")



def register_success(request):
    return render(request, "register_success.html")


def logout(request):
    auth.logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')


def create_view(request):
    form = MemberCreationForm()
    if request.method == 'POST':
        form = MemberCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bankingapp:register_success')
    return render(request, 'home.html', {'form': form})


def update_view(request, pk):
    member = get_object_or_404(Register, pk=pk)
    form = MemberCreationForm(instance=member)
    if request.method == 'POST':
        form = MemberCreationForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('change', pk=pk)
    return render(request, 'home.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('email.html')
            d = {'username': username}
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form, 'title': 'register here'})


# AJAX
def load_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).all()
    return render(request, 'branch_dropdown_list_options.html', {'branches': branches})


def calculate_age(request):
    birthdate = request.GET.get('birthdate')
    today = date.today()
    age= today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return render(request,'cal_age.html',{'age':age})