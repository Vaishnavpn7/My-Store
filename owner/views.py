from django.shortcuts import render
from django.views.generic import View
from owner.forms import LoginForm, RegistrationForm, ProductForm
from django.contrib.auth.models import User


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')


class SignupView(View):

    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request, *args, **kw):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'form': form})


class SigninView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request, *args, **kw):
        print(request.POST.get('username'))
        print(request.POST.get('password'))
        return render(request, 'home.html')


class ProductCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ProductForm()
        return render(request, 'product-add.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'home.html')
        else:
            return render(request, 'product-add.html', {'form': form})
