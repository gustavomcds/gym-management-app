from django.shortcuts import get_object_or_404, render
from training_sessions.models import TrainingSession
from django.contrib.auth.decorators import login_required

@login_required(login_url="/auth/login")
def sessions(request):

    training_sessions = TrainingSession.objects.all()

    return render(request, 'sessions.html', {'training_sessions' : training_sessions})

@login_required(login_url="/auth/login")
def one_session(request, id):

    training_session = get_object_or_404(TrainingSession, id=id)

    return render(request, 'session.html', {'training_session' : training_session})

@login_required(login_url="/auth/login")
def insert_checkin(request):

    pass

@login_required(login_url="/auth/login")
def remove_checkin(request):

    pass