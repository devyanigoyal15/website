# Generated by Django 2.2 on 2019-04-08 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_auto_20190408_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='buss',
            fields=[
                ('busno', models.CharField(max_length=50)),
                ('routeno', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.DeleteModel(
            name='staff',
        ),
    ]
