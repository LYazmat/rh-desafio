# Generated by Django 3.1.1 on 2020-10-01 04:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('logo', models.ImageField(null=True, upload_to='company', verbose_name='Logo')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('legal_number', models.CharField(max_length=25, null=True, verbose_name='CNPJ')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('create_user', models.UUIDField(editable=False, null=True)),
                ('update_user', models.UUIDField(editable=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('create_user', models.UUIDField(editable=False, null=True)),
                ('update_user', models.UUIDField(editable=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Homem'), ('F', 'Mulher'), ('O', 'Outros')], max_length=1)),
                ('phone', models.CharField(default='Sem Telefone', max_length=14)),
                ('role', models.CharField(default='Sem Atribuição', max_length=50)),
                ('age', models.IntegerField(default=0)),
                ('joining_date', models.DateField(null=True)),
                ('salary', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('create_user', models.UUIDField(editable=False, null=True)),
                ('update_user', models.UUIDField(editable=False, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
