# -*- coding: utf-8 -*-
"""
Скрипт для создания суперпользователя Django
"""
import os
import sys
import django

# Настройка кодировки для Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoWebProject_Theme6.settings')
django.setup()

from django.contrib.auth.models import User

# Данные для суперпользователя
USERNAME = 'admin'
EMAIL = 'admin@ostrovmb.ru'
PASSWORD = 'admin123'  # Измените на свой пароль!

# Проверяем, существует ли уже пользователь
user, created = User.objects.get_or_create(username=USERNAME)

if created:
    # Создаём суперпользователя
    user.email = EMAIL
    user.set_password(PASSWORD)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    print('SUCCESS: Суперпользователь "{}" успешно создан!'.format(USERNAME))
    print('  Email: {}'.format(EMAIL))
    print('  Пароль: {}'.format(PASSWORD))
else:
    # Обновляем пароль существующего пользователя
    user.set_password(PASSWORD)
    user.email = EMAIL
    user.is_superuser = True
    user.is_staff = True
    user.save()
    print('SUCCESS: Пароль для пользователя "{}" обновлен!'.format(USERNAME))
    print('  Email: {}'.format(EMAIL))
    print('  Пароль: {}'.format(PASSWORD))

print('')
print('ВАЖНО: Измените пароль после первого входа!')
print('')
print('Доступ:')
print('  - Сайт: http://127.0.0.1:8000/login/')
print('  - Админ-панель: http://127.0.0.1:8000/admin/')




