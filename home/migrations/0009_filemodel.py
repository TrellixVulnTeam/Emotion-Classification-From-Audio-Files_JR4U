# Generated by Django 3.0.3 on 2020-06-06 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0008_auto_20200606_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('path', models.FilePathField(default='C:\\Users\\Priyash Gupta\\Desktop\\Emotion_Classification_Audio\\media', path='C:\\Users\\Priyash Gupta\\Desktop\\Emotion_Classification_Audio\\media')),
            ],
            options={
                'unique_together': {('file', 'path')},
            },
        ),
    ]
