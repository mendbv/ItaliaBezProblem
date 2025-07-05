from modeltranslation.translator import translator, TranslationOptions
from .models import CompanyInfo, Service, TeamMember

class CompanyInfoTranslationOptions(TranslationOptions):
    fields = ('slogan', 'about_us_short', 'about_us_full', 'mission', 'vision',)

class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'full_description',)

class TeamMemberTranslationOptions(TranslationOptions):
    fields = ('position', 'experience',)

translator.register(CompanyInfo, CompanyInfoTranslationOptions)
translator.register(Service, ServiceTranslationOptions)
translator.register(TeamMember, TeamMemberTranslationOptions)
