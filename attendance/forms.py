from django import forms
from .models import Attendance

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance  # Specify the model here
        fields = ['matric_number', 'student_name', 'status']  # List the fields you want in the form


from django import forms

class AttendanceUpdateForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget(), label="Select Date")

