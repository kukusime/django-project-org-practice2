from django.db import models

MAX_LENGTH = 255


class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование категории')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Client(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название компании')
    contact_person = models.CharField(max_length=MAX_LENGTH, verbose_name='Контактное лицо')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    logo = models.ImageField(upload_to='clients/%Y/%m/%d', null=True, blank=True, verbose_name='Логотип')
    is_active = models.BooleanField(default=True, verbose_name='Активный')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Position(models.Model):
    title = models.CharField(max_length=MAX_LENGTH, verbose_name='Должность')
    salary = models.FloatField(verbose_name='Оклад')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Employee(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    position = models.ForeignKey(Position, on_delete=models.PROTECT, verbose_name='Должность')
    photo = models.ImageField(upload_to='employees/%Y/%m/%d', null=True, blank=True, verbose_name='Фото')
    email = models.EmailField(verbose_name='Email')
    hire_date = models.DateField(verbose_name='Дата приёма')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Project(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название проекта')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    client = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name='Клиент')
    employees = models.ManyToManyField(Employee, blank=True, verbose_name='Сотрудники')
    photo = models.ImageField(upload_to='projects/%Y/%m/%d', null=True, blank=True, verbose_name='Фото')
    start_date = models.DateField(verbose_name='Дата начала')
    budget = models.FloatField(verbose_name='Бюджет')
    is_completed = models.BooleanField(default=False, verbose_name='Завершён')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Service(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование услуги')
    description = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Review(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    text = models.TextField(verbose_name='Текст отзыва')
    rating = models.PositiveIntegerField(default=5, verbose_name='Оценка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return f'Отзыв от {self.client.name}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Partner(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название партнёра')
    logo = models.ImageField(upload_to='partners/%Y/%m/%d', null=True, blank=True, verbose_name='Логотип')
    website = models.URLField(blank=True, verbose_name='Сайт')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры'