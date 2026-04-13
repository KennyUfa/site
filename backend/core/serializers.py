from rest_framework import serializers

from .models import PortfolioImage, Service, SiteContent


class SiteContentSerializer(serializers.ModelSerializer):
    hero_image_url = serializers.SerializerMethodField()
    about_image_url = serializers.SerializerMethodField()

    class Meta:
        model = SiteContent
        fields = [
            'hero_title',
            'hero_subtitle',
            'about_text',
            'contact_phone',
            'contact_email',
            'contact_telegram',
            'contact_address',
            'hero_image_url',
            'about_image_url',
        ]

    def _abs_url(self, image):
        if not image:
            return ''
        request = self.context.get('request')
        return request.build_absolute_uri(image.url) if request else image.url

    def get_hero_image_url(self, obj):
        return self._abs_url(obj.hero_image)

    def get_about_image_url(self, obj):
        return self._abs_url(obj.about_image)


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'price']


class PortfolioImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = PortfolioImage
        fields = ['id', 'title', 'image_url']

    def get_image_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url) if request else obj.image.url
