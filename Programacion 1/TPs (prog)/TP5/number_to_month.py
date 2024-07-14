def number_to_month(month):
    if month == 0:
        return 'error'
    if month == 1:
        return 'enero'
    if month == 2:
        return 'febrero'
    if month == 3:
        return 'marzo'
    if month == 4:
        return 'abril'
    if month == 5:
        return 'mayo'
    if month == 6:
        return 'junio'
    if month == 7:
        return 'julio'
    elif month == 8:
        return 'agosto'
    elif month == 9:
        return 'septiembre'
    elif month == 10:
        return 'octubre'
    elif month == 11:
        return 'noviembre'
    elif month == 12:
        return 'diciembre'
    elif month >= 13:
        return 'error'
