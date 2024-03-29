# Generated by Django 5.0 on 2023-12-17 03:46

import django.utils.timezone
import model_utils.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_alter_article_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={"ordering": ("-id",)},
        ),
        migrations.RemoveField(
            model_name="article",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="article",
            name="updated_at",
        ),
        migrations.AddField(
            model_name="article",
            name="created",
            field=model_utils.fields.AutoCreatedField(
                default=django.utils.timezone.now,
                editable=False,
                verbose_name="created",
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="modified",
            field=model_utils.fields.AutoLastModifiedField(
                default=django.utils.timezone.now,
                editable=False,
                verbose_name="modified",
            ),
        ),
    ]
