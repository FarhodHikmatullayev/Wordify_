# Generated by Django 4.2.2 on 2023-06-14 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_feedback_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subblog',
            name='title',
        ),
    ]