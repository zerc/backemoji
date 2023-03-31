from collections import Counter

from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

from .models import Choice, Feedback, Vote


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "results")

    def results(self, obj):
        counter = Counter(v.choice.get_emoji_display() for v in obj.vote_set.all())
        result = [(f"{emoji} - {count}",) for emoji, count in counter.most_common(10)]
        return format_html_join(mark_safe("<br>"), "{}", result)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("emoji", "rating", "name")


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    pass
