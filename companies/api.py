from rest_framework.response import Response
from rest_framework.decorators import api_view

from companies.models import Company


@api_view(['GET'])
def companies(request):
    return Response([
        {
            'name': company.name,
            'description': company.description,
        }
        for company in Company.objects.iterator()
    ])
