# Generated by Django 5.0.7 on 2024-07-19 16:31

import bottle_return.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bottle_return', '0003_alter_bottlereturn_address_alter_bottlereturn_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottlereturn',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=bottle_return.models.bottle_return_image_upload_to),
        ),
    ]