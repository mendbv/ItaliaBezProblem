from .models import CompanyInfo

def company_info_processor(request):
    """
    Adds the first CompanyInfo object to the context of every template.
    This allows access to company_info in any template without explicitly
    passing it from each view.
    """
    try:
        company_info = CompanyInfo.objects.first()
    except CompanyInfo.DoesNotExist:

        company_info = None
    return {'company_info': company_info}

