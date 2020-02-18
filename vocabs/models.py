from django.db import models


class Dictionary(models.Model):
    hindi = models.CharField(max_length=200)
    english = models.CharField(max_length=200)
    attempts = models.IntegerField(default=0)
    total_attempts = models.IntegerField(default=0)
    total_false_attempts = models.IntegerField(default=0)
    source = models.CharField(max_length=50, blank=True, null=True)
    notes = models.CharField(max_length=300, blank=True, null=True)

    def get_random():
        return Dictionary.objects.filter(attempts__lt = 5).order_by("?").first()

    def increment_attempt(self):
        self.attempts += 1

    def decrement_attempts(self):
        self.attempts -= 1

    def update_total_attempts(self):
        self.total_attempts += 1

    def update_total_false_attempts(self):
        self.total_false_attempts += 1

    def __str__(self):
        return self.english


class Example(models.Model):
    vocab = models.ForeignKey(Dictionary, on_delete=models.CASCADE)
    example_text = models.CharField(max_length=300)

    def __str__(self):
        return self.example_text
