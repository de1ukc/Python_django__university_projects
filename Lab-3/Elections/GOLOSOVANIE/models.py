from django.db import models
from .services import path_to_directory, user_path_to_directory  # какого хуя это не работает ни при Elections.GOLOSOVANIE.services ни просто from services
from django.urls import reverse
from django.contrib.auth.models import User


class StartPage(models.Model):
    img = models.ImageField(upload_to='photos/Start_Page/')
    login_img = models.ImageField(upload_to='photos/login_page/', null=True)

    class Meta:
        verbose_name = 'Стартовая страница'
        verbose_name_plural = 'Стартовая страницы'


class Candidate(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=150, verbose_name='Отчество')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    region = models.CharField(max_length=150, verbose_name='Регион')
    description = models.TextField(verbose_name='Информация')
    preview = models.ImageField(upload_to=path_to_directory, verbose_name='Фото')
    #slogan = models.ForeignKey('Slogan', on_delete=models.PROTECT, verbose_name='Слоган', null=True)
    #preview_text = models.CharField(max_length=100)
    batch = models.ForeignKey('Batch', on_delete=models.CASCADE, verbose_name='Партия', default=4, blank=True) # многие к одному, в параметры передаётся именно то, чего будет 1 штука
    slogan = models.OneToOneField('Slogan', on_delete=models.PROTECT, verbose_name='Слоган', null=True)
    support_count = models.IntegerField(default=0, verbose_name='Поддерживают')  # для прибавления к значению будет candidate.support_count = F('support_count') + 1
    creator = models.ForeignKey('MyUser', on_delete=models.CASCADE, verbose_name='Выдвиженец', null=True)

    class Meta:
        verbose_name = 'Кандидат'
        verbose_name_plural = 'Кандидаты'
        ordering = ('-date_of_birth',)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('candidate', kwargs={'pk': self.pk})


class Slogan(models.Model):
    slogan = models.CharField(max_length=150, verbose_name='Слоган')

    class Meta:
        verbose_name = 'Слоган'
        verbose_name_plural = 'Слоганы'

    def __str__(self):
        return self.slogan


class Batch(models.Model):
    name = models.CharField(max_length=150)
    political_views = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('batch', kwargs={'batch_id': self.pk})

    class Meta:
        verbose_name = 'Партия'
        verbose_name_plural = 'Партии'


class MyUser(User):
    nick_name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to=user_path_to_directory, verbose_name='Фото')
    candidates = models.ManyToManyField('Candidate', verbose_name="Кандидаты")


