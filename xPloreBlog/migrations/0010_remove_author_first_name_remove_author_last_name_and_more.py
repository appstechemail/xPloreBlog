# Generated by Django 5.0.3 on 2024-04-19 04:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xPloreBlog', '0009_remove_reply_rating'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
        migrations.AddField(
            model_name='author',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ruser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='xPloreBlog.author'),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='reader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cuser', to='xPloreBlog.author'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ruser', to='xPloreBlog.author'),
        ),
    ]
