from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PortfolioImage, Service, SiteContent
from .serializers import PortfolioImageSerializer, ServiceSerializer, SiteContentSerializer


class HomeView(TemplateView):
    template_name = 'index.html'


class SiteContentAPIView(APIView):
    def get(self, request):
        content = SiteContent.objects.first()
        if not content:
            return Response({})
        serializer = SiteContentSerializer(content, context={'request': request})
        return Response(serializer.data)


class ServiceListAPIView(APIView):
    def get(self, request):
        serializer = ServiceSerializer(Service.objects.all(), many=True)
        return Response(serializer.data)


class PortfolioListAPIView(APIView):
    def get(self, request):
        serializer = PortfolioImageSerializer(
            PortfolioImage.objects.all(), many=True, context={'request': request}
        )
        return Response(serializer.data)
