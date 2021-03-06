# Generated by Django 2.1.4 on 2018-12-29 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("invoices", "0004_auto_20181229_1114")]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="recipient_address",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="invoices.Address",
                verbose_name="Recipient Address",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="invoice",
            name="recipient_first_name",
            field=models.CharField(
                blank=True, max_length=100, verbose_name="Recipient first name"
            ),
        ),
        migrations.AddField(
            model_name="invoice",
            name="recipient_last_name",
            field=models.CharField(
                blank=True, max_length=100, verbose_name="Recipient last name"
            ),
        ),
        migrations.AddField(
            model_name="invoice",
            name="recipient_tax_code",
            field=models.CharField(
                blank=True, max_length=16, verbose_name="Tax code"
            ),
        ),
    ]
