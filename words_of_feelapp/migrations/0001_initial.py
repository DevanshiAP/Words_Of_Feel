# Generated by Django 3.1.1 on 2020-10-10 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_first_name', models.CharField(max_length=50, verbose_name='First name')),
                ('user_last_name', models.CharField(max_length=50, verbose_name='Last name')),
                ('user_email', models.EmailField(max_length=254, verbose_name='Email')),
                ('user_password', models.CharField(max_length=50, verbose_name='Password')),
                ('user_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quote_image', models.ImageField(upload_to='images', verbose_name='Quotes Image')),
                ('Quote_caption', models.CharField(max_length=300, verbose_name='Caption')),
                ('Quote_date', models.DateTimeField(auto_now_add=True)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='words_of_feelapp.registration')),
            ],
        ),
    ]
