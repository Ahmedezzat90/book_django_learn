# Generated by Django 4.2.4 on 2023-08-22 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_lab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='publishing_house',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('relation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='book_lab.book')),
            ],
        ),
    ]
