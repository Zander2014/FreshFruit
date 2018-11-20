#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 14:26
# @Author  : Zander
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.mycart),
    url(r'^add(\d+)_(\d+)/$', views.add),
    url(r'^edit(\d+)_(\d+)/$', views.edit),
    url(r'^delete(\d+)/$', views.delete),
]
