from django.contrib import admin
from .models import Article

# Register your models here.
# admin.site.register(Article)


# Andiamo a modificare il layout della pagina di admin per il modello Article
# Il decorator permette di aggiungere delle caratteristiche alla classe
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
    # lista di attributi che vogliamo siano visibili nella sezione Articles della pagina admin.
    # i valori che passiamo nella lista sono i campi che verranno mostrati nella tabella degli articoli nella pagina admin
    list_display = ('title', 'author', 'created')
    
    # lista di attributi per creare dei filtri nella pagina di admin
    list_filter = ('created', 'title')
    
    # lista che permette di identificare dei campi sui quali fare delle ricerche
    search_fields = ('content',)
    
    # questo permette di scegliere dei criteri di ordinamento nella pagina
    ordering = ('created', 'published')