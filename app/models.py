"""
Definition of models.
"""

# Импорт модуля models из пакета библиотеки. В этом модуле объявлен 
# базовый класс модели Model и классы полей, предназначенных для хранения
# данных различных типов.
from django.db import models
# Модель может иметь произвольное количество полей любого типа - каждое 
# представляет столбец данных, которое сохраняется в одной из таблиц базы данных.
# Список типов полей модели, соответствующих столбцам базы данных:
#     CharField – ограниченный текст;
#     TextField – неограниченный текст;
#     EmailField – поле для Email;
#     URLField – поле для URL;
#     DateTimeField – поле дата;
#     IntegerField – поле для целочисленных значений;
#     ForeignKey, OneToOneField, ManyToManyField – поля для связи между моделями.
# Каждое поле может иметь атрибуты.

# Create your models here.
from datetime import datetime # импорт класса datetime из модуля datetime
from django.contrib import admin # импорт модуля административного раздела 
from django.core.urlresolvers import reverse # импорт метода reverse (нужно при добавлении метода get_absolute_url)
from django.contrib.auth.models import User # импорт модели User (т.к. поле автора в модели блога добавляется из связанной модели)

# Перечень использованных в моделях общих атрибутов для разных типов полей:
# db_index	        Если True, на основе этого поля будет создан индекс
# default	        Задает значение по умолчанию
# verbose_name	    Задает имя поля, которое будет отображаться на страницах административного раздела
# unique_for_date	Задает имя поля класса DateField или DateTimeField, после чего данное поле станет уникальным в пределах даты, чье значение будет взято из указанного поля


# Модель данных блога
class Blog(models.Model):
    title = models.CharField(max_length = 100, unique_for_date= "posted", verbose_name = "Заголовок") # Заголовок статьи
    description = models.TextField(verbose_name = "Краткое содержание") # Краткое содержание статьи
    content = models.TextField(verbose_name = "Полное содержание") # Полное содержание статьи
    posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Опубликована") # Дата публикации статьи блога. В поле даты значение по умолчанию равное текущей дате
    image = models.FileField(default = 'temp.jpg', verbose_name = "Путь к картинке") # Поле для основной картинки
    # Дополнительное поле для видео: можно сохранить ссылку на ролик (YouTube и др.)
    video_url = models.URLField(blank=True, null=True, verbose_name="Ссылка на видео")
    # Поле для автора в модели Blog из модели User должно иметь тип ForeignKey (так как 
    # у каждой статьи будет только один автор, но у автора может быть много статей). 
    # Подбробнее о типе ForeignKey см. в модели Comment
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")

    # Методы класса
    def get_absolute_url(self): # метод возвращает строку с уникальным интернет-адресом записи
        return reversed("blogpost", args=[str(self.id)])
    # Возвращенный URL-адрес для отображения отдельных записей модели на веб-сайте (при определении в модели этого метода Django автоматически добавит кнопку «Смотреть на сайте» в окне редактирования записей модели в разделе администратора).

    def __str__(self): # метод возвращает название, используемое для представления отдельных заголовков (записей) в административном разделе
        return self.title
    # Эта строка используется для представления отдельных записей в разделе администрирования (и в любом другом месте, где необходимо обратиться к экземпляру модели). Возвращает поле названия или имени из модели.

    # Метаданные - вложенный класс, который задает дополнительные параметры модели
    class Meta:
        db_table = "Posts" # имя таблицы для модели
        ordering = ["-posted"] # порядок сортировки данных в модели ("-" означает по убыванию)
        verbose_name = "статья блога" # имя, под которым модель будет отображаться в административном разделе (для одной статьи блога)
        verbose_name_plural = "статьи блога" # тоже, для всех статей блога

# Для редактирования данных в административном разделе необходимо зарегистрировать модель после определения класса модели.
admin.site.register(Blog) # регистрация модели блога (class Blog) в административном разделе


# Модель комментариев к статьям блога
class Comment(models.Model):
    text = models.TextField(verbose_name = "Комментарий") # Текст комментария
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Дата") # Дата добавления комментария
    # Связи между моделями задаются с помощью полей специальных классов. 
    # Например, здесь для создания связи "один ко многим" во вторичной модели (Comment)
    # необходимо добавить поле класса ForeignKey (обязательный парметр здесь - имя 
    # первичной модели; первичные модели здесь - это User и Blog):
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор") # Имя пользователя, который добавил комментарий
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = "Статья") # Статья для комментария
    # второй параметр on_delete является необязательным, указывает, что необходимо делать СУБД 
    # при удалении записи в первичной модели. В данном случае свойство CASCADE указывает,
    # что должно быть выполнено каскадное удаление записей в связанных таблицах

    # Методы класса
    def __str__(self): # метод возвращает автора комментария и название комментируемой статьи
        return 'Комментарий %s к %s' % (self.author, self.post)
    # Эта строка используется для представления отдельных записей в разделе администрирования (и в любом другом месте, где необходимо обратиться к экземпляру модели). Возвращает поле названия или имени из модели.

    # Метаданные - вложенный класс, который задает дополнительные параметры модели
    class Meta:
        db_table = "Comments" # имя таблицы для модели
        ordering = ["-date"] # порядок сортировки данных в модели ("-" означает по убыванию). Все оставленные комментарии к статье блога должны отображаться на странице с соответствующей статьей блога в порядке убывания даты.
        verbose_name = "Комментарий" # имя, под которым модель будет отображаться в административном разделе (для одного комментария)
        verbose_name_plural = "Комментарий к статьям блога" # тоже, для всех комментариев блога

# Для редактирования данных в административном разделе необходимо зарегистрировать модель после определения класса модели.
admin.site.register(Comment) # регистрация модели комментариев (class Comment) в административном разделе


# Модель отзывов (обратной связи)
class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    city = models.CharField(max_length=100, verbose_name="Город")
    job = models.CharField(max_length=100, verbose_name="Род занятий")
    gender = models.CharField(max_length=10, choices=[('1', 'Мужской'), ('2', 'Женский')], verbose_name="Пол")
    design = models.CharField(max_length=20, choices=[('1', 'Отлично'), ('2', 'Хорошо'), ('3', 'Сойдет'), ('4', 'Ужасно')], verbose_name="Оценка дизайна")
    content = models.CharField(max_length=20, choices=[('1', 'Отлично'), ('2', 'Хорошо'), ('3', 'Сойдет'), ('4', 'Ужасно')], verbose_name="Оценка контента")
    notice = models.BooleanField(default=False, verbose_name="Получать новости на e-mail")
    contact = models.BooleanField(default=False, verbose_name="Разрешаю связаться по поводу отзыва")
    email = models.EmailField(verbose_name="Адрес e-mail")
    message = models.TextField(verbose_name="Отзыв")
    date = models.DateTimeField(default=datetime.now, db_index=True, verbose_name="Дата отправки")

    def __str__(self):
        return 'Отзыв от %s (%s) - %s' % (self.name, self.email, self.date.strftime('%d.%m.%Y %H:%M'))

    class Meta:
        db_table = "Feedback"
        ordering = ["-date"]
        verbose_name = "отзыв"
        verbose_name_plural = "отзывы"

# Регистрация модели отзывов в административном разделе
admin.site.register(Feedback)


# Модель врачей
class Doctor(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="ФИО врача")
    specialty = models.CharField(max_length=200, verbose_name="Специальность")
    office = models.CharField(max_length=50, blank=True, null=True, verbose_name="Кабинет")
    work_schedule = models.CharField(max_length=200, blank=True, null=True, verbose_name="График работы")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    
    def __str__(self):
        return '%s - %s' % (self.full_name, self.specialty)
    
    class Meta:
        db_table = "Doctors"
        ordering = ["specialty", "full_name"]
        verbose_name = "врач"
        verbose_name_plural = "врачи"

# Регистрация модели врачей в административном разделе
# Теперь регистрация происходит в admin.py для лучшей настройки интерфейса
# admin.site.register(Doctor)


# Модель записей на приём к врачу
class Appointment(models.Model):
    # Временные слоты для записи
    TIME_SLOTS = [
        ('09:00', '09:00'),
        ('09:30', '09:30'),
        ('10:00', '10:00'),
        ('10:30', '10:30'),
        ('11:00', '11:00'),
        ('11:30', '11:30'),
        ('12:00', '12:00'),
        ('12:30', '12:30'),
        ('13:00', '13:00'),
        ('13:30', '13:30'),
        ('14:00', '14:00'),
        ('14:30', '14:30'),
        ('15:00', '15:00'),
        ('15:30', '15:30'),
        ('16:00', '16:00'),
        ('16:30', '16:30'),
        ('17:00', '17:00'),
    ]
    
    patient_name = models.CharField(max_length=200, verbose_name="ФИО пациента")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Врач")
    appointment_date = models.DateField(verbose_name="Дата приёма")
    appointment_time = models.CharField(max_length=5, choices=TIME_SLOTS, verbose_name="Время приёма")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(blank=True, null=True, verbose_name="E-mail")
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")
    created_at = models.DateTimeField(default=datetime.now, db_index=True, verbose_name="Дата создания записи")
    is_confirmed = models.BooleanField(default=False, verbose_name="Подтверждена")
    
    def __str__(self):
        return 'Запись: %s к %s на %s %s' % (self.patient_name, self.doctor.full_name, 
                                               self.appointment_date.strftime('%d.%m.%Y'), 
                                               self.appointment_time)
    
    class Meta:
        db_table = "Appointments"
        ordering = ["-appointment_date", "appointment_time"]
        verbose_name = "запись на приём"
        verbose_name_plural = "записи на приём"
        # Уникальность: один врач не может принимать двух пациентов одновременно
        unique_together = [['doctor', 'appointment_date', 'appointment_time']]

# Регистрация модели записей в административном разделе
# Теперь регистрация происходит в admin.py для лучшей настройки интерфейса
# admin.site.register(Appointment)