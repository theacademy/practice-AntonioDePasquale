from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()

    contacts = Contact.objects.all()
    return render(request, 'home.html', {'form': form, 'contacts': contacts})

# View for adding a contact
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')  # Redirect to the contact list page
    else:
        form = ContactForm()
    return render(request, 'add_contact.html', {'form': form})

# View to list all contacts
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})