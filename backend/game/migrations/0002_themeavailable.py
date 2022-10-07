# Generated by Django 4.0.1 on 2022-10-07 07:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThemeAvailable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_id', models.CharField(max_length=20)),
                ('theme_name', models.CharField(max_length=30)),
                ('theme_des', models.TextField(blank=True, null=True)),
                ('available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('theme_image', models.ImageField(null=True, upload_to='themes/images')),
            ],
        ),
    ]