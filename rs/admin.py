from django.contrib import admin
from .models import Summary, Skills, WorkExperience, SocialMedia, Education, Awards

# Register your models here.

# admin.register(Summary, Skills, WorkExperience, SocialMedia, Education)
class SummaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'title','emailid')

class SkillsAdmin(admin.ModelAdmin):
    list_display = ('organisation', 'url','year')

class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('companyname','title','year', 'responsibilities')

class SocialMedialAdmin(admin.ModelAdmin):
    list_display = ('id','social', 'image_url')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('course', 'year','gpa','content')

class AwardsAdmin(admin.ModelAdmin):
    list_display = ('certificate', 'url')


admin.site.register(Summary, SummaryAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(SocialMedia, SocialMedialAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Awards, AwardsAdmin)