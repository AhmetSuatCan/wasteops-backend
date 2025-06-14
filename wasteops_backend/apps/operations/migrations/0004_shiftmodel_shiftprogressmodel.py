# Generated by Django 5.1.7 on 2025-05-28 00:15

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
        ('operations', '0003_userteam'),
        ('organizations', '0004_car_facility_wastecontainer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShiftModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unnamed', max_length=255)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to='organizations.organization')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to='maps.route')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to='operations.team')),
            ],
            options={
                'unique_together': {('route', 'team', 'start_time')},
            },
        ),
        migrations.CreateModel(
            name='ShiftProgressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('collected', 'Collected'), ('skipped', 'Skipped')], default='pending', max_length=20)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('route_node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shift_progress', to='maps.routenode')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress_entries', to='operations.shiftmodel')),
            ],
            options={
                'unique_together': {('shift', 'route_node')},
            },
        ),
    ]
