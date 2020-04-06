# Generated by Django 3.0.4 on 2020-03-29 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=100)),
                ('Price', models.DecimalField(decimal_places=5, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Root', models.CharField(max_length=100)),
                ('Product_name', models.CharField(max_length=100)),
                ('Price', models.DecimalField(decimal_places=5, max_digits=19)),
                ('Sale_able', models.IntegerField()),
                ('Bounce', models.IntegerField()),
                ('Sold', models.IntegerField()),
                ('Balance', models.DecimalField(decimal_places=5, max_digits=19)),
                ('Total_Balance', models.DecimalField(decimal_places=5, max_digits=19)),
            ],
        ),
    ]
