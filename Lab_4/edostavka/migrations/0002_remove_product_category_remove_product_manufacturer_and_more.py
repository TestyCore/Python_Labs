# Generated by Django 4.2.1 on 2023-06-03 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edostavka', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='manufacturer',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(help_text='Select categories for this product', to='edostavka.productcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='edostavka.manufacturer'),
        ),
    ]