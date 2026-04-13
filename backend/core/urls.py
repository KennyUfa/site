from django.urls import path

from .views import PortfolioListAPIView, ServiceListAPIView, SiteContentAPIView

urlpatterns = [
    path('content/', SiteContentAPIView.as_view(), name='api-content'),
    path('services/', ServiceListAPIView.as_view(), name='api-services'),
    path('portfolio/', PortfolioListAPIView.as_view(), name='api-portfolio'),
]
