#coding:utf-8

from ..models import *
from django import template
from django.db.models.aggregates import Count

register=template.Library()


@register.simple_tag
def get_recent_posts(num=4):
    return Post.objects.all().order_by('?')[:num]

@register.simple_tag
def get_all_posts():
    return Post.objects.all()

@register.simple_tag
def archives():
    return Post.objects.dates('create_time','month','DESC')

@register.simple_tag
def get_categories():
    return Category.objects.annotate(post_num=Count("post")).filter(post_num__gt=0) #返回一个分类对象,__gt代表最小值，即此处意为大于0

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(post_num=Count("post")).filter(post_num__gt=0)  #返回多个标签对象

