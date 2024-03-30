from django.contrib import admin
from .models import *


# admin.site.register(Muallif)
@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'jins', 't_sana', 'kitob_soni', 'tirik')
    list_editable = ('tirik', 'kitob_soni')
    list_display_links = ( 'id', 'ism' )
    search_fields = ('ism', 'id', 't_sana' )
    search_help_text = ("Id, ism va sanasi bo'yicha qidirish")
    # list_filter = ('trik', 'jins')
    ordering = ('ism', 't_sana')
    date_hierarchy = 't_sana'
    list_per_page = 3

# @admin.register(Kitob)
# class KitobAdmin(admin.ModelAdmin):
#     # list_display = ('nom', 'janr', 'sahifa', 'muallif')
#     list_editable = ('sahifa', )
#     # list_display_links = ()
#     search_fields = ('nom', 'janr' )
#     autocomplete_fields = ('muallif',)

# admin.site.unregister(User)
# admin.site.unregister(Group)


admin.site.register(Talaba)
admin.site.register(Kitob)
admin.site.register(Kutubxonachi)
admin.site.register(Record)

