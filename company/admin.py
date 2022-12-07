from django.contrib import admin
import datetime
from .models import Block, Flat


@admin.display(description='Дата окончания')
@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('number', 'price', 'entrance', 'floor', 'flat',)
    # list_display_links = ('detail',)

    # list_filter = ('name',)

    @admin.display(description='Общее количество квартир')
    def flat_all(self, obj):
        return obj.flat * obj.floor * obj.entrance
