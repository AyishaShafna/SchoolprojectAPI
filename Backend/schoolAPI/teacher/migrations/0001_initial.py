# Generated by Django 4.1.7 on 2023-03-03 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.BigIntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=200)),
                ('phone', models.BigIntegerField()),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
