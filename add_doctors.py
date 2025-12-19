"""
Скрипт для добавления врачей в базу данных
Запустите: python add_doctors.py
"""

import os
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoWebProject_Theme6.settings')
django.setup()

from app.models import Doctor

# Список врачей для добавления
doctors_data = [
    {
        'full_name': 'Иванов Иван Иванович',
        'specialty': 'Терапевт',
        'office': '101',
        'work_schedule': 'Пн-Пт: 09:00-17:00',
        'is_active': True
    },
    {
        'full_name': 'Петрова Мария Сергеевна',
        'specialty': 'Педиатр',
        'office': '205',
        'work_schedule': 'Пн-Ср, Пт: 08:00-16:00',
        'is_active': True
    },
    {
        'full_name': 'Сидоров Петр Александрович',
        'specialty': 'Хирург',
        'office': '310',
        'work_schedule': 'Вт-Чт: 10:00-18:00',
        'is_active': True
    },
    {
        'full_name': 'Козлова Анна Владимировна',
        'specialty': 'Кардиолог',
        'office': '215',
        'work_schedule': 'Пн, Ср, Пт: 09:00-15:00',
        'is_active': True
    },
    {
        'full_name': 'Морозов Дмитрий Николаевич',
        'specialty': 'Невролог',
        'office': '420',
        'work_schedule': 'Вт-Пт: 09:00-17:00',
        'is_active': True
    },
    {
        'full_name': 'Волкова Елена Петровна',
        'specialty': 'Офтальмолог',
        'office': '118',
        'work_schedule': 'Пн-Чт: 08:00-16:00',
        'is_active': True
    },
    {
        'full_name': 'Лебедев Сергей Викторович',
        'specialty': 'Отоларинголог',
        'office': '225',
        'work_schedule': 'Пн, Ср, Пт: 10:00-18:00',
        'is_active': True
    },
    {
        'full_name': 'Соколова Ольга Михайловна',
        'specialty': 'Гинеколог',
        'office': '305',
        'work_schedule': 'Вт-Пт: 09:00-17:00',
        'is_active': True
    },
]

def add_doctors():
    """Добавляет врачей в базу данных"""
    added_count = 0
    skipped_count = 0
    
    for doctor_data in doctors_data:
        # Проверяем, существует ли уже такой врач
        doctor, created = Doctor.objects.get_or_create(
            full_name=doctor_data['full_name'],
            defaults=doctor_data
        )
        
        if created:
            print(f"[+] Добавлен врач: {doctor.full_name} - {doctor.specialty}")
            added_count += 1
        else:
            print(f"[=] Врач уже существует: {doctor.full_name} - {doctor.specialty}")
            skipped_count += 1
    
    print(f"\nИтого: добавлено {added_count}, пропущено {skipped_count}")

if __name__ == '__main__':
    add_doctors()

