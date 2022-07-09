# Generated by Django 4.0.5 on 2022-06-29 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0019_consultationschedule_doctor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultationschedule',
            name='doctor',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor schedule con+', to='hospital.doctor'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='consultation_schedule',
            field=models.ManyToManyField(blank=True, null=True, related_name='consultai_schedule+', to='hospital.consultationschedule'),
        ),
    ]
