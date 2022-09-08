import datetime
from django.shortcuts import render
from .LIB.main_lib import *
from .LIB.sql_requests_lib import *


def index(request):
    context = {'title': 'MT5 Reports'}
    return render(request, 'index.html', context=context)


def bonus_report(request):
    deals = get_sql_result(sql_finance_report('', 7, 1, '(3, 6)'))
    start_date = datetime.datetime.now() + datetime.timedelta(days=-7)
    start_date = start_date.strftime('%Y-%m-%d')
    finish_date = datetime.datetime.now() + datetime.timedelta(days=1)
    finish_date = finish_date.strftime('%Y-%m-%d')
    context = {'deals': deals, 'title': 'Bonus report from ' + start_date + ' to ' + finish_date}
    return render(request, 'finance_report.html', context=context)


def deposit_report(request):
    deals = get_sql_result(sql_finance_report('', 7, 1, '(2, 4)'))
    start_date = datetime.datetime.now() + datetime.timedelta(days=-7)
    start_date = start_date.strftime('%Y-%m-%d')
    finish_date = datetime.datetime.now() + datetime.timedelta(days=1)
    finish_date = finish_date.strftime('%Y-%m-%d')
    context = {'deals': deals, 'title': 'Deposit report from ' + start_date + ' to ' + finish_date}
    return render(request, 'finance_report.html', context=context)


def correction_report(request):
    deals = get_sql_result(sql_finance_report('', 7, 1, '(5)'))
    start_date = datetime.datetime.now() + datetime.timedelta(days=-7)
    start_date = start_date.strftime('%Y-%m-%d')
    finish_date = datetime.datetime.now() + datetime.timedelta(days=1)
    finish_date = finish_date.strftime('%Y-%m-%d')
    context = {'deals': deals, 'title': 'Correction report from ' + start_date + ' to ' + finish_date}
    return render(request, 'finance_report.html', context=context)


def bbook_dangerous(request):
    deals = get_sql_result(sql_bbook_clients_report())
    context = {'deals': deals, 'title': 'BBook Dangerous clients report'}
    return render(request, 'dangerous_clients_report.html', context=context)


def abook_dangerous(request):
    deals = get_sql_result(sql_abook_clients_report())
    context = {'deals': deals, 'title': 'BBook Dangerous clients report'}
    return render(request, 'dangerous_clients_report.html', context=context)


def all_book_dangerous(request):
    deals = get_sql_result(sql_allbook_clients_report())
    context = {'deals': deals, 'title': 'BBook Dangerous clients report'}
    return render(request, 'dangerous_clients_report.html', context=context)

