from django.urls import path

from note.views import notes_view, note_detail_view
app_name = 'note'
urlpatterns = [
    path('', notes_view),
    path('<int:pk>/', note_detail_view, name='note_detail')
]