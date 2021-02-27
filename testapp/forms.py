from django import forms
from multiselectfield import MultiSelectFormField


class Feedback_Data_Form(forms.Form):
    name = forms.CharField(
        label='Enter Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Name::'
            }
        )
    )
    rating = forms.IntegerField(
        label='Your Rating-',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Rating Here...'
            }
        )
    )
    feedback = forms.CharField(
        label='Your FeedBack -',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Feedback here...'
            }
        )
    )


class Suggestion_form(forms.Form):
    name = forms.CharField(
        label='Enter Your Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Name here...'
            }
        )
    )
    suggestion_name = forms.CharField(
        label='Your Suggestion ->',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your suggestion here...'
            }
        )
    )