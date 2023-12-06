# Generated by Django 4.2.7 on 2023-11-11 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('sku_id', models.CharField(max_length=255, unique=True)),
                ('nums', models.IntegerField()),
                ('id_delete', models.IntegerField()),
            ],
            options={
                'db_table': 'shopping_cart1',
            },
        ),
    ]
