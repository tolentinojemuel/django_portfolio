# Generated by Django 4.0.5 on 2022-06-07 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_certificate_cv_cert'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='link_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
