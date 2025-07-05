from django.db import models
from django.utils.translation import gettext_lazy as _

class CompanyInfo(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Company Name"))
    slogan = models.CharField(max_length=255, verbose_name=_("Slogan"))
    address = models.CharField(max_length=255, verbose_name=_("Address"))
    working_hours_mon_fri = models.CharField(max_length=100, verbose_name=_("Working Hours (Mon-Fri)"))
    working_hours_sat = models.CharField(max_length=100, verbose_name=_("Working Hours (Saturday)"))
    email = models.EmailField(verbose_name=_("Email"))
    phone = models.CharField(max_length=50, verbose_name=_("Phone"))
    telegram_link = models.URLField(blank=True, null=True, verbose_name=_("Telegram Link"))
    instagram_link = models.URLField(blank=True, null=True, verbose_name=_("Instagram Link"))
    linkedin_link = models.URLField(blank=True, null=True, verbose_name=_("LinkedIn Link"))
    whatsapp_number = models.CharField(max_length=20, blank=True, null=True, verbose_name=_("WhatsApp Number (e.g., +1234567890)"))
    whatsapp_link = models.URLField(blank=True, null=True, verbose_name=_("WhatsApp Link"))
    clients_count = models.IntegerField(default=0, verbose_name=_("Number of Served Clients"))
    about_us_short = models.CharField(max_length=300, verbose_name=_("Short About Us Description"), help_text=_("Used on homepage"))
    about_us_full = models.TextField(verbose_name=_("Full About Us Description"), help_text=_("Used on About Us page"))
    mission = models.TextField(verbose_name=_("Mission"))
    vision = models.TextField(verbose_name=_("Vision"))
    homepage_video = models.FileField(upload_to='videos/', blank=True, null=True, verbose_name=_("Homepage Video (MP4)"))

    class Meta:
        verbose_name = _("Company Information")
        verbose_name_plural = _("Company Information")

    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Service Title"))
    short_description = models.CharField(max_length=300, verbose_name=_("Short Description"), help_text=_("Used for cards"))
    full_description = models.TextField(verbose_name=_("Full Description"), help_text=_("Used on service details page"))
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name=_("Price (EUR)"))
    icon_class = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Icon Class (e.g., 'fas fa-briefcase')"))
    is_published = models.BooleanField(default=True, verbose_name=_("Is Published"))

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    full_name = models.CharField(max_length=100, verbose_name=_("Full Name"))
    position = models.CharField(max_length=100, verbose_name=_("Position"))
    experience = models.TextField(blank=True, null=True, verbose_name=_("Experience"))
    photo = models.ImageField(upload_to='team_photos/', blank=True, null=True, verbose_name=_("Photo"))
    linkedin_profile = models.URLField(blank=True, null=True, verbose_name=_("LinkedIn Profile"))

    class Meta:
        verbose_name = _("Team Member")
        verbose_name_plural = _("Team Members")

    def __str__(self):
        return self.full_name
