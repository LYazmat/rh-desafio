# Generated by Django 3.1.1 on 2020-10-03 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201002_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('M', 'Homem'), ('F', 'Mulher'), ('O', 'Outros')], max_length=1, verbose_name='Genero'),
        ),
    ]
