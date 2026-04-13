from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, verbose_name='Название')),
                ('image', models.ImageField(upload_to='portfolio/', verbose_name='Фотография')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Фотография портфолио',
                'verbose_name_plural': 'Портфолио',
                'ordering': ['order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название услуги')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Прайс-лист',
                'ordering': ['order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='SiteContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_title', models.CharField(max_length=200, verbose_name='Заголовок на первом экране')),
                ('hero_subtitle', models.CharField(blank=True, max_length=255, verbose_name='Подзаголовок')),
                ('about_text', models.TextField(verbose_name='Текст блока "Обо мне"')),
                ('contact_phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('contact_email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('contact_telegram', models.CharField(blank=True, max_length=100, verbose_name='Telegram')),
                ('contact_address', models.CharField(blank=True, max_length=255, verbose_name='Адрес')),
                ('hero_image', models.ImageField(blank=True, upload_to='hero/', verbose_name='Фото для обложки')),
                ('about_image', models.ImageField(blank=True, upload_to='about/', verbose_name='Фото для блока "Обо мне"')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Контент сайта',
                'verbose_name_plural': 'Контент сайта',
            },
        ),
    ]
