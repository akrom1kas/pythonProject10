# Generated by Django 4.0.4 on 2022-04-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0021_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Status',
            field=models.CharField(blank=True, choices=[('a', 'Nupirkti'), ('p', 'Rezervuoti')], default='a', help_text='Statusas', max_length=1),
        ),
    ]
