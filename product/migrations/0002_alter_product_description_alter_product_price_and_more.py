# Generated by Django 5.0.7 on 2024-07-19 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='qrcode',
            name='data',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='qrcode',
            name='image',
            field=models.ImageField(null=True, upload_to='qrcodes/'),
        ),
    ]