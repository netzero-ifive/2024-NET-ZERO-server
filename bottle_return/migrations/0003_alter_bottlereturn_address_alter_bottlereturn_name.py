# Generated by Django 5.0.7 on 2024-07-19 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bottle_return', '0002_bottlereturn_name_alter_bottlereturn_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottlereturn',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='bottlereturn',
            name='name',
            field=models.CharField(default='페트병 반환소', max_length=100),
        ),
    ]
