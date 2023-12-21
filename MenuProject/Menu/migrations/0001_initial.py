# Generated by Django 4.2.6 on 2023-12-21 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('another_menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Menu', to='Menu.modelmenu', verbose_name='Меню на странице')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='Menu.modelmenu', verbose_name='Родительское меню')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
    ]
