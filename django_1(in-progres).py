from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.AddField(
            model_name='question',
            name='answer_list',
            field=models.ManyToManyField(
                help_text='This is a list of answers.',
                to='quiz.answer',
                verbose_name='answer list'
            ),
        ),
    ]