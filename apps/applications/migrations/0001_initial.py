# Generated by Django 5.0.7 on 2024-09-12 07:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('loan_type', models.CharField(choices=[('PERSONAL_LOAN', 'Personal Loan'), ('BUSINESS_LOAN', 'Business Loan'), ('MORTGAGE', 'Mortgage'), ('STUDENT_LOAN', 'Student Loan'), ('CAR_LOAN', 'Car Loan')], max_length=32)),
                ('amount_requested', models.DecimalField(decimal_places=2, max_digits=12)),
                ('currency', models.CharField(choices=[('USD', 'US Dollar'), ('UZS', 'Uzbekistani Som'), ('EUR', 'Euro')], default='UZS', max_length=3)),
                ('application_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected'), ('UNDER_REVIEW', 'Under Review'), ('DISBURSED', 'Disbursed')], default='PENDING', max_length=20)),
                ('loan_purpose', models.TextField(blank=True, null=True)),
                ('interest_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('repayment_period_months', models.IntegerField(blank=True, null=True)),
                ('reference_number', models.CharField(max_length=128, unique=True)),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approved_applications', to=settings.AUTH_USER_MODEL)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='clients.client')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_applications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Loan Application',
                'verbose_name_plural': 'Loan Applications',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ApplicationSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('due_date', models.DateField()),
                ('installment_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('is_paid', models.BooleanField(default=False)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='applications.application')),
            ],
            options={
                'verbose_name': 'Application Schedule',
                'verbose_name_plural': 'Application Schedules',
                'ordering': ['due_date'],
            },
        ),
    ]