# Generated by Django 5.0.7 on 2024-07-19 09:49

import django.db.models.deletion
import product.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_description_alter_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='image',
            field=models.ImageField(null=True, upload_to=product.models.qrcode_image_upload_to),
        ),
        migrations.CreateModel(
            name='Allergen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('POULTRY', '난류'), ('MILK', '우유'), ('BUCKWHEAT', '메밀'), ('PEANUT', '땅콩'), ('SOYBEAN', '대두'), ('WHEAT', '밀'), ('MACKEREL', '고등어'), ('CRAB', '게'), ('SHRIMP', '새우'), ('PORK', '돼지고기'), ('PEACH', '복숭아'), ('TOMATO', '토마토'), ('SULFITE', '아황산류'), ('WALNUT', '호두'), ('CHICKEN', '닭고기'), ('BEEF', '쇠고기'), ('SQUID', '오징어'), ('SHELLFISH', '조개류')], max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
