# Generated by Django 2.0.4 on 2018-04-24 15:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('data_of_birth', models.DateTimeField(blank=True, null=True)),
                ('date_of_death', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookInstanceModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='m', help_text='Book availability', max_length=1)),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.CharField(help_text='Enter a brief description of the book', max_length=2000)),
                ('isbn', models.CharField(help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, verbose_name='ISBN')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.AuthorModel')),
            ],
        ),
        migrations.CreateModel(
            name='GenerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this book', to='catalog.GenerModel'),
        ),
        migrations.AddField(
            model_name='bookinstancemodel',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.BookModel'),
        ),
    ]