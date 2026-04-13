from pathlib import Path
from urllib.request import urlretrieve

from django.core.files import File
from django.core.management.base import BaseCommand

from core.models import PortfolioImage, Service, SiteContent


class Command(BaseCommand):
    help = 'Заполняет проект демо-данными и сгенерированными фото.'

    def handle(self, *args, **options):
        media_root = Path('media/generated')
        media_root.mkdir(parents=True, exist_ok=True)

        content, _ = SiteContent.objects.get_or_create(
            id=1,
            defaults={
                'hero_title': 'Светлана МАУА — визажист в вашем городе',
                'hero_subtitle': 'Вечерний, свадебный и коммерческий макияж в темной эстетике.',
                'about_text': (
                    'Я создаю выразительные образы с акцентом на естественную красоту. '
                    'Работаю на профессиональной косметике и подбираю макияж под ваш тип лица и событие.'
                ),
                'contact_phone': '+7 (900) 123-45-67',
                'contact_email': 'hello@darkmakeup.ru',
                'contact_telegram': '@darkmakeup',
                'contact_address': 'Москва, Пресненская наб., 12',
            },
        )

        img_specs = [
            ('hero.jpg', 'https://picsum.photos/seed/makeup-hero/1600/900'),
            ('about.jpg', 'https://picsum.photos/seed/makeup-about/1000/1200'),
            ('portfolio1.jpg', 'https://picsum.photos/seed/makeup-1/1200/1500'),
            ('portfolio2.jpg', 'https://picsum.photos/seed/makeup-2/1200/1500'),
            ('portfolio3.jpg', 'https://picsum.photos/seed/makeup-3/1200/1500'),
            ('portfolio4.jpg', 'https://picsum.photos/seed/makeup-4/1200/1500'),
        ]

        paths = {}
        for filename, url in img_specs:
            target = media_root / filename
            if not target.exists():
                urlretrieve(url, target)
            paths[filename] = target

        with paths['hero.jpg'].open('rb') as f:
            content.hero_image.save('hero_demo.jpg', File(f), save=False)
        with paths['about.jpg'].open('rb') as f:
            content.about_image.save('about_demo.jpg', File(f), save=False)
        content.save()

        if not Service.objects.exists():
            Service.objects.bulk_create(
                [
                    Service(title='Дневной макияж', description='Легкий образ на каждый день.', price=3500, order=1),
                    Service(title='Вечерний макияж', description='Стойкий макияж для мероприятия.', price=5000, order=2),
                    Service(title='Свадебный макияж', description='Пробный + образ в день свадьбы.', price=9000, order=3),
                    Service(title='Макияж для фотосессии', description='Под свет и камеру.', price=6500, order=4),
                ]
            )

        if not PortfolioImage.objects.exists():
            for idx in range(1, 5):
                with paths[f'portfolio{idx}.jpg'].open('rb') as f:
                    item = PortfolioImage(title=f'Образ {idx}', order=idx)
                    item.image.save(f'portfolio_{idx}.jpg', File(f), save=True)

        self.stdout.write(self.style.SUCCESS('Демо-данные добавлены.'))
