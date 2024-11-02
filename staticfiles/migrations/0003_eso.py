# Generated by Django 4.2.2 on 2023-10-03 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyqs', '0002_core'),
    ]

    operations = [
        migrations.CreateModel(
            name='ESO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=50)),
                ('sub_code', models.CharField(max_length=10)),
                ('dept', models.CharField(max_length=50)),
                ('session', models.CharField(max_length=10)),
                ('sem', models.CharField(max_length=10)),
                ('midend', models.CharField(max_length=10)),
                ('pdf', models.FileField(upload_to='')),
            ],
        ),
    ]
