# Generated by Django 4.0.4 on 2022-05-16 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GOLOSOVANIE', '0008_candidate_batch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='batch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GOLOSOVANIE.batch', verbose_name='Партия'),
        ),
    ]