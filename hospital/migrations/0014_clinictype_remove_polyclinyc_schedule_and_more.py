# Generated by Django 4.0.5 on 2022-06-27 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0013_remove_profile_avatar_remove_profile_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='polyclinyc',
            name='schedule',
        ),
        migrations.AddField(
            model_name='polyclinyc',
            name='workingtimes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.workingtimes'),
        ),
        migrations.DeleteModel(
            name='PolyclynicSchedule',
        ),
        migrations.AddField(
            model_name='polyclinyc',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.clinictype'),
        ),
    ]
