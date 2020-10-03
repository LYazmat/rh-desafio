import uuid

from django.contrib.auth.models import User
from django.db import models
from crum import get_current_user


# Create your models here.

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    logo = models.ImageField('Logo', null=True, upload_to='company/', blank=True)
    name = models.CharField('Nome', max_length=100, default=None)
    legal_number = models.CharField('CNPJ', null=True, blank=True, max_length=25)

    # This is auto created and updated date
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    create_user = models.IntegerField(editable=False, null=True)
    update_user = models.IntegerField(editable=False, null=True)

    class Meta:
        verbose_name_plural = 'Companies'
        verbose_name = 'Company'

    def __str__(self):
        return ' - '.join([self.name, str(self.id)])

    # Override save() method to takes current user
    def save(self, *args, **kwargs):
        user = get_current_user()
        if not Company.objects.filter(id=self.id).exists():
            self.create_user = user.id if user else None
        self.update_user = user.id if user else None
        super(Company, self).save(*args, **kwargs)


class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    company = models.ForeignKey(Company, default=None, on_delete=models.PROTECT)
    name = models.CharField('Nome', max_length=100, default=None)
    status = models.BooleanField('Ativo', default=True, null=True)
    admin = models.ForeignKey('auth.User', default=None, on_delete=models.PROTECT)

    # This is auto created and updated date
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    create_user = models.IntegerField(editable=False, null=True)
    update_user = models.IntegerField(editable=False, null=True)

    def __str__(self):
        return ' - '.join([self.name, str(self.company.name if self.company else '')])

    # Override save() method to takes current user
    def save(self, *args, **kwargs):
        user = get_current_user()
        if not Department.objects.filter(id=self.id).exists():
            self.create_user = user.id if user else None
        self.update_user = user.id if user else None
        super(Department, self).save(*args, **kwargs)


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    department = models.ForeignKey(Department, default=None, on_delete=models.PROTECT)
    name = models.CharField('Nome', max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    GENDER = (
        ('M', 'Homem'),
        ('F', 'Mulher'),
        ('O', 'Outros')
    )
    gender = models.CharField('Genero', max_length=1, choices=GENDER)
    phone = models.CharField('Telefone/Celular', max_length=14, default='Sem Telefone')
    role = models.CharField('Função', max_length=50, default='Sem Atribuição')
    age = models.IntegerField('Idade', default=0)
    joining_date = models.DateField('Admissão', null=True)
    salary = models.DecimalField('Salário', decimal_places=2, max_digits=12, default=0)
    email = models.EmailField('E-mail', null=True, blank=True)
    # This is auto created and updated date
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    create_user = models.IntegerField(editable=False, null=True)
    update_user = models.IntegerField(editable=False, null=True)

    # Simple title return queue for django admin or auto template
    def __str__(self):
        return str(self.name)

    # Override save() method to takes current user
    def save(self, *args, **kwargs):
        user = get_current_user()
        if not Employee.objects.filter(id=self.id).exists():
            self.create_user = user.id if user else None
        self.update_user = user.id if user else None
        super(Employee, self).save(*args, **kwargs)
