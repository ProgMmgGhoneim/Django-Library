from django.contrib import admin

from .models import *

# Register your models here.
class BookInstanceInline(admin.TabularInline):
    model = BookInstanceModel

class BookInline(admin.TabularInline):
    model =BookModel

class BookAdmin(admin.ModelAdmin):
    list_display=('title','summary','isbn','display_genre','author','display_language')
    list_filter =('title','isbn','author')
    search_fields=('title','body')
    inlines =[BookInstanceInline]


class AutorAdmin(admin.ModelAdmin):
    list_display=('name','data_of_birth','date_of_death')
    list_filter =('name','data_of_birth','date_of_death')
    search_fields=('title','body')
    fields =['name',('data_of_birth', 'date_of_death')]
    inlines=[BookInline]

class BookInstanceAdmin(admin.ModelAdmin):
    list_display=('id','imprint','due_back', 'borrower','status','book')
    list_filter =('id','imprint','due_back','status','book')
    search_fields=('title','body')
    fieldsets = (
    (None , {'fields' : ('id' ,'imprint' ,'book') }),
    ('Availability', {'fields': ('status', 'due_back', 'borrower')}),
    )


admin.site.register(BookModel,BookAdmin)
admin.site.register(AuthorModel,AutorAdmin)
admin.site.register(BookInstanceModel,BookInstanceAdmin)
admin.site.register(GenerModel)
admin.site.register(LanguageModel)
