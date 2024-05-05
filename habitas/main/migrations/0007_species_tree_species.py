# Generated by Django 4.1.2 on 2023-11-27 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_post_specialized_tree_plantado_por'),
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('bio_index', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='tree',
            name='species',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.species'),
        ),
    ]