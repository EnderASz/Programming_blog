# Generated by Django 2.2.7 on 2019-12-10 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors_manager', '__first__'),
        ('tags_manager', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_title', models.CharField(max_length=35, unique=True)),
                ('post_slug', models.SlugField(max_length=40, unique=True)),
                ('post_image', models.ImageField(default='assets/img/bitmap/no_image.png', upload_to='assets/posts_content/images/thumbnails/')),
                ('post_content', models.TextField()),
                ('date_add', models.DateField(auto_now_add=True)),
                ('post_excerpt', models.CharField(max_length=300)),
                ('authors', models.ManyToManyField(to='authors_manager.Author')),
                ('tags', models.ManyToManyField(to='tags_manager.Tag')),
            ],
        ),
    ]
