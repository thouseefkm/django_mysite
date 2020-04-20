from django.db import models
from django.db.models import Count, Sum


ATTEMPTS = 5
class Dictionary(models.Model):
    english = models.CharField(max_length=200, unique=True)
    hindi = models.CharField(max_length=200)
    attempts = models.IntegerField(default=0)
    total_attempts = models.IntegerField(default=0)
    total_false_attempts = models.IntegerField(default=0)
    source = models.CharField(max_length=50, blank=True, null=True)
    notes = models.CharField(max_length=300, blank=True, null=True)
    last_attempt = models.CharField(max_length=50, default='First attempt')

    def get_random():
        return Dictionary.objects.filter(attempts__lt = ATTEMPTS).order_by("?").first()

    def increment_attempt(self):
        self.attempts += 1

    def decrement_attempts(self):
        self.attempts -= 1

    def update_total_attempts(self):
        self.total_attempts += 1

    def update_total_false_attempts(self):
        self.total_false_attempts += 1

    def remaining_attempts(self):
        return (ATTEMPTS - self.attempts)

    def set_last_attempt(self, value):
        self.last_attempt = value

    @staticmethod
    def find_ratio():
        each_total_attempt_count = Dictionary.objects.values('total_attempts').annotate(count=Count('total_attempts'))
        total_attempted = 0
        for value in each_total_attempt_count:
            total_attempted += (value['total_attempts'] * value['count'])
        total_false_attempts = Dictionary.objects.values('total_false_attempts').annotate(count=Count('total_false_attempts'))

        total_false_attempted = 0
        for value in total_false_attempts:
                    total_false_attempted += (value['total_false_attempts'] * value['count'])

        return {
                    'true': total_attempted - total_false_attempted,
                    'false': total_false_attempted,
               }

    @staticmethod
    def ratio_per_one():
        ratio = Dictionary.find_ratio()
        greater_value = {}
        if ratio['true'] > ratio['false']:
            greater_value['true'] = int(round(ratio['true'] / ratio['false'], 2))
        else:
            greater_value['false'] = int(round(ratio['false'] / ratio['true'], 2))

        print("Greater Value {}".format(greater_value))
        return greater_value

    @staticmethod
    def progress():
        each_attempt_count = Dictionary.objects.values('attempts').annotate(count=Count('attempts'))
        attempted = 0
        for value in each_attempt_count:
            attempted += (value['attempts'] * value['count'])
        total_available_attempts = Dictionary.objects.all().count() * ATTEMPTS
        progress = (attempted / total_available_attempts) * 100
        return round(progress, 2)


    def __str__(self):
        return self.english


class Example(models.Model):
    vocab = models.ForeignKey(Dictionary, on_delete=models.CASCADE)
    example_text = models.CharField(max_length=300)

    def __str__(self):
        return self.example_text
