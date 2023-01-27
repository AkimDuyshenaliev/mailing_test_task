#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse

from main import tasks


def call_email_distribution(request):
    tasks.email_distribution_task.delay()
    return HttpResponse(status=200, content="Email was sent successfully")
