from django import forms
from .models import Review  # Ensure this import statement is correct based on your project structure

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']  # add the fields you have in the Review model that you want in the form
