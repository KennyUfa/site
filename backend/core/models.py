from django.db import models


class SiteContent(models.Model):
    hero_title = models.CharField('Заголовок на первом экране', max_length=200)
    hero_subtitle = models.CharField('Подзаголовок', max_length=255, blank=True)
    about_text = models.TextField('Текст блока "Обо мне"')
    contact_phone = models.CharField('Телефон', max_length=30)
    contact_email = models.EmailField('Email', blank=True)
    contact_telegram = models.CharField('Telegram', max_length=100, blank=True)
    contact_address = models.CharField('Адрес', max_length=255, blank=True)
    hero_image = models.ImageField('Фото для обложки', upload_to='hero/', blank=True)
    about_image = models.ImageField('Фото для блока "Обо мне"', upload_to='about/', blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Контент сайта'
        verbose_name_plural = 'Контент сайта'

    def __str__(self):
        return 'Контент сайта'


class Service(models.Model):
    title = models.CharField('Название услуги', max_length=120)
    description = models.TextField('Описание', blank=True)
    price = models.DecimalField('Цена', max_digits=8, decimal_places=2)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Услуга'
        verbose_name_plural = 'Прайс-лист'

    def __str__(self):
        return f'{self.title} — {self.price} ₽'


class PortfolioImage(models.Model):
    title = models.CharField('Название', max_length=120, blank=True)
    image = models.ImageField('Фотография', upload_to='portfolio/')
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Фотография портфолио'
        verbose_name_plural = 'Портфолио'

    def __str__(self):
        return self.title or f'Фото #{self.pk}'
