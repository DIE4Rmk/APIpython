# Generated by Django 4.2.2 on 2023-06-17 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tasks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('time', models.TimeField(auto_now=True)),
                ('status', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'db_table': 'tasks',
                'managed': True,
            },
        ),
    ]
