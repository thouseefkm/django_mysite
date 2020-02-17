from django.db import models


class Dictionary(models.Model):
    hindi = models.CharField(max_length=200)
    english = models.CharField(max_length=200)
    attempts = models.IntegerField(default=0)
    total_attempts = models.IntegerField(default=0)
    cons_false_attempts = models.IntegerField(default=0)
    total_false_attempts = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    notes = models.CharField(max_length=300, blank=True, null=True)

    def get_random():
        return Dictionary.objects.filter(attempts__lt = 5).order_by("?").first()

    def increment_attempt(self):
        self.attempts += 1

    def decrement_attempts(self):
        self.attempts -= 1

    def update_total_false_attempts(self):
        self.total_false_attempts += 1

    def update_points(self):
        if self.cons_false_attempts <= 1:
            self.points += (5 - self.cons_false_attempts)
        else:
            this_point = (5 - self.cons_false_attempts)
            deductible_points = ((self.total_false_attempts - 1) * 5) if self.total_false_attempts > 0 else 0
            self.points += (deductible_points - this_point)

    def update_cons_false_attempts(self):
        self.cons_false_attempts += 1

    def update_total_attempts(self):
        self.total_attempts += 1

    def reset_cons_false_attempts(self):
        self.cons_false_attempts = 0



    def __str__(self):
        return self.english