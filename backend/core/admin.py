from django.contrib import admin

from .models import PortfolioImage, Service, SiteContent


@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ('hero_title', 'contact_phone', 'updated_at')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'order')
    list_editable = ('price', 'order')


@admin.register(PortfolioImage)
class PortfolioImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
