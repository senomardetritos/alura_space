from django.contrib import admin
from galeria.models import Fotografia


class ListFotografia(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'legenda', 'publicada')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 10


admin.site.register(Fotografia, ListFotografia)
