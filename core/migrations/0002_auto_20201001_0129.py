# Generated by Django 3.1.1 on 2020-10-01 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='legal_number',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='CNPJ'),
        ),
    ]