# Generated by Django 4.0.1 on 2022-10-07 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_alter_playedgameby_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playedgameby',
            name='users',
            field=models.CharField(max_length=180),
        ),
    ]