# Generated by Django 4.0 on 2022-05-22 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GOLOSOVANIE', '0012_alter_candidate_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='support_count',
            field=models.IntegerField(default=0),
        ),
    ]
