# Generated by Django 3.1.1 on 2020-10-03 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201002_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='create_user',
            field=models.IntegerField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='update_user',
            field=models.IntegerField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='create_user',
            field=models.IntegerField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='update_user',
            field=models.IntegerField(editable=False, null=True),
        ),
    ]
