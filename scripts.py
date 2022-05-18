import random

from datacenter.models import Mark, Schoolkid, Lesson, Chastisement, Commendation

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def fix_marks(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.MultipleObjectsReturned:
        print("Найдено несколько учеников с таким именем")
        return
    except Schoolkid.DoesNotExist:
        print("Учеников с таким именем не обнаружено")
        return
    bad_marks = Mark.objects.filter(schoolkid=schoolkid.id, points__lt=4)
    for mark in bad_marks:
        mark.points = 5
        mark.save()
    print(f"Двойки и тройки ученика {schoolkid.full_name} исправлены на пятерки")


def remove_chastisements(schoolkid_name):
    if not schoolkid_name:
        print("Не указано имя ученика")
        return
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.MultipleObjectsReturned:
        print("Найдено несколько учеников с таким именем")
        return
    except Schoolkid.DoesNotExist:
        print("Учеников с таким именем не обнаружено, проверьте правильность написания.")
        return
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid.id)
    for chastisement in chastisements:
        chastisement.delete()
    print(f"Замечания ученика {schoolkid.full_name} удалены")


def create_commendation(schoolkid_name, subject_name):
    examples = ["Молодец!",
                "Отлично!",
                "Хорошо!",
                "Гораздо лучше, чем я ожидал!",
                "Ты меня приятно удивил!",
                "Великолепно!",
                "Прекрасно!",
                "Ты меня очень обрадовал!",
                "Именно этого я давно ждал от тебя!",
                "Сказано здорово – просто и ясно!",
                "Ты, как всегда, точен!",
                "Очень хороший ответ!",
                "Талантливо!",
                "Ты сегодня прыгнул выше головы!",
                "Я поражен!",
                "Уже существенно лучше!",
                "Потрясающе!",
                "Замечательно!",
                "Прекрасное начало!",
                "Так держать!",
                "Ты на верном пути!",
                "Здорово!",
                "Это как раз то, что нужно!",
                "Я тобой горжусь!",
                "С каждым разом у тебя получается всё лучше!",
                "Мы с тобой не зря поработали!",
                "Я вижу, как ты стараешься!",
                "Ты растешь над собой!",
                "Ты многое сделал, я это вижу!",
                "Теперь у тебя точно все получится!",]
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.MultipleObjectsReturned:
        print("Найдено несколько учеников с таким именем")
        return
    except Schoolkid.DoesNotExist:
        print("Учеников с таким именем не обнаружено, проверьте правильность написания.")
        return
    class_lessons = Lesson.objects.filter(year_of_study=schoolkid.year_of_study,
                                          group_letter=schoolkid.group_letter)
    try:
        lesson = class_lessons.get(subject__title__contains=subject_name)
    except Lesson.DoesNotExist:
        print("Предметов с данным названием не обнаружено, проверьте правильность написания.")
        return
    last_lesson = lesson.order_by("-date").first()
    Commendation.objects.create(text=random.choice(examples),
                                created=last_lesson.date,
                                schoolkid=schoolkid,
                                subject=last_lesson.subject,
                                teacher=last_lesson.teacher)
    
    print(f"Добавлена похвала для ученика {schoolkid.full_name}")
