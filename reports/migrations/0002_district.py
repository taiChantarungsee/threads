# Generated by Django 2.0.2 on 2018-03-16 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='district',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('la_code', models.CharField(max_length=8)),
                ('la_name', models.CharField(max_length=20)),
                ('average_download_speed', models.FloatField()),
            ],
        ),
    ]