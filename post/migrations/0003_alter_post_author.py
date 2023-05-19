# Generated by Django 4.0.6 on 2023-05-19 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0002_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(help_text='User that made the post.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
