#!/usr/bin/env python

from django.contrib import admin
from team.models import Player

class PlayerAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Player, PlayerAdmin)
