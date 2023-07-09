from django.shortcuts import render, get_object_or_404

from note.models import Note


def notes_view(request, *args, **kwargs):
    return render(request, 'all_notes.html', {'notes': Note.objects.all()})


def note_detail_view(request, pk, *args, **kwargs):
    return render(request, 'note.html', {'note': get_object_or_404(Note, pk=pk)})
