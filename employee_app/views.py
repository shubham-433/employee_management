from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Employee, Department

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'

class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'employee_form.html'
    fields = ['name', 'email', 'address', 'designation', 'reporting_manager', 'department']
    success_url = reverse_lazy('employee_app:employee-list')

    
class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employee_form.html'
    fields = ['name', 'email', 'address', 'designation', 'reporting_manager', 'department']

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_confirm_delete.html'
    success_url = reverse_lazy('employee_app:employee-list')

class DepartmentListView(ListView):
    model = Department
    template_name = 'department_list.html'
    context_object_name = 'departments'

class DepartmentCreateView(CreateView):
    model = Department
    template_name = 'department_form.html'
    fields = ['name', 'floor']

class DepartmentUpdateView(UpdateView):
    model = Department
    template_name = 'department_form.html'
    fields = ['name', 'floor']

class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'department_confirm_delete.html'
    success_url = reverse_lazy('employee_app:department-list')
