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


def sql_symbols_profit():
    return "SELECT " \
           "ROW_NUMBER() over (ORDER BY SUM(t.ProfitTotal) DESC ) as Num, " \
           "t.Symbol as Symbol, " \
           "COUNT(t.Login) as DealsTotal, " \
           "ROUND(SUM(t.Storage), 2) as Storage, " \
           "ROUND(SUM(t.Commission), 2) as Commission, " \
           "ROUND(SUM(t.ProfitTotal), 2) as ProfitTotal, " \
           "ROUND(SUM(t.Volume), 2) as VolumeTotal " \
           "FROM _all_trades t " \
           "GROUP BY Symbol"


def sql_abook_all_clients_report(_group_mask):
    return "SELECT ROW_NUMBER() over (ORDER BY u.Login DESC) as Num, u.Login as Login, u.LastAccess Last, " \
           "u.Name as Name, " \
           "u.`Group` as UserGroup, u.Balance as Balance, u.Credit as Credit, COUNT(d.Login) as Deals " \
           "FROM mt5_users u, mt5_deals d " \
           "WHERE u.Login = d.Login and " \
           "LOCATE('" + _group_mask + "', u.Group) > 0 and " \
           "LOCATE('real', u.Group) > 0 " \
           "GROUP BY u.Login HAVING Deals > 0"


def sql_zero_accounts_report():
    return "SELECT ROW_NUMBER() over (ORDER BY u.Login DESC) as Num, u.Login as Login, u.LastAccess Last, " \
           "u.Name as Name, u.`Group` as UserGroup, u.Balance as Balance, u.Credit as Credit " \
           "FROM mt5_users u " \
           "LEFT JOIN mt5_deals d ON u.Login = d.Login WHERE d.Login is null and LOCATE('real', u.Group) > 0 " \
           "GROUP BY u.Login "


def sql_open_positions_report():
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
    return "SELECT ROW_NUMBER() over (ORDER BY Login DESC) as Num, Login, Name, `Group`, SUM(Bonus) as Bonus, " \
           "SUM(Deposit) as Deposit " \
           "FROM _welcome_bonus " \
           "GROUP BY Login, Name, `Group` HAVING SUM(Bonus) > 0 and SUM(Deposit) > 0 " \
           "ORDER BY Login DESC "
