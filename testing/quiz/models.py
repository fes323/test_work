from django.db import models


class Answer(models.Model):
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    answer_list = models.ManyToManyField(
                help_text='This is a list of answers.',
                to='quiz.answer',
                verbose_name='answer list'
            )

    def __str__(self):
        return self.question_text