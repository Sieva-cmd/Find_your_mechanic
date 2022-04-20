# Generated by Django 4.0.3 on 2022-04-20 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yourMechanic', '0003_alter_fullbodypaint_mechanic_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EngineRepair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='enginerepair', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
