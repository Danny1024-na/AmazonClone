# Generated by Django 4.1.5 on 2023-02-19 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_product_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.CharField(choices=[('New', 'New'), ('Sale', 'Sale'), ('Feature', 'Feature')], max_length=10, verbose_name='flag'),
        ),
    ]
