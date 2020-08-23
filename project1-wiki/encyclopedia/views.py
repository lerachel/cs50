from django.shortcuts import render

from . import util

entries = {"css", "django", "git", "html", "python"}

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def valid_entry(request, title):
    return render(request, "encyclopedia/valid_entry.html", {
        "entry": util.get_entry(title.capitalize())
    })

def not_found(request, title):
    return render(request, "encyclopedia/notfound.html")

def check(request, title):
    if title in entries:
        return valid_entry(request, title)
    else:
        return render(request, "encyclopedia/notfound.html")
