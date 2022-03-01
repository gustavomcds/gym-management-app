from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.password_validation import validate_password

def signup(request):

    if request.user.is_authenticated:

        return redirect('/')

    if request.method == "GET":

        return render(request, 'signup.html')

    elif request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        print(password, password_confirm)

        if password == password_confirm:
            if len(username.strip()) > 0 and len(password.strip()) > 0 and len(password_confirm.strip()) > 0 \
                and len(email.strip()) > 0 and len(first_name.strip()) > 0 and len(last_name.strip()) > 0:

                user = User.objects.filter(username = username)

                if not user:

                    new_user = User.objects.create_user(username = username, 
                                            password = password, 
                                            email = email, 
                                            first_name = first_name, 
                                            last_name = last_name)

                    new_user.save()

                    try:
                        password_validation = validate_password(password=password)
                    except ValidationError as errors:
                        for error in errors:
                            messages.add_message(request, constants.ERROR, error)
                        return redirect('/auth/signup')

                    messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso')
                    return redirect('/auth/login')

                else:

                    messages.add_message(request, constants.ERROR, 'Usuário já cadastrado')
                    return redirect('/auth/signup')

            else:
                messages.add_message(request, constants.ERROR, 'Dados inválidos')
                return redirect('/auth/signup')
        else:
            messages.add_message(request, constants.ERROR, 'A senha e a confirmação de senha devem ser iguais')
            return redirect('/auth/signup')

def login(request):

    if request.method == "GET":

        if request.user.is_authenticated:
            return redirect('/')

        return render(request, 'login.html')

    elif request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if not user:
            messages.add_message(request, messages.constants.ERROR, 'Usuário ou senha inválidos')
            return redirect('/auth/login')
        else:
            print(f"username: {username} - password: {password}")
            auth.login(request, user)
            return render(request, 'signup.html')

def logout(request):

    auth.logout(request)

    return redirect('/auth/login')
