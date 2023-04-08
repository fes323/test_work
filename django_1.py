from django.db import migrations, models


def copy_answer_to_answer_list(apps, schema_editor):
    Question = apps.get_model('quiz', 'Question')
    for question in Question.objects.all():
        question.answer_list.add(question.answer)


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer_list',
            field=models.ManyToManyField(help_text='This is a list of answers.',
                                         to='quiz.answer',
                                         verbose_name='answer list'),
        ),
        migrations.RunPython(copy_answer_to_answer_list),
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
    ]