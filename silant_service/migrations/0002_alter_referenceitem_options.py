

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('silant_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='referenceitem',
            options={'verbose_name': 'Справочник', 'verbose_name_plural': 'Справочники'},
        ),
    ]
