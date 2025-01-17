# Generated by Django 4.0.1 on 2022-02-08 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drf_stripe", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feature",
            name="description",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name="price",
            name="freq",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name="price",
            name="nickname",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="cancel_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="ended_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="period_end",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="period_start",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="trial_end",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="trial_start",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
