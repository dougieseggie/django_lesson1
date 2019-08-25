# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Fcuser(models.Model):
    username = models.CharField(max_length=32, verbose_name='사용자명')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    useremail = models.EmailField(max_length=128, verbose_name='사용자이메일')
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = '패스트캠퍼스 사용자'
        verbose_name_plural = '패스트캠퍼스 사용자'


"""table명 지정"""
"""verbose_name 은 실제로 어떻게 보이는지"""
"""auto_now_add 은 추가된 시간을 알아서 넣는 것"""
