# Generated by Django 4.0.5 on 2022-06-30 20:56

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cap',
            fields=[
                ('main_color', models.CharField(max_length=15)),
                ('secondary_color', models.CharField(max_length=15, null=True)),
                ('brand', models.CharField(max_length=30)),
                ('catalog_inclusion_date', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('image_url', models.URLField(unique=True)),
                ('description', models.TextField()),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('logo_color', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TShirt',
            fields=[
                ('main_color', models.CharField(max_length=15)),
                ('secondary_color', models.CharField(max_length=15, null=True)),
                ('brand', models.CharField(max_length=30)),
                ('catalog_inclusion_date', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('image_url', models.URLField(unique=True)),
                ('description', models.TextField()),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('size', models.CharField(choices=[('XXS', 'XXS'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=3)),
                ('fabric', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('MAN', 'Man'), ('WOMAN', 'Woman'), ('UNISEX', 'Unisex')], max_length=6)),
                ('sleeves', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('creation_date', models.DateField(default=django.utils.timezone.now)),
                ('caps', models.ManyToManyField(related_name='caps_by_cart', to='shoppingcart.cap')),
                ('tshirts', models.ManyToManyField(related_name='tshirts_by_cart', to='shoppingcart.tshirt')),
            ],
        ),
    ]