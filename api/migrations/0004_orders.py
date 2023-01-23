# Generated by Django 4.1.2 on 2023-01-11 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_review_carts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('order-placed', 'order-placed'), ('dispatched', 'dispatched'), ('in transit', 'in transit'), ('cancelled', 'cancelled')], default='order-placed', max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
