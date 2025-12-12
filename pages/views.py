from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def about_view(request):
    return render(request, 'pages/about_me.html')

def experience_view(request):
    return render(request, 'pages/experience.html')

def contact_view(request):
    # Handle contact form submission
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Validate the form and collect data
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Build the email content
            message_body = (
                f'You have a new email from your Portfolio webpage \n'
                f'Name: {name}\n'
                f'Email: {email}\n'
                f'Message: {message}\n'
            )
            try:
                send_mail(
                    # Subject
                    f'Email from Portfolio Website',
                    # Message Body --> The user typed message
                    message_body,
                    email,  # From email (user's email)
                    ['zanem201@gmail.com'],  # To email (your email)
                )
                # after sending the email
                form = ContactForm()  # Reset the form
                return render(request, 'pages/contact.html', { 'form': form})
            except Exception as e:
                print(f'Error sending email: {e}')
                return render(request, 'pages/contact.html', {'form': form})
        else:
            print('Form is not valid')
    else:
        form = ContactForm()
        return render(request, 'pages/contact.html', {'form': form})
    
    form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})