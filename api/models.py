from django.db import models


class Student(models.Model):
    name = models.CharField('Полное имя', max_length=50)
    math = models.IntegerField('Математика')
    physic = models.IntegerField('Физика')
    russian = models.IntegerField('Русский')
    english = models.IntegerField('Английский')

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return str(self.name)

