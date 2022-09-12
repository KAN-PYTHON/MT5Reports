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
    # from django.db import connection
    # from .models import Mt5Users
    # # from django.conf import
    # #
    # sql = "SELECT " \
    #        "ROW_NUMBER() over (ORDER BY t.Login DESC ) as Num, " \
    #        "t.Login as Login, " \
    #        "u.Name as Name, " \
    #        "t.UserGroup as UserGroup, " \
    #        "COUNT(t.Login) as DealsTotal, " \
    #        "ROUND(SUM(t.ProfitTotal), 2) as ProfitTotal, " \
    #        "ROUND(SUM(t.Volume), 2) as VolumeTotal " \
    #        "FROM _all_trades t, mt5_users u " \
    #        "WHERE t.Login = u.Login and LOCATE('real', t.UserGroup) > 0 "\
    #        "GROUP BY Login, UserGroup"

    # with connection.cursor() as cursor:
    #     cursor.execute(sql)
    #     deals = cursor.fetchall()
    #     print('=========================================')
    #     print('=========================================')
    #     for item in deals:
    #         print(item[1])
    #         print(type(item))

    # print('=========================================')
    # print('=========================================')
    deals = get_sql_result(sql_allbook_clients_report())
    # for item in deals:
    #     print(item)
    #     print(type(item))
    # deals = get_sql_result(sql_allbook_clients_report())

    # print('=========================================')
    # print('=========================================')
    # users = Mt5Users.objects.all()
    # for item in users:
    #     print(item.firstname)
    context = {'deals': deals, 'title': 'BBook Dangerous clients report'}
    return render(request, 'dangerous_clients_report.html', context=context)


def symbols_profit(request):
    deals = get_sql_result(sql_symbols_profit())
    context = {'deals': deals, 'title': 'Symbols profit report'}
    return render(request, 'symbols_profit_report.html', context=context)


def abook_all(request):
    deals = get_sql_result(sql_abook_all_clients_report('abook'))
    context = {'deals': deals, 'title': 'A Book report All '}
    return render(request, 'all_clients_report.html', context=context)


def bbook_all(request):
    deals = get_sql_result(sql_abook_all_clients_report('bbook'))
    context = {'deals': deals, 'title': 'B Book report All '}
    return render(request, 'all_clients_report.html', context=context)


def zero_accounts(request):
    deals = get_sql_result(sql_zero_accounts_report())
    context = {'deals': deals, 'title': 'Zero accounts report '}
    return render(request, 'all_clients_report.html', context=context)


def open_positions(request):
    deals = get_sql_result(sql_open_positions_report())
    context = {'deals': deals, 'title': 'Open positions report '}
    return render(request, 'dangerous_clients_report.html', context=context)


def inactive_users(request):
    deals = get_sql_result(sql_inactive_report('real', 30))
    context = {'deals': deals, 'title': 'Inactive users report last 30 days'}
    return render(request, 'inactive_users_report.html', context=context)


def bonus100_report(request):
    deals = get_sql_result(sql_bonus100_report('real', 10000, 1, '(6)'))
    start_date = datetime.datetime.now() + datetime.timedelta(days=-10000)
    start_date = start_date.strftime('%Y-%m-%d')
    finish_date = datetime.datetime.now() + datetime.timedelta(days=1)
    finish_date = finish_date.strftime('%Y-%m-%d')
    context = {'deals': deals, 'title': 'Correction report from ' + start_date + ' to ' + finish_date}
    return render(request, 'finance_report.html', context=context)