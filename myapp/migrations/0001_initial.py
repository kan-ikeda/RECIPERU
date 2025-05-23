# Generated by Django 5.2.1 on 2025-05-12 02:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='カテゴリー名')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名前')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='メールアドレス')),
                ('message', models.TextField(blank=True, null=True, verbose_name='内容')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='タグ')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='タイトル')),
                ('image', models.ImageField(blank=True, null=True, upload_to='recipes/', verbose_name='画像')),
                ('items', models.TextField(blank=True, null=True, verbose_name='材料')),
                ('steps', models.TextField(blank=True, null=True, verbose_name='作り方')),
                ('cook_time', models.IntegerField(blank=True, null=True, verbose_name='調理時間')),
                ('created_date', models.DateTimeField(blank=True, null=True, verbose_name='作成日')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category', verbose_name='所属カテゴリー')),
                ('tags', models.ManyToManyField(related_name='所属タグ', to='myapp.tag')),
            ],
        ),
    ]
