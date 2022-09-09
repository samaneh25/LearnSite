from django.contrib import admin
from .models import PlanModel, UserActivePLan


@admin.register(PlanModel)
class PLanModeAdmin(admin.ModelAdmin):
    list_display = ['id', 'period', 'price', 'description']


@admin.register(UserActivePLan)
class UserActivePLanAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'plan_id', 'is_plan_active', 'remain_date']