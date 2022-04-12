# OptiSales

Для власних потреб написав не велику програму, яка виводить у форматі PDF таблицю/накладну
в якій вказуються товарні групи, їх кількість, ціна. Після чого програма виводить таблицю, та кінцеву суму до сплати.

<img src = 0-02-05-8cb1863200fb34f8f15a15ff5501189c8333ee675334d117441d03523d0f9a09_533b639781e34e22.jpg wight = 200 px>

### Використані бібліотеки: 
- datetime 
- os
- fpdf

### Функціонал:
-	Приймає ім’я клієнта
-	Приймає назву товару, кількість, ціну
-	Виводить кінцеву суму
-	В файлі вказується ім’я клієнта, дата створення накладної (Так само буде названо і сам PDF файл
-	Програма створює діректорію з ім’ям клієнта в папці (клієнти), або шукає вже існуючу 
-	Якщо клієнтом зроблено декілька заказів за один день, програма виведе, наприклад Іванов В(1), Іванов В(2) и т.д.
