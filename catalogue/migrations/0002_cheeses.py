from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheese',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]