def date_fixer(date):
    date = date.split('/')
    date[-1] = f'20{date[-1]}'
    date = '/'.join(date)
    return date
