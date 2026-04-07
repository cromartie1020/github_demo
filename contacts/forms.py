from django import forms
from .models import Contacts    

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'email', 'phone', 'message']  

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'phone': 'Your Phone Number',
            'message': 'Your Message',
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter your name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        self.fields['phone'].widget.attrs['placeholder'] = 'Enter your phone number'
        self.fields['message'].widget.attrs['placeholder'] = 'Enter your message'

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = f'Enter your {field.label.lower()}'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Email is required.')
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone:
            raise forms.ValidationError('Phone number is required.')
        return phone

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if not message:
            raise forms.ValidationError('Message is required.')
        return message

    def clean(self):
        cleaned_data = super().clean()
        # Perform any additional validation across fields here
        return cleaned_data


        
                
