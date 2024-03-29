# Generated by Django 3.1.2 on 2021-09-16 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('link', models.TextField()),
                ('description', models.TextField()),
                ('creator', models.TextField()),
                ('publication_date', models.CharField(max_length=255)),
                ('media_url', models.TextField()),
                ('media_description', models.TextField()),
                ('media_credit', models.TextField()),
                ('categories', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MasterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=255)),
            ],
        ),
    ]
