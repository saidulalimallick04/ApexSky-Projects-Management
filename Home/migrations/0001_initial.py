# Generated by Django 5.1.7 on 2025-03-31 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeroSectionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image_one', models.TextField(max_length=400)),
                ('image_two', models.TextField(max_length=400)),
                ('image_three', models.TextField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='UserFeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('time', models.TimeField(auto_now_add=True)),
                ('feedback', models.TextField(max_length=300)),
                ('status', models.CharField(default='Pending', max_length=50)),
            ],
        ),
    ]
