from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter()
def sampling_of_paired_numbers(value: list) -> list:
    if not isinstance(value, list):
        raise TypeError
    finish_list = []
    for char in value:
        if isinstance(char, int) and char % 2 == 0:
            finish_list.append(char)
    return finish_list


@register.filter()
@stringfilter
def word_counter(text):
    return text.count(' ') + 1


'''
або використати  'wordcount' готовий на який я не звернув уваги коли чітав докунтацію, яле ви вказали мні на нього за що дякую вам)
'''
