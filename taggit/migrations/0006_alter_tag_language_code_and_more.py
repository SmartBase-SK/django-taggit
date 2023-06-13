from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('taggit', '0005_auto_20200204_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='language_code',
            field=models.CharField(choices=list(map(lambda cou: (cou['code'], cou['code']), settings.PARLER_LANGUAGES[1])), default=settings.LANGUAGE_CODE, max_length=255, verbose_name='Language code'),
        ),
        migrations.AlterField(
            model_name='taggeditem',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_tagged_items', to='contenttypes.contenttype', verbose_name='Content type'),
        ),
        migrations.AlterField(
            model_name='taggeditem',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_items', to='taggit.tag'),
        ),
    ]
