from django.urls import path
from .views import (
    index, about, contact, contact_success, feature, financing,
    quote, quote_success, service, testimonial, newsletter_and_quote,
    newsletter_signup, newsletter_signup_success
)

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('contact/success/', contact_success, name='contact_success'),
    path('feature/', feature, name='feature'),
    path('financing/', financing, name='financing'),
    path('quote/', quote, name='quote'),
    path('quote/success/', quote_success, name='quote_success'),
    path('service/', service, name='service'),
    path('testimonial/', testimonial, name='testimonial'),
    path('newsletter_and_quote/', newsletter_and_quote, name='newsletter_and_quote'),
    path('newsletter_signup/', newsletter_signup, name='newsletter_signup'),
    path('newsletter_signup/success/', newsletter_signup_success, name='newsletter_signup_success'),
]
