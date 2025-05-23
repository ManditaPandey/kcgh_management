# Generated by Django 5.1.5 on 2025-03-18 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('sch_no', models.IntegerField()),
                ('category', models.CharField(max_length=15)),
                ('branch', models.CharField(max_length=15)),
                ('year', models.IntegerField()),
                ('number_of_days', models.IntegerField()),
                ('total_amount', models.IntegerField()),
                ('dues', models.IntegerField()),
            ],
        ),
    ]
