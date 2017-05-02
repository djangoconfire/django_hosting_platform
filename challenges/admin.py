from django.contrib import admin

from base.admin import TimeStampedAdmin

from .models import Challenge
@admin.register(Challenge)
class ChallengeAdmin(TimeStampedAdmin):
    list_display = ("title", "start_date", "end_date", "creator", "published", "enable_forum", "anonymous_leaderboard")
    list_filter = ("creator", "published", "enable_forum", "anonymous_leaderboard")
    search_fields = ("title", "creator")