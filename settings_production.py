"""
Настройки для production на PythonAnywhere
Скопируйте нужные изменения в ваш settings.py
"""

# В settings.py измените следующие строки:

# 1. DEBUG должен быть False в production
DEBUG = False

# 2. Добавьте ваш домен в ALLOWED_HOSTS
# Замените 'ваш_username' на ваш username
ALLOWED_HOSTS = ['ваш_username.pythonanywhere.com']

# 3. Обновите пути к статическим и медиа файлам
# Замените 'ваш_username' и путь к проекту на ваши значения
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 4. (Опционально) Использование переменных окружения для SECRET_KEY
# Это более безопасно для production
# import os
# SECRET_KEY = os.environ.get('SECRET_KEY', 'ваш_секретный_ключ')

# 5. Настройки для базы данных (оставьте SQLite или переключитесь на MySQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Для MySQL (если используете платный тариф):
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'ваш_username$dbname',
#         'USER': 'ваш_username',
#         'PASSWORD': 'ваш_пароль',
#         'HOST': 'ваш_username.mysql.pythonanywhere-services.com',
#     }
# }




