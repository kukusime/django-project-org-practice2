from django.urls import path
from . import views

urlpatterns = [
    # Старые страницы
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('about/contacts/', views.contacts, name='contacts'),
    path('about/find-us/', views.find_us, name='find_us'),
    path('projects/', views.projects, name='projects'),
    path('services/', views.services, name='services'),

    # Проекты
    path('project-list/', views.ProjectListView.as_view(), name='project_list'),
    path('project-list/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('project-list/create/', views.ProjectCreateView.as_view(), name='project_create'),
    path('project-list/<int:pk>/update/', views.ProjectUpdateView.as_view(), name='project_update'),
    path('project-list/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),

    # Сотрудники
    path('employee-list/', views.EmployeeListView.as_view(), name='employee_list'),
    path('employee-list/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('employee-list/create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('employee-list/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee-list/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),

    # Клиенты
    path('client-list/', views.ClientListView.as_view(), name='client_list'),
    path('client-list/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
    path('client-list/create/', views.ClientCreateView.as_view(), name='client_create'),
    path('client-list/<int:pk>/update/', views.ClientUpdateView.as_view(), name='client_update'),
    path('client-list/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='client_delete'),

    # Услуги
    path('service-list/', views.ServiceListView.as_view(), name='service_list'),
    path('service-list/<int:pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('service-list/create/', views.ServiceCreateView.as_view(), name='service_create'),
    path('service-list/<int:pk>/update/', views.ServiceUpdateView.as_view(), name='service_update'),
    path('service-list/<int:pk>/delete/', views.ServiceDeleteView.as_view(), name='service_delete'),

    # Отзывы
    path('review-list/', views.ReviewListView.as_view(), name='review_list'),
    path('review-list/<int:pk>/', views.ReviewDetailView.as_view(), name='review_detail'),
    path('review-list/create/', views.ReviewCreateView.as_view(), name='review_create'),
    path('review-list/<int:pk>/update/', views.ReviewUpdateView.as_view(), name='review_update'),
    path('review-list/<int:pk>/delete/', views.ReviewDeleteView.as_view(), name='review_delete'),

    # Партнёры
    path('partner-list/', views.PartnerListView.as_view(), name='partner_list'),
]