# Generated by Django 2.1.4 on 2020-04-21 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_remove_user_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
