# Generated by Django 5.1.5 on 2025-03-26 06:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sch_no', models.IntegerField()),
                ('branch', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('category', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('blood_group', models.CharField(max_length=5)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.IntegerField(max_length=10)),
                ('g_no', models.IntegerField(max_length=10)),
                ('g_name', models.CharField(max_length=100)),
                ('g_email', models.EmailField(max_length=10)),
                ('g_occupation', models.CharField(max_length=100)),
                ('g_address', models.CharField(max_length=100)),
                ('e_no', models.IntegerField(max_length=10)),
                ('l_name', models.CharField(max_length=100)),
                ('l_address', models.CharField(max_length=100)),
                ('l_no', models.IntegerField(max_length=10)),
                ('disease', models.CharField(max_length=100)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
