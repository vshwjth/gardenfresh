# Generated by Django 4.1.3 on 2022-11-28 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productpage', '0014_remove_cart_item_cart_remove_cart_item_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_item',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='order_item',
            name='product',
        ),
        migrations.DeleteModel(
            name='order',
        ),
        migrations.DeleteModel(
            name='order_item',
        ),
    ]
