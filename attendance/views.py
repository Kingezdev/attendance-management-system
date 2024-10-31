from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages  # Import the messages framework
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AttendanceForm
from .models import Attendance
import csv


@login_required
def download_attendance(request):
    # Define the response as a CSV file
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="attendance_list.csv"'

    # Create a CSV writer
    writer = csv.writer(response)
    writer.writerow(['Matric Number', 'Student Name', 'Date', 'Status'])

    # Fetch attendance records and write them to the CSV file
    attendance_records = Attendance.objects.all()
    for record in attendance_records:
        writer.writerow([record.matric_number, record.student_name, record.date, record.status])

    return response

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')
    return render(request, 'login.html', {'page': 'login'})

def registerPage(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.username = user.username.lower()
        user.save()
        login(request, user)
        return redirect('home')
    return render(request, 'login.html', {'form': form})


#logout view
def logoutUser(request):
    logout(request)
    return redirect('login')

def menu(request):
    return render(request, 'menu.html', )

@login_required(login_url='login')
def record_attendance(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AttendanceForm(request.POST)
            if form.is_valid():
                matric_number = form.cleaned_data.get('matric_number')
                date = form.cleaned_data.get('date')
                status = form.cleaned_data.get('status')

                # Check if a record with this matric number and date already exists
                attendance_record = Attendance.objects.filter(matric_number=matric_number, date=date).first()
                
                if attendance_record:
                    # Update existing record
                    attendance_record.status = status
                    attendance_record.save()
                    messages.success(request, "Attendance updated successfully.")
                else:
                    # Create a new record
                    form.save()
                    messages.success(request, "Attendance recorded successfully.")
                return redirect('attendance:success')
            else:
                messages.error(request, "Error in form submission. Please check the details.")
        
        else:
            form = AttendanceForm()
        
        return render(request, 'attendance/attendance_form.html', {'form': form})
    else:
        # Redirect unauthenticated users to login/register page
        return render(request, 'login.html')
    
def success(request):
    return render(request, 'attendance/success.html')

@login_required
def list_attendance(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'attendance/list_attendance.html', {'attendance_records': attendance_records})
