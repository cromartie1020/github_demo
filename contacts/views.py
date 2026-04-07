from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Contacts
# Create your views here.

class ContactListView(ListView):
    model = Contacts
    template_name = 'contacts/contact_list.html'
    context_object_name = 'contacts'

class ContactDetailView(DetailView):
    model = Contacts
    template_name = 'contacts/contact_detail.html'
    context_object_name = 'contact'

class ContactCreateView(CreateView):
    model = Contacts
    template_name = 'contacts/contact_form.html'
    fields = ['name', 'email', 'phone', 'message']
    success_url = '/contacts/'

class ContactUpdateView(UpdateView):
    model = Contacts
    template_name = 'contacts/contact_form.html'
    fields = ['name', 'email', 'phone', 'message']
    success_url = '/contacts/'

class ContactDeleteView(DeleteView):
    model = Contacts
    template_name = 'contacts/contact_confirm_delete.html'
    success_url = '/contacts/'
