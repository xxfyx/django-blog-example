# Generated by Django 2.0.2 on 2018-03-06 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmarkpost',
            name='obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post', verbose_name='Post'),
        ),
    ]