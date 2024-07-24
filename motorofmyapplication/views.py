from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm, NewsletterSignupForm
import requests
import json

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def verify_recaptcha(token):
    url = 'https://recaptchaenterprise.googleapis.com/v1/projects/jp-cooling-and-h-1715985656693/assessments?key=YOUR_API_KEY'
    payload = {
        "event": {
            "token": token,
            "siteKey": settings.RECAPTCHA_PUBLIC_KEY,
            "expectedAction": "submit"
        }
    }
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    result = response.json()
    return result.get('tokenProperties', {}).get('valid', False)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        recaptcha_token = request.POST.get('g-recaptcha-response')
        if form.is_valid() and verify_recaptcha(recaptcha_token):
            # Send email
            subject = f"Message from {form.cleaned_data['name']}"
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['email']
            recipient_list = [settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, recipient_list)
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')

def feature(request):
    return render(request, 'feature.html')

def financing(request):
    return render(request, 'financing.html')

def quote(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        recaptcha_token = request.POST.get('g-recaptcha-response')
        if form.is_valid() and verify_recaptcha(recaptcha_token):
            # Handle form submission (e.g., save data, send email, etc.)
            return redirect('quote_success')
    else:
        form = ContactForm()
    return render(request, 'quote.html', {'form': form})

def quote_success(request):
    return render(request, 'quote_success.html')

def service(request):
    return render(request, 'service.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def newsletter_and_quote(request):
    return render(request, 'newsletter_and_quote.html')

def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        recaptcha_token = request.POST.get('g-recaptcha-response')
        if form.is_valid() and verify_recaptcha(recaptcha_token):
            # You can save the email to your database or send an email
            return redirect('newsletter_signup_success')
    else:
        form = NewsletterSignupForm()
    return render(request, 'newsletter_and_quote.html', {'form': form})

def newsletter_signup_success(request):
    return render(request, 'newsletter_signup_success.html')
