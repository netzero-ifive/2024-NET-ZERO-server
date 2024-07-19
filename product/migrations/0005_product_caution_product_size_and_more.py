# Generated by Django 5.0.7 on 2024-07-19 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_materials_ko_product_nutrients_ko_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='caution',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='source_of_manufacture',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='nutrients_ko',
            field=models.JSONField(blank=True, default={'calories': '30kcal', 'detail': {'나트륨': {'amount': '0mg', 'percent': '0%'}, '단백질': {'amount': '0g', 'percent': '0%'}, '당류': {'amount': '0g', 'percent': '0%'}, '지방': {'amount': '0g', 'percent': '0%'}, '콜레스트롤': {'amount': '0mg', 'percent': '0%'}, '탄수화물': {'amount': '0g', 'percent': '0%'}, '트랜스지방': {'amount': '0g', 'percent': '0%'}, '포화지방': {'amount': '0g', 'percent': '0%'}}, 'serving_size': '100ml'}),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
