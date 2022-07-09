# Generated by Django 4.0.5 on 2022-06-29 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0014_clinictype_remove_polyclinyc_schedule_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='consultation_schedule',
        ),
        migrations.AddField(
            model_name='doctor',
            name='consultation_schedule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consultai_schedule+', to='hospital.consultationschedule'),
        ),
    ]