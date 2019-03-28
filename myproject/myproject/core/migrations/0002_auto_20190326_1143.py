# Generated by Django 2.1.7 on 2019-03-26 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_datetime', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('url', models.CharField(max_length=128)),
                ('title_image_url', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=128)),
                ('brief_description', models.CharField(max_length=128)),
                ('content', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='KeyNews',
        ),
    ]
