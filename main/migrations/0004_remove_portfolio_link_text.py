# Generated by Django 4.0.5 on 2022-06-07 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_portfolio_link_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='link_text',
        ),
    ]
