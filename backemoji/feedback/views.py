from django.shortcuts import render


def show_feedback(request, slug: str):
    return render(request, "feedback/show.html", {"feedback": slug})
