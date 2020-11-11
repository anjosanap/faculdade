now = 2020


def principal():
    while True:
        try:
            entrada = input()
            years = entrada.split()
            ano_valido = digit_count(years)
            bissexto, normal_years = eh_bissexto(ano_valido)
            message(years, bissexto, normal_years)
        except EOFError:
            break


def digit_count(years):
    ano_valido = []
    for year in years:
        if len(year) == 4:
            ano_valido.append(int(year))
    return ano_valido


def eh_bissexto(ano_valido):
    bissexto = []
    normal_years = []
    for year in ano_valido:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            bissexto.append(year)
        else:
            normal_years.append(year)
    return bissexto, normal_years


def message(years, bissexto, normal_years):
    for year in years:
        year = int(year)
        if year not in normal_years and year not in bissexto:
            print('Ano invalido')
        if year in bissexto:
            year_message = ''
            if year > now:
                year_message = 'serah'
            elif year == now:
                year_message = 'eh'
            else:
                year_message = 'foi'
            print(f'O ano {year} {year_message} bissexto')
        elif year in normal_years:
            print(f'O ano {year} NAO eh bissexto')


principal()
