from django.contrib import admin
from contact.models import *

# Register your models here.


@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameter', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'parameter']
    list_editable = ['description', 'parameter']

    class Meta:
        model = GeneralSetting


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'message', 'created_date']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['name', 'email', 'subject', 'message']

    class Meta:
        model = ContactMessage


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'company', 'date_range', 'order']
    search_fields = ['title', 'company']
    list_editable = ['order']

    class Meta:
        model = Experience


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['id', 'school', 'department', 'date_range', 'order']
    search_fields = ['school', 'department']
    list_editable = ['order']

    class Meta:
        model = Education


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'percentage', 'order']
    search_fields = ['name']
    list_editable = ['percentage', 'order']

    class Meta:
        model = Skill


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'github_url', 'order']
    search_fields = ['title', 'description']
    list_editable = ['order']

    class Meta:
        model = Project


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'level', 'is_highlighted', 'order']
    search_fields = ['name']
    list_editable = ['level', 'is_highlighted', 'order']

    class Meta:
        model = Language
