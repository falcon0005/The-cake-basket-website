# Generated by Django 4.2.5 on 2023-10-23 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_shoppingcart_delete_usercake'),
    ]

    operations = [
        migrations.CreateModel(
            name='usercake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c', models.IntegerField()),
                ('u', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
