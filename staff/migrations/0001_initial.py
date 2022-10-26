# Generated by Django 4.1.2 on 2022-10-23 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='ФИО')),
                ('position', models.CharField(blank=True, max_length=50, null=True, verbose_name='Должность')),
                ('employment_date', models.DateField(null=True, verbose_name='Дата приема на работу')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Размер заработной платы')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='staff.staff')),
            ],
            options={
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]