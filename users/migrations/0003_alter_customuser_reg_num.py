# Generated by Django 3.2.8 on 2021-10-30 06:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_reg_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='reg_num',
            field=models.PositiveIntegerField(default=None, unique=True, validators=[django.core.validators.MaxValueValidator(999999999)], verbose_name='registration number'),
        ),
    ]
