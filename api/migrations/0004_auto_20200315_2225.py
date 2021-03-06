# Generated by Django 3.0.4 on 2020-03-15 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200314_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='discipline',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='student',
        ),
        migrations.AddField(
            model_name='student',
            name='english',
            field=models.IntegerField(default=5, verbose_name='Английский'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='math',
            field=models.IntegerField(default=4, verbose_name='Математика'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='physic',
            field=models.IntegerField(default=3, verbose_name='Физика'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='russian',
            field=models.IntegerField(default=2, verbose_name='Русский'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Discipline',
        ),
        migrations.DeleteModel(
            name='Rate',
        ),
    ]
