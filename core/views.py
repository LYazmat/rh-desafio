from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from .models import Company
from typing import Dict, Any
import json
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from .forms import FormCompany

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


def save_company(request, form, template_name):
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
    return save_company(request, form, 'core/company/new.html')


def edit_company(request, pk):
    c = get_object_or_404(Company, pk=pk)
    form = FormCompany(request.POST or None, request.FILES if request.method == 'POST' else None, instance=c)
    return save_company(request, form, 'core/company/edit.html')
