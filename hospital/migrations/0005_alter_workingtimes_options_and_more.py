# Generated by Django 4.0.5 on 2022-06-24 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_remove_doctor_consultation_schedule_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workingtimes',
            options={'verbose_name': 'График', 'verbose_name_plural': 'Графики'},
        ),
        migrations.AlterField(
            model_name='doctorschedule',
            name='openning_times',
            field=models.ManyToManyField(to='hospital.workingtimes', verbose_name='рабочее время'),
        ),
        migrations.AlterField(
            model_name='workingtimes',
            name='from_weekday',
            field=models.CharField(choices=[('ПОНЕДЕЛЬНИК', 'Понедельник'), ('Вторник', 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница'), (6, 'Суббота'), (7, 'Воскресенье')], max_length=200, verbose_name='с какого дня'),
        ),
        migrations.AlterField(
            model_name='workingtimes',
            name='to_weekday',
            field=models.CharField(choices=[('ПОНЕДЕЛЬНИК', 'Понедельник'), ('Вторник', 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница'), (6, 'Суббота'), (7, 'Воскресенье')], max_length=100),
        ),
    ]
