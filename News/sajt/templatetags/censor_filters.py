from django import template

register = template.Library()

STOP_WORDS = [
   'перед',
   'Чемпионат',
   'At',
   'lorem',
   'Dolor',
   'он',
]

@register.filter()
def censor(value):
   L = value.split()
   for i in STOP_WORDS:
      for j in L:
         wordi = i.lower()
         wordj = j.lower()
         if wordi == wordj:
            new_word = j[0] + '*' * (len(j) - 1)
            value = value.replace(j, new_word)

   return f'{value}'
