from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Project, Employee, Client, Service, Review, Partner
from .forms import ProjectForm, EmployeeForm, ClientForm, ServiceForm, ReviewForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def find_us(request):
    return render(request, 'find_us.html')

def projects(request):
    return render(request, 'projects.html')

def services(request):
    return render(request, 'services.html')



class ProjectListView(ListView):
    model = Project
    template_name = 'organization/project/project_list.html'
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'organization/project/project_detail.html'
    context_object_name = 'project'

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'organization/project/project_form.html'
    success_url = reverse_lazy('project_list')

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'organization/project/project_form.html'
    success_url = reverse_lazy('project_list')

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'organization/project/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')

class EmployeeListView(ListView):
    model = Employee
    template_name = 'organization/employee/employee_list.html'
    context_object_name = 'employees'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'organization/employee/employee_detail.html'
    context_object_name = 'employee'

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'organization/employee/employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'organization/employee/employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'organization/employee/employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')

class ClientListView(ListView):
    model = Client
    template_name = 'organization/client/client_list.html'
    context_object_name = 'clients'

class ClientDetailView(DetailView):
    model = Client
    template_name = 'organization/client/client_detail.html'
    context_object_name = 'client'

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'organization/client/client_form.html'
    success_url = reverse_lazy('client_list')

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'organization/client/client_form.html'
    success_url = reverse_lazy('client_list')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'organization/client/client_confirm_delete.html'
    success_url = reverse_lazy('client_list')

class ServiceListView(ListView):
    model = Service
    template_name = 'organization/service/service_list.html'
    context_object_name = 'services'

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'organization/service/service_detail.html'
    context_object_name = 'service'

class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'organization/service/service_form.html'
    success_url = reverse_lazy('service_list')

class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'organization/service/service_form.html'
    success_url = reverse_lazy('service_list')

class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'organization/service/service_confirm_delete.html'
    success_url = reverse_lazy('service_list')

class ReviewListView(ListView):
    model = Review
    template_name = 'organization/review/review_list.html'
    context_object_name = 'reviews'

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'organization/review/review_detail.html'
    context_object_name = 'review'

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'organization/review/review_form.html'
    success_url = reverse_lazy('review_list')

class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'organization/review/review_form.html'
    success_url = reverse_lazy('review_list')

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'organization/review/review_confirm_delete.html'
    success_url = reverse_lazy('review_list')

class PartnerListView(ListView):
    model = Partner
    template_name = 'organization/partner/partner_list.html'
    context_object_name = 'partners'