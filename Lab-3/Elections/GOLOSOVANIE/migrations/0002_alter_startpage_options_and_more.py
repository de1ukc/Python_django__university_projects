# Generated by Django 4.0.4 on 2022-05-15 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GOLOSOVANIE', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='startpage',
            options={'verbose_name': 'Стартовая страница', 'verbose_name_plural': 'Стартовая страницы'},
        ),
        migrations.RenameField(
            model_name='startpage',
            old_name='arztozka_img',
            new_name='img',
        ),
    ]