from django.contrib import admin
from .models import memberList

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstName", "mailId", "dateOfJoin")

admin.site.register(memberList,MemberAdmin)