# Generated by Django 4.1.5 on 2023-02-18 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_product_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.CharField(choices=[('Sale', 'Sale'), ('Feature', 'Feature'), ('New', 'New')], max_length=10, verbose_name='flag'),
        ),
    ]
