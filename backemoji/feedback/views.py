from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from .models import Choice, Feedback, Vote


def show_feedback(request, slug: str):
    feedback = get_object_or_404(Feedback, slug=slug)
    if request.method == "POST" and request.POST.get("choice_id"):
        choice = get_object_or_404(Choice, pk=request.POST.get("choice_id"))
        Vote(feedback=feedback, choice=choice).save()
        return redirect("success", slug=feedback.slug)
    return render(request, "feedback/show.html", {"feedback": feedback})


def success(request, slug: str):
    feedback = get_object_or_404(Feedback, slug=slug)
    return render(request, "feedback/success.html", {"feedback": feedback})
