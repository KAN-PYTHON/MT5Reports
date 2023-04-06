def sql_finance_report(_group_mask, _start_date, _finish_date, _action):
    '''
    Выбираем сделки, которые подходят по типу, от счетов из определенных групп
    и совершены в определенное время, нумеруем и сортируем по времени совершения
    '''

    import datetime
    _start_date = datetime.datetime.now() + datetime.timedelta(days=-int(_start_date))
    _start_date = "'" + _start_date.strftime('%Y-%m-%d') + "'"
    _finish_date = datetime.datetime.now() + datetime.timedelta(days=int(_finish_date))
    _finish_date = "'" + _finish_date.strftime('%Y-%m-%d') + "'"

    return "SELECT " \
           "ROW_NUMBER() over (ORDER BY d.Time DESC) as Num, " \
           "d.Login as Login, " \
           "u.FirstName as Name, " \
           "d.Time as Time, " \
           "d.Action as Action, " \
           "d.Profit as Profit, " \
           "d.Comment as Comment " \
           "FROM mt5_deals d, mt5_users u " \
           "WHERE " \
           "d.Action in " + _action + " and " \
           "d.Time > " + _start_date + " and " \
           "d.Time < " + _finish_date + " and " \
           "d.Login = u.Login and " \
           "LOCATE('" + _group_mask + "', u.Group) > 0 " \
           "ORDER BY Time DESC "


def sql_bbook_clients_report():
    '''
    Из _all_trades (view в которой собраны закрытые и открытые сделки) группируем Profit и Volume
    для каждого счета из групп B Book
    '''
    return "SELECT " \
           "ROW_NUMBER() over (ORDER BY SUM(t.ProfitTotal) DESC ) as Num, " \
           "t.Login as Login, " \
           "u.Name as Name, " \
           "t.UserGroup as UserGroup, " \
           "COUNT(t.Login) as DealsTotal, " \
           "ROUND(SUM(t.ProfitTotal), 2) as ProfitTotal, " \
           "ROUND(SUM(t.Volume), 2) as VolumeTotal, HEX(u.Color) as Color " \
           "FROM _all_trades t, mt5_users u " \
           "WHERE LastAccess > '2023.01.01' and t.Login = u.Login and LOCATE('bbook', t.UserGroup) > 0 " \
           "and LOCATE('real', t.UserGroup) > 0 " \
           "and t.Time > '2022.12.30' " \
           "GROUP BY Login, UserGroup HAVING ProfitTotal > 0"


def sql_abook_clients_report():
    '''
    Из _all_trades (view в которой собраны закрытые и открытые сделки) группируем Profit и Volume
    для каждого счета из групп A Book
    '''
    return "SELECT " \
           "ROW_NUMBER() over (ORDER BY SUM(t.ProfitTotal)) as Num, " \
           "t.Login as Login, " \
           "u.Name as Name, " \
           "t.UserGroup as UserGroup, " \
           "COUNT(t.Login) as DealsTotal, " \
           "ROUND(SUM(t.ProfitTotal), 2) as ProfitTotal, " \
           "ROUND(SUM(t.Volume), 2) as VolumeTotal, HEX(u.Color) as Color " \
           "FROM _all_trades t, mt5_users u " \
           "WHERE t.Login = u.Login and LOCATE('abook', t.UserGroup) > 0 and t.Time > '2022.10.30' " \
           "GROUP BY Login, UserGroup HAVING ProfitTotal < 0"


def sql_allbook_clients_report():
    '''
    Из _all_trades (view в которой собраны закрытые и открытые сделки) группируем Profit и Volume
    для каждого счета из групп real

    * Фильтр по группам real нужно вставить во все запросы!!!
    '''
    return "SELECT " \
           "ROW_NUMBER() over (ORDER BY t.Login DESC ) as Num, " \
           "t.Login as Login, " \
           "u.Name as Name, " \
           "t.UserGroup as UserGroup, " \
           "COUNT(t.Login) as DealsTotal, " \
           "ROUND(SUM(t.ProfitTotal), 2) as ProfitTotal, " \
           "ROUND(SUM(t.Volume), 2) as VolumeTotal " \
           "FROM _all_trades t, mt5_users u " \
           "WHERE t.Login = u.Login and LOCATE('real', t.UserGroup) > 0 " \
           "GROUP BY Login, UserGroup"


def sql_symbols_profit(_start_date):
    '''
    Из _all_trades (view в которой собраны закрытые и открытые сделки) группируем Profit и Volume
    для каждого символа

    * Не хватает Фильтра по группам real !!!
    '''
    return "SELECT " \
           "ROW_NUMBER() over (ORDER BY SUM(t.ProfitTotal) DESC ) as Num, " \
           "t.Symbol as Symbol, " \
           "COUNT(t.Login) as DealsTotal, " \
           "ROUND(SUM(t.Storage), 2) as Storage, " \
           "ROUND(SUM(t.Commission), 2) as Commission, " \
           "ROUND(SUM(t.ProfitTotal), 2) as ProfitTotal, " \
           "ROUND(SUM(t.Volume), 2) as VolumeTotal " \
           "FROM _all_trades t " \
           "WHERE t.Time >= '" + _start_date + "' and t.Login not in (1425, 1553, 1669) GROUP BY Symbol"


def sql_abook_all_clients_report(_group_mask):
    '''
    Из таблицы mt5_users получаем данные о балансе, кредите и количестве сделок по каждому счету
    с фильтрацией по маске групп, т.е. фактически это список активных ненулевых счетов
    '''

    return "SELECT ROW_NUMBER() over (ORDER BY u.Login DESC) as Num, u.Login as Login, u.LastAccess Last, " \
           "u.Name as Name, " \
           "u.`Group` as UserGroup, u.Balance as Balance, u.Credit as Credit, COUNT(d.Login) as Deals " \
           "FROM mt5_users u, mt5_deals d " \
           "WHERE u.Login = d.Login and " \
           "LOCATE('" + _group_mask + "', u.Group) > 0 and " \
           "LOCATE('real', u.Group) > 0 " \
           "GROUP BY u.Login HAVING Deals > 0"


def sql_zero_accounts_report():
    '''
    Из таблицы mt5_users получаем список счетов по которым нет ни одной сделки,
    т.е. фактически это список нулевых (неиспользуемых) счетов
    '''
    return "SELECT ROW_NUMBER() over (ORDER BY u.Login DESC) as Num, u.Login as Login, u.LastAccess Last, " \
           "u.Name as Name, u.`Group` as UserGroup, u.Balance as Balance, u.Credit as Credit " \
           "FROM mt5_users u " \
           "LEFT JOIN mt5_deals d ON u.Login = d.Login WHERE d.Login is null and LOCATE('real', u.Group) > 0 " \
           "GROUP BY u.Login "


def sql_open_positions_report():
    '''
    Получаем количество, профит и объем открытых позиций по реальным счетам
    '''
    return "SELECT " \
           "ROW_NUMBER() over (ORDER BY u.Login DESC) as Num, " \
           "u.Login as Login, " \
           "u.Name as Name, " \
           "u.`Group` as UserGroup, " \
           "COUNT(p.Position) as DealsTotal, " \
           "ROUND(SUM(p.Profit), 2) as ProfitTotal, " \
           "ROUND(SUM(p.Volume / 10000), 2) as VolumeTotal " \
           "FROM mt5_users u, mt5_positions p " \
           "WHERE u.Login = p.Login and LOCATE('real', u.Group) > 0 " \
           "GROUP BY u.Login "


def sql_inactive_report(_group_mask, _start_date):
    '''
    Список счетов которых не было online определенное время с фильтрацией по маске групп
    '''
    import datetime

    _start_date = datetime.datetime.now() + datetime.timedelta(days=-int(_start_date))
    _start_date = "'" + _start_date.strftime('%Y-%m-%d') + "'"

    return "SELECT " \
           "ROW_NUMBER() over (ORDER BY LastAccess DESC) as Num, Login, LastAccess, Name, `Group`, " \
           "Balance, Credit " \
           "FROM mt5_users " \
           "WHERE " \
           "LastAccess < " + _start_date + " and " \
           "LOCATE('" + _group_mask + "', `Group`) > 0 "


def sql_bonus100_report(_group_mask, _start_date, _finish_date, _action):
    '''
    Список счетов которые получили бонус 100$ с фильтрацией по диапазону дат
    '''
    import datetime

    _start_date = datetime.datetime.now() + datetime.timedelta(days=-int(_start_date))
    _start_date = "'" + _start_date.strftime('%Y-%m-%d') + "'"
    _finish_date = datetime.datetime.now() + datetime.timedelta(days=int(_finish_date))
    _finish_date = "'" + _finish_date.strftime('%Y-%m-%d') + "'"

    return "SELECT " \
           "ROW_NUMBER() over (ORDER BY d.Time DESC) as Num, " \
           "d.Login as Login, " \
           "u.FirstName as Name, " \
           "d.Time as Time, " \
           "d.Action as Action, " \
           "d.Profit as Profit, " \
           "d.Comment as Comment " \
           "FROM mt5_deals d, mt5_users u " \
           "WHERE " \
           "d.Action in " + _action + " and " \
           "d.Time > " + _start_date + " and " \
           "d.Time < " + _finish_date + " and " \
           "d.Login = u.Login and " \
           "d.Profit = 100 and " \
           "LOCATE('" + _group_mask + "', u.Group) > 0 " \
                                                                                                                          "ORDER BY Time DESC "


def sql_welcome_bonus_report():
    '''
    Из _welcome_bonus (view, в которой union сделки типа deposit и credit)
    список счетов, у которых есть и deposit и credit, т.е. все кто получил бонус за депозит
    '''
    return "SELECT ROW_NUMBER() over (ORDER BY Login DESC) as Num, Login, Name, `Group`, " \
           "ROUND(SUM(Bonus), 2) as Bonus, " \
           "ROUND(SUM(Deposit), 2) as Deposit " \
           "FROM _welcome_bonus " \
           "GROUP BY Login, Name, `Group` HAVING SUM(Bonus) > 0 and SUM(Deposit) > 0 " \
           "ORDER BY Login DESC "


def sql_commission_report(_group_mask):
    '''
    Количество сделок типа buy или sell, объемы, профиты, комисии и спрэды, сгруппированные по счетам
    '''
    sql = "SELECT " \
          "ROW_NUMBER() over (ORDER BY SUM(d.Commission)) as Num, " \
          "d.Login as Login, " \

          "u.Name as Name, " \
          "u.Group as UserGroup, " \
          "COUNT(d.Login) as DealsTotal, " \
          "ROUND(SUM(d.Volume / 10000), 2) as VolumeTotal, " \
          "ROUND(SUM(d.Storage), 2) as StorageTotal, " \
          "ROUND(SUM(d.Commission), 2) as CommissionTotal, " \
          "ROUND(SUM(d.Profit), 2) as ProfitTotal " \
          "FROM mt5_deals d, mt5_users u " \
          "WHERE d.Login = u.Login and d.Action IN (0, 1) and " \

    if _group_mask == 'abook':
        sql = sql + "LOCATE('real', u.Group) > 0 and d.Gateway > '' "
    elif _group_mask == 'bbook':
        sql = sql + "LOCATE('real', u.Group) > 0 and d.Gateway = '' "

    sql = sql + "GROUP BY Login, UserGroup "
    return sql

def sql_payout_cancel():
    '''
    Список сделок с комментарием Payout
    '''
    sql = "SELECT u.Login, u.Name, d.Action, d.Profit, d.Time, d.Comment " \
          "FROM mt5_deals as d, mt5_users as u " \
          "WHERE d.Login = u.Login and Action IN (2) and " \
          "LOCATE('real', u.Group) > 0 and LOCATE('Payout', d.Comment) " \
          "ORDER BY u.Login, d.Time "
    return sql


def sql_volume_in_money():
    '''
    Отчет по объемам торговли клиентов в USD
    '''
    sql = "SELECT " \
          "ROW_NUMBER() over (ORDER BY Login) as Num, Login, ROUND(SUM(DealsTotal), 2) as DealsTotal, " \
          "ROUND(SUM(ProfitTotal), 2) as ProfitTotal, ROUND(SUM(VolumeTotalUsd), 2) as VolumeTotalUsd " \
          "FROM " \
          "(SELECT d.Login as Login, u.Name as Name, u.`Group` as UserGroup, COUNT(d.Login) as DealsTotal, " \
          "ROUND(SUM(d.Profit + d.Storage + d.Commission), 2) as ProfitTotal, " \
          "ROUND(SUM((d.VolumeExt * d.Price * d.ContractSize) / 100000000), 2) as VolumeTotalUsd " \
          "FROM mt5_real.mt5_deals d, mt5_real.mt5_users u, mt5_real.mt5_symbols s " \
          "WHERE " \
          "d.Login = u.Login and d.Symbol = s.Symbol and d.RateMargin = 1 and Action in (0,1) and " \
          "d.Time >= '2023.02.01' and d.Time < '2023.03.01' " \
          "GROUP BY d.Login, u.`Group` " \
          "UNION " \
          "SELECT " \
          "d.Login as Login, u.Name as Name, u.`Group` as UserGroup, COUNT(d.Login) as DealsTotal, " \
          "ROUND(SUM(d.Profit + d.Storage + d.Commission), 2) as ProfitTotal, " \
          "ROUND(SUM((d.VolumeExt * d.RateMargin * d.ContractSize) / 100000000), 2) as VolumeTotalUsd " \
          "FROM mt5_real.mt5_deals d, mt5_real.mt5_users u, mt5_real.mt5_symbols s " \
          "WHERE " \
          "d.Login = u.Login and d.Symbol = s.Symbol and d.RateMargin != 1 and Action in (0,1) and " \
          "d.Time >= '2023.02.01' and d.Time < '2023.03.01' " \
          "GROUP BY d.Login, u.`Group` ) AS Query " \
          "GROUP BY Login "
    return sql
