from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from .models import Company, Department, Employee
from typing import Dict, Any
import json
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from .forms import FormCompany, FormDepartment, FormEmployee

# Create your views here.


def home(request):
    return render(request, 'base.html', {})


def test(request):
    return render(request, 'core/user_form.html', {})


def company(request):
    return render(request, 'core/company/company.html', {})


def data_company(request):
    companies = Company.objects.all()
    # Serialize companies before sending to template table
    result = [serialize_company(c) for c in companies]
    return HttpResponse(json.dumps(result, default=str))


def serialize_company(c: Company) -> Dict[str, Any]:
    return {
        'id': c.id,
        'name': c.name,
        'legal_number': c.legal_number
    }


def save(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request)
    return JsonResponse(data)


def create_company(request):
    if request.method == 'POST':
        form = FormCompany(request.POST, request.FILES)
    else:
        form = FormCompany()
    return save(request, form, 'core/company/new.html')


def edit_company(request, pk):
    c = get_object_or_404(Company, pk=pk)
    form = FormCompany(request.POST or None, request.FILES if request.method == 'POST' else None, instance=c)
    return save(request, form, 'core/company/edit.html')


def delete_company(request, pk):
    c = get_object_or_404(Company, pk=pk)
    data = dict()
    try:
        c.delete()
    except Exception:
        data['html_alert'] = 'Não foi possível remover o registro.'
    return JsonResponse(data)


def department(request):
    return render(request, 'core/department/department.html', {})


def data_department(request):
    departments = Department.objects.all()
    # Serialize companies before sending to template table
    result = [serialize_department(d) for d in departments]
    return HttpResponse(json.dumps(result, default=str))


def serialize_department(d: Department) -> Dict[str, Any]:
    return {
        'id': d.id,
        'name': d.name,
        'status': d.status,
        'admin': ' '.join([d.admin.first_name, d.admin.last_name]) if d.admin else ''
    }


def create_department(request):
    if request.method == 'POST':
        form = FormDepartment(request.POST, request.FILES)
    else:
        form = FormDepartment()
    return save(request, form, 'core/department/new.html')


def edit_department(request, pk):
    d = get_object_or_404(Department, pk=pk)
    form = FormDepartment(request.POST or None, instance=d)
    return save(request, form, 'core/department/edit.html')


def delete_department(request, pk):
    d = get_object_or_404(Department, pk=pk)
    data = dict()
    try:
        d.delete()
    except Exception:
        data['html_alert'] = 'Não foi possível remover o registro.'
    return JsonResponse(data)


def logo_company(request, pk):
    c = get_object_or_404(Company, pk=pk)
    return JsonResponse({'url': c.logo.url if c.logo else None})


def employee(request):
    return render(request, 'core/employee/employee.html', {})


def data_employee(request):
    employees = Employee.objects.all()
    # Serialize companies before sending to template table
    result = [serialize_employee(e) for e in employees]
    return HttpResponse(json.dumps(result, default=str))


def serialize_employee(e: Employee) -> Dict[str, Any]:
    return {
        'id': e.id,
        'name': e.name,
        'gender': e.gender,
        'role': e.role,
        'department': e.department.name,
        'company': e.department.company.name
    }


def create_employee(request):
    if request.method == 'POST':
        form = FormEmployee(request.POST, request.FILES)
    else:
        form = FormEmployee()
    return save(request, form, 'core/employee/new.html')


def edit_employee(request, pk):
    e = get_object_or_404(Employee, pk=pk)
    form = FormEmployee(request.POST or None, instance=e)
    return save(request, form, 'core/employee/edit.html')


def delete_employee(request, pk):
    e = get_object_or_404(Employee, pk=pk)
    data = dict()
    try:
        e.delete()
    except Exception:
        data['html_alert'] = 'Não foi possível remover o registro.'
    return JsonResponse(data)


def logo_department(request, pk):
    d = get_object_or_404(Department, pk=pk)
    return JsonResponse({'url': d.company.logo.url if d.company.logo else None})
