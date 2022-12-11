# Generated by Django 4.1.3 on 2022-11-28 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productpage', '0013_rename_custname_customer_firstname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_item',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cart_item',
            name='product',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='completed',
            new_name='placed',
        ),
        migrations.RemoveField(
            model_name='order',
            name='orderDate',
        ),
        migrations.RemoveField(
            model_name='order_item',
            name='order',
        ),
        migrations.AddField(
            model_name='order_item',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='productpage.order'),
        ),
        migrations.DeleteModel(
            name='cart',
        ),
        migrations.DeleteModel(
            name='cart_item',
        ),
    ]
