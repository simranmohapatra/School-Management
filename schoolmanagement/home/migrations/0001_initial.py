# Generated by Django 4.2.7 on 2024-02-16 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='A',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phno', models.IntegerField()),
                ('pin', models.IntegerField()),
                ('address', models.CharField(max_length=10)),
            ],
        ),
    ]
