# Generated by Django 4.2.2 on 2023-06-14 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contact_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
