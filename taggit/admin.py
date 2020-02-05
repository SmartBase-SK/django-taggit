from django.contrib import admin

from taggit.models import Tag, TaggedItem


class TaggedItemInline(admin.StackedInline):
    model = TaggedItem


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [TaggedItemInline]
    list_display = ["name", "slug", "language_code"]
    ordering = ["name", "slug", "language_code"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ["name"]}
