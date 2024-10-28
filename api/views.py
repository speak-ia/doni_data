from django.shortcuts import render

# Create your views here.
# api/views.py
from rest_framework import generics
from .models import Enqueteur, Enquete
from .serializers import EnqueteurSerializer, EnqueteSerializer
from django.shortcuts import render, redirect
from .firebase_config import auth

def signup(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            try:
                # Create user with Firebase
                user = auth.create_user_with_email_and_password(email, password)
                # Redirect to sign-in page after successful signup
                return redirect('signin')
            except Exception as e:
                error_message = str(e)
                return render(request, 'signup.html', {'error': error_message})
        else:
            error_message = "Passwords do not match"
            return render(request, 'signup.html', {'error': error_message})

    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Sign in user with Firebase
            user = auth.sign_in_with_email_and_password(email, password)
            # Store the user's ID token in the session
            request.session['user_id'] = user['localId']
            return redirect('home')  # Redirect to a home page
        except Exception as e:
            error_message = str(e)
            return render(request, 'signin.html', {'error': error_message})

    return render(request, 'signin.html')

def signout(request):
    # Clear the session
    request.session.flush()
    return redirect('signin')


class EnqueteurListCreateAPIView(generics.ListCreateAPIView):
    queryset = Enqueteur.objects.all()
    serializer_class = EnqueteurSerializer

class EnqueteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Enquete.objects.all()
    serializer_class = EnqueteSerializer


