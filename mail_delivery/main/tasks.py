#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.http import HttpResponse

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import get_connection, EmailMultiAlternatives
from django.conf import settings


@shared_task
def email_distribution_task():
    from_email = settings.EMAIL_HOST_USER
    subject = "A proper test HTML Email"
    content = "Testing sending HTML emails from Django"
    subscribers = [
        {
            "name": "Иван",
            "surname": "Иванович",
            "birthday": "11.11.1999",
            "email": "weben11201@brandoza.com"
        },
        {
            "name": "Аким",
            "surname": "Дуйшеналиев",
            "birthday": "6.7.1999",
            "email": "akimbest2012@gmail.com"
        },
        ]


    connection = get_connection(fail_silently=False)
    emails = []

    for person in subscribers:
        context ={
            "content": content,
            "name": person["name"],
            "surname": person["surname"],
            "birthday": person["birthday"],
        }
        html_content = render_to_string('send/email.html', context)
        text_content = strip_tags(html_content)
        email = (EmailMultiAlternatives(
                    subject,
                    text_content,
                    from_email,
                    [person["email"]]
                    ))
        email.attach_alternative(html_content, 'text/html')
        emails.append(email)

    connection.send_messages(emails)
    connection.close()