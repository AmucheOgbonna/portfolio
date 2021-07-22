from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ContactForm
from django.core.mail import EmailMessage
from django.contrib.auth import login

# Create your views here.
# def login(request):
#     return render(request, 'portfolio_backapp/login.html')
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'portfolio_backapp/register.html', {'form':form})

def Contact(request):
    contact_form = ContactForm
    if request.method == 'POST':
        form = contact_form(data= request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
        
            template = get_template('portfolio_app/contact_form.txt')

            content = {
                'contact_name': request.POST.get('contact_name'),
                'contact_email': request.POST.get('contact_email'),
                'subject' : request.POST.get('subject'),
                'message': request.POST.get('message')
            }
            content = template.render(content)

        email = EmailMessage(
            'Contact Us',
            'Portfolio App',
            ['amuche247cynthia@gmail.com'],
            headers= {'Reply to' : contact_email}
        )
        email.send()

        return render(messages.success(request, f'Message sent!'))
    return render(request, 'portfolio_app/index.html', {'form':contact_form})
