# Generated by Django 2.1 on 2018-09-13 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slugatricle', models.SlugField()),
                ('body', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('pic', models.ImageField(default='default.png', upload_to='')),
                ('genre', models.CharField(choices=[('Rock', 'Rock'), ('Indie', 'Indie'), ('Metal', 'Metal'), ('Other', 'Other')], default='Other', max_length=5)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]