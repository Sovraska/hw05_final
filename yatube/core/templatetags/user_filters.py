from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})

# Проба пера пока не трогать ВАЖНО
# @register.filter
# def add_url(post):
#     post_words = ' '.join(post.split('<br>'))
#     post_words = post_words.split(' ')
#     for index, word in enumerate(post_words):
#         if word.startswith('https://'):
#             post_words[index] = f'<a href="{word}">{word}</a>'
#     return ' '.join(post_words)
