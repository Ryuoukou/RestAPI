# Generated by Django 3.2.6 on 2021-08-29 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testrestapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='author',
        ),
    ]