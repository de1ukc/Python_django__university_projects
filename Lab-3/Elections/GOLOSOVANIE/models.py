from django.db import models


class StartPage(models.Model):
    img = models.ImageField(upload_to='photos/Start_Page/')

    class Meta:
        verbose_name = 'Стартовая страница'
        verbose_name_plural = 'Стартовая страницы'


def path_to_directory(instance, filename):
    return 'photos/Elections/{0}/{1}/{2}'.format(instance.last_name, instance.first_name, filename)


class Candidate(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=150, verbose_name='Отчество')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    region = models.CharField(max_length=150, verbose_name='Регион')
    description = models.TextField()
    preview = models.ImageField(upload_to=path_to_directory)
    #slogan = models.ForeignKey('Slogan', on_delete=models.PROTECT, verbose_name='Слоган', null=True)
    #preview_text = models.CharField(max_length=100)
    batch = models.ForeignKey('Batch', on_delete=models.CASCADE, verbose_name='Партия', null=True, default='Самовыдвиженец') # многие к одному, в параметры передаётся именно то, чего будет 1 штука
    slogan = models.OneToOneField('Slogan', on_delete=models.PROTECT, verbose_name='Слоган', null=True)


    class Meta:
        verbose_name = 'Кандидат'
        verbose_name_plural = 'Кандидаты'
        ordering = ('-date_of_birth',)

    def __str__(self):
        return self.first_name + self.last_name


class Slogan(models.Model):
    slogan = models.CharField(max_length=150)

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

    class Meta:
        verbose_name = 'Партия'
        verbose_name_plural = 'Партии'
