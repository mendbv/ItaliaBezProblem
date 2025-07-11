from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label=_("Your Name"))
    email = forms.EmailField(label=_("Your Email"))
    subject = forms.CharField(max_length=200, label=_("Subject"))
    message = forms.CharField(widget=forms.Textarea, label=_("Your Message"))

class ContactPopupForm(forms.Form):
    name = forms.CharField(max_length=100, label=_("Your Name"), help_text=_("Enter your name"), required=True)
    email = forms.EmailField(label=_("Your Email (Optional)"), help_text=_("Enter your email"), required=False)
    phone = forms.CharField(max_length=20, label=_("Your Phone (Optional)"), help_text=_("Enter your phone number"), required=False)
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'maxlength': 140}),
        max_length=140,
        label=_("Your Message (Optional, max 140 chars)"),
        help_text=_("Tell us how we can help you (max 140 characters)"),
        required=False
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')
        if not email and not phone:
            raise ValidationError(
                _("Please provide either your email or phone number."),
                code='no_contact_info'
            )
        return cleaned_data

