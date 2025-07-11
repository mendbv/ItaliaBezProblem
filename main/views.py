from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from .forms import ContactForm, ContactPopupForm
from .models import CompanyInfo, Service, TeamMember
from django.utils.translation import gettext_lazy as _

def get_company_info():
    """Helper function to get company info or default values."""
    return CompanyInfo.objects.first()

def home(request):
    company_info = get_company_info()
    services = Service.objects.filter(is_published=True)[:3]
    context = {
        'company_info': company_info,
        'services': services,
    }
    return render(request, 'main/index.html', context)

def about_us(request):
    company_info = get_company_info()
    context = {
        'company_info': company_info,
    }
    return render(request, 'main/about_us.html', context)

def services(request):
    company_info = get_company_info()
    all_services = Service.objects.filter(is_published=True)
    context = {
        'company_info': company_info,
        'services': all_services,
    }
    return render(request, 'main/services.html', context)

def mission_vision(request):
    company_info = get_company_info()
    context = {
        'company_info': company_info,
    }
    return render(request, 'main/mission_vision.html', context)

def team(request):
    company_info = get_company_info()
    team_members = TeamMember.objects.all()
    context = {
        'company_info': company_info,
        'team_members': team_members,
    }
    return render(request, 'main/team.html', context)

def contact(request):
    company_info = get_company_info()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message_content = form.cleaned_data['message']

            email_context = {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message_content,
            }

            html_message = render_to_string('emails/contact_form_submission.html', email_context)
            
            plain_message = (
                f"Новый запрос на контакт с сайта:\n\n"
                f"Имя: {name}\n"
                f"Email: {email}\n"
                f"Тема: {subject}\n"
                f"Сообщение:\n{message_content}"
            )

            try:
                send_mail(
                    subject,
                    plain_message,
                    settings.DEFAULT_FROM_EMAIL,
                    ['shirin@italiabezproblem.com',
                     'michele@italiabezproblem.com',
                     'info@italiabezproblem.com'],
                    fail_silently=False,
                    html_message=html_message,
                )
                messages.success(request, _("Your message has been sent successfully!"))
                return redirect('contact')
            except Exception as e:
                messages.error(request, _("There was an error sending your message. Please try again later."))
                print(f"Error sending email: {e}")
        else:
            messages.error(request, _("Please correct the errors below."))
    else:
        form = ContactForm()

    context = {
        'company_info': company_info,
        'form': form,
    }
    return render(request, 'main/contact.html', context)

@require_POST
@csrf_exempt
def contact_popup(request):
    form = ContactPopupForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data.get('email')
        phone = form.cleaned_data.get('phone')
        message_content = form.cleaned_data.get('message')

        email_context = {
            'name': name,
            'email': email if email else _("Не указан"),
            'phone': phone if phone else _("Не указан"),
            'message': message_content if message_content else _("Сообщение не предоставлено."),
        }

        html_message = render_to_string('emails/popup_contact_form_submission.html', email_context)

        plain_message = (
            f"Новый запрос на контакт из всплывающего окна сайта:\n\n"
            f"Имя: {name}\n"
            f"Email: {email if email else _('Не указан')}\n"
            f"Телефон: {phone if phone else _('Не указан')}\n"
            f"Сообщение:\n{message_content if message_content else _('Сообщение не предоставлено.')}"
        )

        try:
            send_mail(
                _("Новый запрос на контакт из всплывающего окна сайта"),
                plain_message,
                settings.DEFAULT_FROM_EMAIL,
                ['shirin@italiabezproblem.com',
                'michele@italiabezproblem.com',
                'info@italiabezproblem.com'],
                fail_silently=False,
                html_message=html_message,
            )
            return JsonResponse({'success': True, 'message': _("Your request has been sent successfully!")})
        except Exception as e:
            print(f"Error sending popup email: {e}")
            return JsonResponse({'success': False, 'message': _("An error occurred. Please try again.")}, status=500)
    else:
        errors = form.errors.as_json()
        return JsonResponse({'success': False, 'message': _("Please correct the errors below."), 'errors': errors}, status=400)

