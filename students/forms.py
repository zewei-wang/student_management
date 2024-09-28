import re

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
            return email
        raise forms.ValidationError('Invalid email address')

    def clean_grade(self):
        grade = self.cleaned_data.get('grade')
        if not 1 <= grade <= 10:
            raise forms.ValidationError('Grade must be between 1 and 10.')
        return grade