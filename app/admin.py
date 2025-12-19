"""
Настройка административного интерфейса для моделей
"""

from django.contrib import admin
from .models import Doctor, Appointment


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели Doctor"""
    list_display = ('full_name', 'specialty', 'office', 'work_schedule', 'is_active')
    list_filter = ('specialty', 'is_active')
    search_fields = ('full_name', 'specialty', 'office')
    list_editable = ('is_active',)
    ordering = ('specialty', 'full_name')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели Appointment"""
    list_display = ('patient_name', 'doctor', 'appointment_date', 'appointment_time', 
                    'phone', 'is_confirmed', 'created_at')
    list_filter = ('doctor', 'appointment_date', 'is_confirmed', 'created_at')
    search_fields = ('patient_name', 'phone', 'email', 'doctor__full_name')
    date_hierarchy = 'appointment_date'
    list_editable = ('is_confirmed',)
    ordering = ('-appointment_date', 'appointment_time')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Информация о пациенте', {
            'fields': ('patient_name', 'phone', 'email')
        }),
        ('Детали записи', {
            'fields': ('doctor', 'appointment_date', 'appointment_time', 'is_confirmed')
        }),
        ('Дополнительно', {
            'fields': ('comment', 'created_at'),
            'classes': ('collapse',)
        }),
    )

