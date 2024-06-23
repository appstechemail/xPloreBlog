# Generated by Django 5.0.3 on 2024-04-15 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(max_length=20)),
                ('project_name', models.CharField(max_length=100)),
                ('project_about', models.TextField()),
                ('created_by', models.CharField(max_length=100)),
                ('created_on', models.DateField()),
                ('updated_by', models.CharField(max_length=100)),
                ('updated_on', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
    ]
