# Generated by Django 4.1.7 on 2023-03-21 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truyen', '0004_alter_rate_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truyen',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
