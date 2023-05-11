# Generated by Django 4.2 on 2023-04-26 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_song_liked'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongPost',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='posts.post')),
                ('song_title', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=4)),
                ('audiofile', models.FileField(upload_to='audio/')),
            ],
            bases=('posts.post',),
        ),
        migrations.RemoveField(
            model_name='song',
            name='liked',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.CreateModel(
            name='TextPost',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='posts.post')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
            ],
            options={
                'ordering': ('-created',),
            },
            bases=('posts.post',),
        ),
        migrations.DeleteModel(
            name='PlayCount',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]
