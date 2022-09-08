def sql_finance_report(_group_mask, _start_date, _finish_date, _action):
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
    return "SELECT " \
           "ROW_NUMBER() over (ORDER BY SUM(t.ProfitTotal) DESC ) as Num, " \
           "t.Login as Login, " \
           "u.Name as Name, " \
           "t.UserGroup as UserGroup, " \
           "COUNT(t.Login) as DealsTotal, " \
           "ROUND(SUM(t.ProfitTotal), 2) as ProfitTotal, " \
           "ROUND(SUM(t.Volume), 2) as VolumeTotal " \
           "FROM _all_trades t, mt5_users u " \
           "WHERE t.Login = u.Login and LOCATE('bbook', t.UserGroup) > 0 "\
           "GROUP BY Login, UserGroup HAVING ProfitTotal > 0"


def sql_abook_clients_report():
    return "SELECT " \
           "ROW_NUMBER() over (ORDER BY SUM(t.ProfitTotal)) as Num, " \
           "t.Login as Login, " \
           "u.Name as Name, " \
           "t.UserGroup as UserGroup, " \
           "COUNT(t.Login) as DealsTotal, " \
           "ROUND(SUM(t.ProfitTotal), 2) as ProfitTotal, " \
           "ROUND(SUM(t.Volume), 2) as VolumeTotal " \
           "FROM _all_trades t, mt5_users u " \
           "WHERE t.Login = u.Login and LOCATE('abook', t.UserGroup) > 0 "\
           "GROUP BY Login, UserGroup HAVING ProfitTotal < 0"


def sql_allbook_clients_report():
    return "SELECT " \
           "ROW_NUMBER() over (ORDER BY t.Login DESC ) as Num, " \
           "t.Login as Login, " \
           "u.Name as Name, " \
           "t.UserGroup as UserGroup, " \
           "COUNT(t.Login) as DealsTotal, " \
           "ROUND(SUM(t.ProfitTotal), 2) as ProfitTotal, " \
           "ROUND(SUM(t.Volume), 2) as VolumeTotal " \
           "FROM _all_trades t, mt5_users u " \
           "WHERE t.Login = u.Login and LOCATE('real', t.UserGroup) > 0 "\
           "GROUP BY Login, UserGroup"
