# Generated by Django 4.2.7 on 2023-11-05 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название кафе')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес кафе')),
                ('number', models.CharField(max_length=15, verbose_name='Номер кафе')),
            ],
            options={
                'verbose_name': 'Кафе',
                'verbose_name_plural': 'Кафе',
                'ordering': ('name',),
            },
        ),
    ]
