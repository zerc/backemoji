from django.db import models
from django.urls import reverse


# Create your models here.
class Feedback(models.Model):
    name = models.CharField(unique=True, max_length=225, blank=False, null=False)
    slug = models.SlugField(blank=False, null=False)
    choices = models.ManyToManyField("Choice")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("show_feedback", kwargs={"slug": self.slug})

    def get_vote_url(self):
        return reverse(
            "register_vote", kwargs={"slug": self.slug, "choice_id": self.pk}
        )


class Choice(models.Model):
    CHOICES = list(enumerate(("😡", "😔", "😐", "🙂", "🥰")))

    name = models.CharField(unique=True, max_length=225, blank=False, null=False)
    rating = models.IntegerField(default=0, blank=False, null=False)
    emoji = models.IntegerField(choices=CHOICES, blank=False, null=False)

    def __str__(self):
        return f"{self.get_emoji_display()}"

    class Meta:
        unique_together = [("name", "rating", "emoji")]

    def get_vote_url(self):
        return reverse(
            "register_vote", kwargs={"slug": self.slug, "choice_id": self.pk}
        )


class Vote(models.Model):
    feedback = models.ForeignKey(
        "Feedback", blank=False, null=False, on_delete=models.PROTECT
    )
    choice = models.ForeignKey(
        "Choice", blank=False, null=False, on_delete=models.PROTECT
    )
    created_at = models.DateTimeField(auto_now_add=True)
