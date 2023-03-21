# Generated by Django 4.1.7 on 2023-03-21 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Truyen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('is_completed', models.BooleanField(default=False)),
                ('views', models.IntegerField(default=0)),
                ('rating', models.DecimalField(decimal_places=2, default=5, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('follow_up', models.IntegerField(default=0)),
                ('content', models.TextField(blank=True)),
                ('removed', models.BooleanField(default=False)),
                ('number_of_rating', models.IntegerField(default=0)),
                ('number_of_comment', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('truyen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='truyen.truyen')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
