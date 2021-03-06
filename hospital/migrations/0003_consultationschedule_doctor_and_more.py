# Generated by Django 4.0.5 on 2022-06-24 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_consultationschedule_alter_doctorschedule_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultationschedule',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor schedule con+', to='hospital.doctor'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='consultation_schedule',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='consultai schedule+', to='hospital.consultationschedule'),
        ),
    ]
