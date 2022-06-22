from django import template
from django.contrib.auth.models import User

register = template.Library()

#Цензор - ver.1
# @register.filter()
# def censor(value):
#     try:
#         tmp_str = str(value)
#         censor_dict = {
#             'Редиска': 'Р......',
#             'редиска': 'р......',
#         }
#         for i, j in censor_dict.items():
#             tmp_str = tmp_str.replace(i, j)
#         return tmp_str
#     except:
#         print('Ошибка!')

#Цензор - ver.2
@register.filter
def censor(value):
    forbidden_words = ["редиска", "сосиска"]
    words = value.split()
    result = []
    for word in words:
        if word.lower() in forbidden_words:
            result.append(word[0] + "*"*(len(word)-2) + word[-1])
        else:
            result.append(word)
    return " ".join(result)



@register.filter(name='subscribed')
def subscribed(qs, user):
    try:
        qs.get(pk=user.id)
        return True
    except User.DoesNotExist:
        return False


@register.filter(name='by_category')
def by_category(post_cat_list, category_id):
    return post_cat_list.filter(categoryLink=category_id)
