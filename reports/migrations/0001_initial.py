# Generated by Django 2.0.2 on 2018-03-15 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laua_code', models.CharField(max_length=10)),
                ('laua_name', models.CharField(max_length=10)),
                ('average_download_speed', models.FloatField()),
            ],
        ),
    ]