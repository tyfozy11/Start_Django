from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter()
def sampling_of_paired_numbers(value):
    start_list = value.split()
    finish_list = []

    for char in start_list:
        if char.isnumeric():
            if int(char) % 2 == 0:
                finish_list.append(int(char))
    return finish_list


@register.filter()
@stringfilter
def word_counter(text):
    return len(text.split(' '))
