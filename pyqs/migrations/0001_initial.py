# Generated by Django 4.2.2 on 2023-10-03 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Firstyear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=50)),
                ('sub_code', models.CharField(max_length=10)),
                ('session', models.CharField(max_length=10)),
                ('sem', models.CharField(max_length=10)),
                ('midend', models.CharField(max_length=10)),
                ('pdf', models.FileField(upload_to='')),
            ],
        ),
    ]