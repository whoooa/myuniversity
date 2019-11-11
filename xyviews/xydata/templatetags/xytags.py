import random
from xyviews.xydata.models import University

from django import template

register = template.Library()

@register.simple_tag
def random_unis():
    count = University.objects.count()
    random_num = random.sample(range(1, count+1), 4)
    return University.objects.filter(id__in=random_num)