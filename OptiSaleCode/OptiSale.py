import datetime
from fpdf import FPDF
import os

def OptiSale():
    date = datetime.date.today()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'I', 10)
    print('Укажите клиента:')
    client = input().title()
    pdf.write(6, 'Client:  ' + client)
    pdf.ln()
    pdf.write(6, 'Date: '), str(date)
    pdf.write(6, str(date))
    pdf.ln(10)


    pdf.set_font('Arial', '', 12)
    pdf.cell(6, 6, '', 1)
    pdf.cell(80, 6, 'name', 1)
    pdf.cell(23, 6, 'number', 1)
    pdf.cell(16, 6, 'price', 1)
    pdf.cell(16, 6, 'total', 1)
    pdf.ln()


    pdf.set_font('Arial', '', 8)
    position = 1
    name = ''
    number = 0
    price = 0
    total = 0
    final_total = 0
    flag = True
    while flag != False:
        print('Добавить в заказ: ', end='')
        name = input()
        while True:
            try:
                print('Количество: ', end='')
                number = int(input())
                break
            except ValueError:
                print('Некорректный ввод')
                continue
        while True:
            try:
                print('Цена: ', end='')
                price = float(input())
                break
            except ValueError:
                print('Некоректный ввод')

        pdf.cell(6, 6, str(position), 1)
        pdf.cell(80, 6, name, 1)
        pdf.cell(23, 6, str(number), 1)
        pdf.cell(16, 6, str(price), 1)
        total = round(number * price, 2)
        pdf.cell(16, 6, str(total), 1)
        final_total += total
        position += 1
        pdf.ln()
        print('Для формирования заказа наберите на клавиатуре "print"')
        print('Для продолжения обработки заказа нажмите "Enter."')
        choice = input()
        if choice == 'print':
            flag = False
    final_total = round(final_total, 2)
    pdf.cell(109, 6, '')
    pdf.cell(16, 6, 'END ', 1)
    pdf.cell(16, 6, str(final_total), 1)

    date = str(date)
    os.chdir('E:\Pycharm\PyCharm Community Edition 2020.1.1\OptiSales\Клиенты')
    client_list = os.listdir('E:\Pycharm\PyCharm Community Edition 2020.1.1\OptiSales\Клиенты')
    copy = 2
    copy_file = str(client + ' ' + date[8:] + '.' + date[5:7] + '.pdf')
    if client in client_list:
        os.chdir('E:\Pycharm\PyCharm Community Edition 2020.1.1\OptiSales\Клиенты' + '\\' + client)
        while True:
            if copy_file in os.listdir():
                copy_file = str(client + ' ' + date[8:] + '.' + date[5:7] + '(' + str(copy) + ')' + '.pdf')
                copy += 1
            elif copy_file not in os.listdir():
                return pdf.output(copy_file)
    elif client not in client_list:
        os.chdir('E:\Pycharm\PyCharm Community Edition 2020.1.1\OptiSales\Клиенты')
        os.mkdir(client)
        os.chdir('E:\Pycharm\PyCharm Community Edition 2020.1.1\OptiSales\Клиенты' + '\\' + client)
        return pdf.output(client + ' ' + date[8:] + '.' + date[5:7] + '.pdf', 'F')

OptiSale()