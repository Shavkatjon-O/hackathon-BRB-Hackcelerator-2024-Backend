# Generated by Django 5.0.7 on 2024-08-30 06:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('request_type', models.CharField(choices=[('LEAVE', 'Leave'), ('EXPENSE', 'Expense'), ('TRAVEL', 'Travel'), ('ABSENCE', 'Absence'), ('MEETING_ROOM_BOOKING', 'Meeting Room Booking'), ('PROJECT_EXTENSION', 'Project Extension'), ('OVERTIME', 'Overtime'), ('WORK_FROM_HOME', 'Work From Home'), ('TRAINING', 'Training'), ('SHIFT_CHANGE', 'Shift Change'), ('EQUIPMENT', 'Equipment'), ('SICK_LEAVE', 'Sick Leave')], default='LEAVE', max_length=50)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')], default='PENDING', max_length=50)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]