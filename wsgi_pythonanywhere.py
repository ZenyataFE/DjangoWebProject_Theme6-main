"""
WSGI конфигурация для PythonAnywhere
Замените содержимое файла wsgi.py в PythonAnywhere на этот код
"""

import os
import sys

# Замените 'ваш_username' на ваш username на PythonAnywhere
# Замените 'DjangoWebProject_Theme6-main' на имя вашей папки проекта
path = '/home/ваш_username/DjangoWebProject_Theme6-main'
if path not in sys.path:
    sys.path.append(path)

# Замените 'myenv' на имя вашего виртуального окружения
activate_this = '/home/ваш_username/.virtualenvs/myenv/bin/activate_this.py'
if os.path.exists(activate_this):
    with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))

os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoWebProject_Theme6.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()




