# Generated by Django 2.2.6 on 2019-11-25 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owned_by', models.IntegerField()),
                ('data', models.TextField()),
            ],
        ),
    ]
