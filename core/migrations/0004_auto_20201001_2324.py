# Generated by Django 3.1.1 on 2020-10-02 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201001_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(null=True, upload_to='company/', verbose_name='Logo'),
        ),
    ]
