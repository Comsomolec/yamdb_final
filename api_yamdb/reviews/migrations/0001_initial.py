# Generated by Django 3.2 on 2023-03-31 15:48

import core.validators
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.SlugField(max_length=150, unique=True, validators=[core.validators.validate_username])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(blank=True, choices=[('user', 'Пользователь'), ('admin', 'Админ'), ('moderator', 'Модератор')], default='user', max_length=12, verbose_name='роль')),
                ('bio', models.TextField(blank=True, verbose_name='биография')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='имя')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='фамилия')),
                ('confirmation_code', models.CharField(max_length=255, null=True, verbose_name='код подтверждения')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ('first_name', 'last_name'),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название', max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(help_text='URL', unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
                'abstract': False,
                'default_related_name': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название', max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(help_text='URL', unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ('name',),
                'abstract': False,
                'default_related_name': 'genres',
            },
        ),
        migrations.CreateModel(
            name='GenreTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='genre_title', to='reviews.genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Жанр-Произведение',
                'verbose_name_plural': 'Жанры-Произведения',
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название произведения', max_length=256, verbose_name='Название произведения')),
                ('year', models.PositiveSmallIntegerField(db_index=True, help_text='Год выпуска произведения', validators=[core.validators.validate_year], verbose_name='Год выпуска произведения')),
                ('description', models.TextField(blank=True, help_text='Описание произведения', null=True, verbose_name='Описание произведения')),
                ('category', models.ForeignKey(help_text='Категория, к которой будет относиться произведение', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='title', to='reviews.category', verbose_name='Категория')),
                ('genre', models.ManyToManyField(related_name='title', through='reviews.GenreTitle', to='reviews.Genre', verbose_name='Жанры')),
            ],
            options={
                'verbose_name': 'Произведение',
                'verbose_name_plural': 'Произведения',
                'ordering': ('-year', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('text', models.TextField(verbose_name='Текст')),
                ('score', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Оценка')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='reviews.title', verbose_name='Произведение')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ('-pub_date',),
                'abstract': False,
                'default_related_name': 'reviews',
            },
        ),
        migrations.AddField(
            model_name='genretitle',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genre_title', to='reviews.title', verbose_name='Произведение'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('text', models.TextField(verbose_name='Текст')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reviews.review', verbose_name='Отзыв')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ('-pub_date',),
                'abstract': False,
                'default_related_name': 'comments',
            },
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('title', 'author'), name='unique_author_title'),
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('username', 'email'), name='unique_username_email'),
        ),
    ]
