# Generated by Django 4.2 on 2023-06-19 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('anime_list', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anime_genre', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('episode', models.FileField(upload_to='episodes/caps/')),
                ('comment', models.JSONField(default=list)),
                ('image', models.ImageField(upload_to='episode/image/')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime_list.anime')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime_genre.genre')),
                ('score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]