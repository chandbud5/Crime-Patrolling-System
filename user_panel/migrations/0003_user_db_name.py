# Generated by Django 3.2.9 on 2021-12-08 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0002_auto_20211208_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_db',
            name='name',
            field=models.CharField(default='', max_length=256),
        ),
    ]
