# Generated by Django 5.0.7 on 2024-07-24 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=40)),
                ('destination', models.CharField(max_length=40)),
                ('duration', models.IntegerField()),
            ],
        ),
    ]
