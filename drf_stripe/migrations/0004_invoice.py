# Generated by Django 5.0.2 on 2024-02-23 22:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drf_stripe", "0003_price_currency"),
    ]

    operations = [
        migrations.CreateModel(
            name="Invoice",
            fields=[
                (
                    "invoice_id",
                    models.CharField(max_length=256, primary_key=True, serialize=False),
                ),
                ("auto_advance", models.BooleanField(null=True)),
                ("charge", models.CharField(max_length=256, null=True)),
                (
                    "collection_method",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("currency", models.CharField(max_length=256)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "hosted_invoice_url",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("paid", models.BooleanField()),
                (
                    "stripe_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invoices",
                        to="drf_stripe.stripeuser",
                    ),
                ),
                (
                    "subscription",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invoices",
                        to="drf_stripe.subscription",
                    ),
                ),
            ],
        ),
    ]
