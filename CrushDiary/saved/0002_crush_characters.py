from django import migrations

def create_crushes(apps, schema_editor):
    Crush = apps.get_model('diaryapp', 'Crush')
    Crush.objects.bulk_create([
        Crush(crushName='Dante', mood='Musical'),
        Crush(crushName='Tristan', mood='Sporty'),
        Crush(crushName='Raphael', mood='Artistic'),
        Crush(crushName='Caspian', mood='Fashion'),
        Crush(crushName='Sebastian', mood='Nerdy'),

    ])

class Migration(migrations.Migration):
    dependencies = [
        ('diaryapp', 'previous_migration_name'),  # replace with your last migration
    ]

    operations = [
        migrations.RunPython(create_crushes),
    ]