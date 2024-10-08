# Generated by Django 5.0.2 on 2024-06-24 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0052_delete_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subscribed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
