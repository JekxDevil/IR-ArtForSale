# Generated by Django 4.2.7 on 2023-11-26 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('tags', models.JSONField(default=list)),
                ('price', models.CharField(max_length=20)),
            ],
        ),
    ]
