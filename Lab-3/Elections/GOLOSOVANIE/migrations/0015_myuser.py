# Generated by Django 4.0 on 2022-05-23 16:24

import GOLOSOVANIE.services
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('GOLOSOVANIE', '0014_alter_candidate_preview_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('nick_name', models.CharField(max_length=30)),
                ('photo', models.ImageField(upload_to=GOLOSOVANIE.services.user_path_to_directory, verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
