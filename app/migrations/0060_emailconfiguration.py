# Generated by Django 5.0.4 on 2024-07-16 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0059_doms'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_host_user', models.CharField(max_length=255)),
                ('email_host_password', models.CharField(max_length=255)),
                ('default_from_email', models.CharField(max_length=255)),
            ],
        ),
    ]
