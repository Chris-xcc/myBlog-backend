# Generated by Django 3.1 on 2020-08-25 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200826_0105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='to_user',
            new_name='user',
        ),
    ]
