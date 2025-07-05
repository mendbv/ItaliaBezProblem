from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import CompanyInfo, Service, TeamMember

@admin.register(CompanyInfo)
class CompanyInfoAdmin(TranslationAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'whatsapp_number',
        'working_hours_mon_fri',
    )
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'slogan',
                'homepage_video',
                'clients_count',
            )
        }),
        ('Contact Information', {
            'fields': (
                'address',
                'working_hours_mon_fri',
                'working_hours_sat',
                'email',
                'phone',
                'whatsapp_number',
                'whatsapp_link',
            )
        }),
        ('Social Media Links', {
            'fields': (
                'telegram_link',
                'instagram_link',
                'linkedin_link',
            )
        }),
        ('About Us & Mission/Vision', {
            'fields': (
                'about_us_short',
                'about_us_full',
                'mission',
                'vision',
            )
        }),
    )

@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ('title', 'price', 'is_published',)
    list_filter = ('is_published',)
    search_fields = ('title',)
    fieldsets = (
        (None, {
            'fields': (
                'title',
                'short_description',
                'full_description',
                'price',
                'icon_class',
                'is_published',
            )
        }),
    )

@admin.register(TeamMember)
class TeamMemberAdmin(TranslationAdmin):
    list_display = ('full_name', 'position', 'photo',)
    search_fields = ('full_name', 'position',)
    fieldsets = (
        (None, {
            'fields': (
                'full_name',
                'position',
                'experience',
                'photo',
                'linkedin_profile',
            )
        }),
    )
