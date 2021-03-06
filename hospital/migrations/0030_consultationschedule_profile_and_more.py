# Generated by Django 4.0.5 on 2022-07-03 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0029_priyom_choicewhogo_priyom_constype'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultationschedule',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hospital.profile'),
        ),
        migrations.AlterField(
            model_name='priyom',
            name='choicewhogo',
            field=models.CharField(choices=[('ALONE', 'записати себе'), ('MY_CHILD', 'записати дитину')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='priyom',
            name='consType',
            field=models.CharField(choices=[('ONLINE', 'видеоконсльтация'), ('MYSELF', 'прийду до ликаря')], max_length=100, null=True),
        ),
    ]
