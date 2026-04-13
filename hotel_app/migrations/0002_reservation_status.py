from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='Status',
            field=models.CharField(
                max_length=20,
                default='Pending',
                choices=[
                    ('Pending', 'Pending'),
                    ('Confirmed', 'Confirmed'),
                    ('Checked In', 'Checked In'),
                    ('Checked Out', 'Checked Out'),
                    ('Cancelled', 'Cancelled'),
                ]
            ),
        ),
        migrations.AddField(
            model_name='reservation',
            name='Cancelled_At',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='Cancel_Reason',
            field=models.TextField(null=True, blank=True),
        ),
    ]