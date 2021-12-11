import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import sqlite3
import csv
from calc import Ui_Calc
from number_systems import Ui_NumberSystems
from converter import Ui_Converter
from formula import Ui_Formula
from csv_redact import Ui_CSV_Redact
from main_window import Ui_MainWindow


# класс главного окна, в котором можно выбрать, какую операцию пользователь хочет совершить
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # подключение кнопок к событию открытия соответствующих форм
        self.calc_btn.clicked.connect(self.calcform_show)
        self.number_btn.clicked.connect(self.numbers_show)
        self.converter_btn.clicked.connect(self.converter_show)
        self.form_btn.clicked.connect(self.formulasform_show)

    def calcform_show(self):
        self.calc_form = Calc(self)
        self.calc_form.show()

    def numbers_show(self):
        self.numbers_form = NumberSystems(self)
        self.numbers_form.show()

    def converter_show(self):
        self.converter_form = Converter(self)
        self.converter_form.show()

    def formulasform_show(self):
        self.formulas_form = Formulas(self)
        self.formulas_form.show()


# класс, отвечающий за функционал окна с калькулятором
class Calc(QMainWindow, Ui_Calc):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        # переменная, куда записываются все вводимые с помощью кнопок числа/операторы
        self.result = []
        # текущее число, которое набирает пользователь, отображается в self.lineEdit
        self.number = ""
        # подключение кнопок к методам
        self.btn_clear.clicked.connect(self.clear)
        self.digitsgroup.buttonClicked.connect(self.add_number)
        self.operatorsgroup.buttonClicked.connect(self.operation)
        self.btn_equals.clicked.connect(self.print_result)
        self.btn_point.clicked.connect(self.add_point)
        self.btn_sign.clicked.connect(self.change_sign)
        self.done = False  # было ли нажато "равно" во время предыдущего действия

    # сброс (текущее число и записанное выражение обнуляются, на экране калькулятора - 0)
    def clear(self):
        self.lineEdit.setText("0")
        self.number = ""
        self.result = []

    # изменение знака текущего числа на противоположный
    def change_sign(self):
        # если в данный момент есть записанное число
        if self.number:
            # если число без минуса, добавляем к его началу -
            if self.number[0] != "-":
                self.number = "-" + self.number
                # выводим текущее число на экран
                self.lineEdit.setText(self.number)
            # если с минусом : убираем минус из записи числа
            else:
                self.number = self.number[1:]
                # выводим текущее число на экран
                self.lineEdit.setText(self.number)

    # добавление точки (переход к дробной части)
    def add_point(self):
        # если предыдущее действие - равно, не добавляем точку, а начинаем запись операций с начала
        if self.done:
            self.result = []
            self.number = ""
            self.done = False
        # если есть текущее число, добавляем к нему точку
        if self.number:
            self.number += "."
        # выводим текущее число на экран
        self.lineEdit.setText(self.number)

    # добавление числа
    def add_number(self, id):
        # берем текст кнопки, находящейся в группе кнопок с цифрами - это прибавляемая цифра
        digit = id.text()
        # если предыдущее действие - равно, не добавляем цифру,
        # а начинаем запись операций с нажатой цифры
        if self.done:
            self.result = []
            self.number = digit
            self.done = False
        # если текущее число уже есть и оно не равно 0 (нельзя приписать цифру к нулю),
        # приписываем выбранную цифру к текущему числу
        elif self.number and self.number != "0":
            self.number += digit
        # иначе выбранная цифра - текущее число
        else:
            self.number = digit
        # выводим текущее число на экран
        self.lineEdit.setText(self.number)

    # добавление оператора в выражение
    def operation(self, id):
        # если есть текущее число - отпраляем его в переменную с выражением
        # и обнуляем значение текущего числа
        if self.number:
            self.result.append(self.number)
            self.number = ""
        # заменяем знак возведения в степень на соответствующий оператор в питоне
        if id.text() == "^":
            operator = "**"
        # или же просто берем текст с кнопки из группы кнопок с операторами в остальных случаях
        else:
            operator = id.text()
        # если предыдущее действие - равно, все равно добавляем оператор к выражению,
        # чтобы можно было проводить действия с полученным результатом
        if self.done:
            self.result.append(operator)
            self.done = False
        # если в выражении есть хоть одно число - добавляем оператор
        elif self.result and self.result[-1] not in "+-*/**":
            self.result.append(operator)
        # если же последний элемент значения оператор - заменяем его на новый
        else:
            self.result = self.result[:-1]
            self.result.append(operator)

    def print_result(self):
        # если есть текущее число - отпраляем его в переменную с выражением
        # и обнуляем значение текущего числа
        if self.number:
            self.result.append(self.number)
            self.number = ""
        # если есть записанное выражение и оно соответсвует правилам,
        # вычисляем значение и выводим на экран
        if self.result:
            if self.result[-1] not in "+-*/**":
                try:
                    self.lineEdit.setText(str(eval("".join(self.result))))
                    self.number = ""
                    self.result = list(str(eval("".join(self.result))))
                    self.done = True
                except ZeroDivisionError:
                    self.lineEdit.setText("Error")
                    self.number = ""
                    self.result = []


# класс, отвечающий за функционал окна с переводом в системы счислений
class NumberSystems(QMainWindow, Ui_NumberSystems):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        # словарь для преобразования текста рядом с кнопками в числа
        self.systems = {"Двоичная": 2, "Троичная": 3, "Восьмеричная": 8, "Десятичная": 10,
                        "Шестнадцатеричная": 16}
        self.result = ""  # переменная для записи результата
        self.sys1 = 0  # система счисления первого числа
        self.sys2 = 0  # система счисления, в которую нужно перевести
        # подключаем элементы к методам
        self.group1.buttonToggled.connect(self.button_check)
        self.group2.buttonToggled.connect(self.button_check)
        self.result_btn.clicked.connect(self.print_result)
        self.first_number.textChanged.connect(self.show_button)
        self.csv_btn.clicked.connect(self.csv_redact)
        # переменные для проверки, выбраны ли системы счислений
        self.first_choose = False
        self.second_choose = False
        # прячем элементы для лучших времен
        self.other1.hide()
        self.other2.hide()
        self.result_btn.hide()

    # показ кнопки для выведения результата
    def show_button(self):
        # если обе системы счислений выбраны и записано число для перевода, показываем кнопку
        if self.first_choose and self.second_choose and self.first_number.text():
            if not self.other1.isHidden() and not self.other1.text():
                self.result_btn.hide()
            elif not self.other2.isHidden() and not self.other2.text():
                self.result_btn.hide()
            else:
                self.result_btn.show()
        # иначе прячем
        else:
            self.result_btn.hide()

    # показ строки под переключателем "Другая" для ввода основания системы счисления, если он выбран
    def show_other(self, id, ischecked=True):
        if id == 1:
            self.other1.show() if ischecked else self.other1.hide()
        else:
            self.other2.show() if ischecked else self.other2.hide()
        # если изменяется текст в строках, вызываем метод показа кнопки
        self.other1.textChanged.connect(self.show_button)
        self.other2.textChanged.connect(self.show_button)

    # выбор переключателя для нужной системы счисления
    # изменение значений переменных для проверки выбора
    # для дальнейшего отображения кнокпи для результата
    def button_check(self, id):
        if id in self.group1.buttons():
            if id.text() != "Другая":
                self.first_choose = True if id.isChecked() else False
            else:
                self.first_choose = True if id.isChecked() else False
                self.show_other(1) if id.isChecked() else self.show_other(1, False)
        elif id in self.group2.buttons():
            if id.text() != "Другая":
                self.second_choose = True if id.isChecked() else False
            else:
                self.second_choose = True if id.isChecked() else False
                self.show_other(2) if id.isChecked() else self.show_other(2, False)
        self.show_button()

    # открытие режима работы с csv-файлами
    def csv_redact(self):
        self.function = "Системы счисления"
        self.text = "Требования к файлу:\n\nПервый" \
                    " столбец: число\nВторой столбец: основание его системы счисления" \
                    " (целое число)\nТретий столбец: основание системы счисления" \
                    " для перевода (целое число)\nРазделитель: ';'\nВнимание: строки," \
                    " не подходящие под требования, будут удалены"
        # открытие окна для работы с csv-файлами
        self.csv_redact_window = CSVFiles(self, self.function, self.text)
        self.csv_redact_window.show()

    # перевод числа в другую систему счисления
    def print_result(self):
        self.result = ""
        # берем первичное число из строки
        # если наше число вдруг не число - выводим ошибку
        try:
            self.number = int(self.first_number.text())
        except Exception:
            self.result_line.setText("Error")
            return None
        # берем его систему счисления из первой группы переключателей
        for i in self.group1.buttons():
            if i.isChecked():
                if i.text() in self.systems:
                    self.sys1 = self.systems[i.text()]
                else:
                    self.sys1 = int(self.other1.text())
        # преобразовывем число в десятичную систему счисления
        if self.sys1 != 10:
            try:
                self.number = int(str(self.number), base=self.sys1)
            # если наше число не соответсвует своей системе счисления - выводим ошибку
            except ValueError:
                self.result_line.setText("Error")
                return None
        # берем систему счисления для перевода из второй группы переключателей
        for i in self.group2.buttons():
            if i.isChecked():
                if i.text() in self.systems:
                    self.sys2 = self.systems[i.text()]
                else:
                    self.sys2 = int(self.other2.text())
        # для некоторых систем счисления используем встроенные функции
        if self.sys2 == 2:
            self.result = format(int(self.number), 'b')
        elif self.sys2 == 8:
            self.result = format(int(self.number), 'o')
        elif self.sys2 == 16:
            self.result = format(int(self.number), 'x')
        elif self.sys2 == 10:
            self.result = str(self.number)
        # для остальных преобразовываем с помощью деления и остатков
        else:
            if self.sys2 <= 9 and self.sys2 > 1:
                while self.number > 0:
                    self.result = str(self.number % self.sys2) + self.result
                    self.number //= self.sys2
            # системы счислений с основанием больше 9 (кроме 10 и 16) пока не поддерживаются
            else:
                self.result = "Мы пока не можем это решить"
        # выводим результат в строку для результата
        self.result_line.setText(self.result)


# класс, отвечающий за функционал окна с конвертером единиц измерения
class Converter(QMainWindow, Ui_Converter):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.measure = ""  # выбранная физическая величина
        # переменные для проверки выбора единиц измерения
        self.first_choose = False
        self.second_choose = False
        # прячем кнопку для расчета результата
        self.result_btn.hide()
        # подключаемся к базе данных с единицами измерений
        self.con = sqlite3.connect("converter_db.sqlite")
        self.cur = self.con.cursor()
        # заполняем выпадающие списки
        self.choose_firstunit.addItem("-")
        self.choose_secondunit.addItem("-")
        # берем все физические величины из базы данных для первого выпадающего списка
        self.measures = self.cur.execute("""SELECT measure FROM measures""").fetchall()
        self.choose_measure.addItem("-")
        self.choose_measure.addItems([i[0] for i in self.measures])
        # подлкючаем сигналы от элементов к соотбетствующим методам
        self.choose_measure.activated[str].connect(self.measure_chosen)
        self.first_number.textChanged.connect(self.show_button)
        self.csv_btn.clicked.connect(self.csv_redact)

    # когда физическая величина выбрана
    def measure_chosen(self, text):
        # сбрасываем элементы выпадающих списков с единицами измерений
        self.choose_firstunit.clear()
        self.choose_secondunit.clear()
        self.choose_firstunit.addItem("-")
        self.choose_secondunit.addItem("-")
        self.measure = text
        if self.measure != "-":
            # берем все единицы измерений, относящиеся к выбранной физ.величине из базы данных
            self.units = self.cur.execute("""SELECT unit FROM units 
        WHERE measure=(
    SELECT id FROM measures 
        WHERE measure = ?)""", (self.measure,)).fetchall()
            # и заполняем ими выпадающие списки
            self.choose_firstunit.addItems([i[0] for i in self.units])
            self.choose_secondunit.addItems([i[0] for i in self.units])
            # подключаем сигналы выбора элемента из списка к методу проверки выбора
            self.choose_firstunit.activated[str].connect(self.unit1_chosen)
            self.choose_secondunit.activated[str].connect(self.unit2_chosen)
            self.result_btn.clicked.connect(self.transform)

    # метод для показа кнопки для результата
    def show_button(self):
        # если обе единицы измерения выбраны и указано значение, которое нужно перевести, в строке,
        # показываем кнопку
        if self.first_choose and self.second_choose and self.first_number.text():
            self.result_btn.show()
        # иначе прячем
        else:
            self.result_btn.hide()

    # проверка выбора первой единицы измерения
    def unit1_chosen(self, text):
        self.first_unit = text
        if self.first_unit != "-":
            self.first_choose = True
        else:
            self.first_choose = False
        self.show_button()

    # проверка выбора второй единицы измерения
    def unit2_chosen(self, text):
        self.second_unit = text
        if self.second_unit != "-":
            self.second_choose = True
        else:
            self.second_choose = False
        self.show_button()

    # перевод единиц измерения
    def transform(self):
        # берем из базы данных коэффициент умножения первой е.и. и второй е.и.
        # коэффициент умножения у меня - значение, на которое нужно умножить
        # первичную единицу измерения числа (в большинстве случаев - е.и. в СИ),
        # чтобы получить значение в выбранной е.и.
        self.first_coeff = self.cur.execute("""SELECT multiply FROM units
WHERE unit = ?""", (self.first_unit,)).fetchall()[0][0]
        self.second_coeff = self.cur.execute("""SELECT multiply FROM units
WHERE unit = ?""", (self.second_unit,)).fetchall()[0][0]
        try:
            # сначала делим указанное в строке число на первый
            # коэффициент умножения (перевод в первичную е.и.), затем умножаем на
            # второй для перевода в нужную е.и.
            self.result = float(self.first_number.text()) / self.first_coeff * self.second_coeff
            self.second_number.setText(str(self.result))
        except Exception:  # Если что-то пошло не так - выводим ошибку
            self.second_number.setText("Error")

    def csv_redact(self):
        self.function = "Конвертер"
        self.text = "Требования к файлу:\n\nПервый" \
                    " столбец: значение величины\n" \
                    "Второй столбец: единица измерения заданного значения" \
                    " \nТретий столбец: единица измерения, в которую нужно перевести" \
                    " \nРазделитель: ';'\nВнимание: строки," \
                    " не подходящие под требования, будут удалены"
        # открытие окна для работы с csv-файлами
        self.csv_redact_window = CSVFiles(self, self.function, self.text)
        self.csv_redact_window.show()


# класс, отвечающий за функционал окна с расчетами по формулам
class Formulas(QMainWindow, Ui_Formula):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        # подключение к базе данных с формулами
        self.con = sqlite3.connect("formulas.sqlite")
        self.cur = self.con.cursor()
        # берем из базы данных все физические величины
        self.measures = self.cur.execute("""SELECT measure FROM measures""").fetchall()
        # и заполняем выпадающий список для выбора физ. величины ими
        self.measures_box.addItem("-")
        self.measures_box.addItems([i[0] for i in self.measures])
        # подключаем сигналы элементов к соответствующим методам
        self.measures_box.activated[str].connect(self.measure_chosen)
        self.formulas_box.activated[str].connect(self.formula_chosen)
        self.ready_btn.clicked.connect(self.show_lineedits)
        self.result_btn.clicked.connect(self.result)
        # списки строк для вписывания значений физ.величин в выбранной формуле
        self.lines = [self.first_line, self.second_line, self.third_line, self.fourth_line,
                      self.fifth_line, self.sixth_line, self.seventh_line, self.eighth_line,
                      self.nineth_line, self.tenth_line]
        self.labels = [self.first_label, self.second_label, self.third_label, self.fourth_label,
                       self.fifth_label, self.sixth_label, self.seventh_label, self.eighth_label,
                       self.nineth_label, self.tenth_label]
        # пока что прячем эти элементы
        for i in self.lines:
            i.hide()
        for i in self.labels:
            i.hide()
        self.result_btn.hide()
        self.length = 0

    # когда выбрана физическая величина
    def measure_chosen(self, text):
        if text != "-":
            self.formulas_box.clear()
            # выбираем из базы данных все формулы, относящиеся к данной физ.величине
            self.formulas = self.cur.execute("""SELECT formula FROM formulas 
        WHERE measure=(
    SELECT id FROM measures 
        WHERE measure = ?)""", (text,)).fetchall()
            self.formulas_box.addItem("-")
            # и заполняем ими выпадающий список для выбора формулы
            self.formulas_box.addItems([i[0] for i in self.formulas])

    # когда выбрана формула
    def formula_chosen(self, text):
        if text != "-":
            self.letters = []
            # берем из базы данных длину формулу (кол-во величин в ней)
            self.length = self.cur.execute("""SELECT length FROM formulas 
                WHERE formula=?""", (text,)).fetchall()[0][0]
            self.formula = text
            self.formula_list = []
            name_of_measure = ""
            # разбиваем строку с формулой на отдельные элементы - величины и операторы
            for i in range(len(self.formula)):
                if not self.formula[i].isalpha():
                    self.formula_list.append(name_of_measure)
                    self.letters.append(name_of_measure)
                    self.formula_list.append(self.formula[i])
                    name_of_measure = ""
                else:
                    name_of_measure += self.formula[i]
            self.formula_list.append(name_of_measure)
            self.letters.append(name_of_measure)
        else:
            self.formula = ""
            self.length = 0

    # метод для показа кнопки для результата
    def show_result_btn(self):
        all_chosen = True
        # проверка, все ли значения для величин введены
        for i in self.used_lineedits:
            if i.text() == "":
                all_chosen = False
        if all_chosen:
            self.result_btn.show()
        else:
            self.result_btn.hide()

    # расчет результата
    def result(self):
        # словарь физ.величина:ее значение
        self.amounts = dict()
        self.result = [i for i in self.formula_list]
        # заполняем словарь
        for i in range(len(self.used_lineedits)):
            self.amounts[self.letters[i]] = self.used_lineedits[i].text()
        # подставляем в список result (копию списка с формулой)
        # значения физ.величин вместо их обозначений
        for i in range(len(self.result)):
            if self.result[i] in self.amounts:
                self.result[i] = self.amounts[self.result[i]]
        # вычисляем значение получившегося выражения
        try:
            self.result = str(eval("".join(self.result)))
            self.result_line.setText(self.result)
        except Exception:  # выводим ошибку, если что-то не так
            self.result_line.setText("Error")

    # показываем строки для ввода значений величин в выбранной формуле
    def show_lineedits(self):
        # показываем ровно столько строк, сколько величин в формуле
        if self.length:
            self.used_lineedits = []
            # и указываем рядом с каждой строкой,
            # значение какой величины мы вводим  (буквенное обозначение
            for i in range(self.length):
                self.lines[i].show()
                self.labels[i].show()
                self.labels[i].setText(self.letters[i])
                self.used_lineedits.append(self.lines[i])
            for i in self.used_lineedits:
                i.textChanged.connect(self.show_result_btn)


# класс, отвечающий за функционал окна для работы с csv-файлами
class CSVFiles(QMainWindow, Ui_CSV_Redact):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.mode = args[1]  # режим - переданный аргумент с формы, откуда открыто окно
        self.first_text.setText(self.first_text.text() + self.mode)
        self.first_text.adjustSize()
        # текст требований к файлу - переданный аргумент с формы, откуда открыто окно
        self.textBrowser.setText(args[2])
        # подключаем сигналы элементов к соответствующим методам
        self.choose_btn.clicked.connect(self.choose_file)
        self.transform_btn.clicked.connect(self.transform)
        self.transform_btn.hide()

    # метод для выбора файла
    def choose_file(self):
        self.ready_label.setText("")
        self.amount_label.setText("")
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать файл', '', "*.csv")[0]
        self.current_file.setText(self.fname)
        self.transform_btn.show()

    # метод для преобразования выбранного файла на основе выбранного режима
    def transform(self):
        self.succesfully_transformed = 0
        self.strings = []
        with open(self.fname, "r", encoding="utf8") as csvfile:
            self.reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            if self.mode == "Системы счисления":
                for i in self.reader:
                    if len(i) == 3:
                        self.strings.append([i[0], i[1], i[2]])
                with open(self.fname, 'w', newline='', encoding="utf8") as csvfile:
                    self.writer = csv.writer(csvfile, delimiter=';', quotechar='"')
                    for i in self.strings:
                        try:
                            self.number_first = int(i[0])
                            self.number = int(i[0])
                            self.sys1 = int(i[1])
                            self.sys2 = int(i[2])
                        except Exception:
                            continue
                        if self.sys1 != 10:
                            try:
                                self.number = int(str(self.number), base=self.sys1)
                            except ValueError:
                                self.result = "-"
                                self.writer.writerow(
                                    [self.number, self.sys1, self.sys2, self.result])
                                continue
                        if self.sys2 == 2:
                            self.result = format(int(self.number), 'b')
                        elif self.sys2 == 8:
                            self.result = format(int(self.number), 'o')
                        elif self.sys2 == 16:
                            self.result = format(int(self.number), 'x')
                        elif self.sys2 == 10:
                            self.result = str(self.number)
                        else:
                            if self.sys2 <= 9 and self.sys2 > 1:
                                while self.number > 0:
                                    self.result = str(self.number % self.sys2) + self.result
                                    self.number //= self.sys2
                            else:
                                self.result = "-"
                        if self.result != "-":
                            self.succesfully_transformed += 1
                        self.writer.writerow([self.number_first, self.sys1, self.sys2, self.result])
            elif self.mode == "Конвертер":
                self.con = sqlite3.connect("converter_db.sqlite")
                self.cur = self.con.cursor()
                for i in self.reader:
                    if len(i) == 3:
                        self.strings.append([i[0], i[1], i[2]])
                with open(self.fname, 'w', newline='', encoding="utf8") as csvfile:
                    self.writer = csv.writer(csvfile, delimiter=';', quotechar='"')
                    for i in self.strings:
                        try:
                            self.number = float(i[0])
                            self.first_unit = i[1]
                            self.second_unit = i[2]
                            self.first_coeff = self.cur.execute("""SELECT multiply FROM units
                                                    WHERE unit = ?""",
                                                                (self.first_unit,)).fetchall()[0][0]
                            self.second_coeff = self.cur.execute("""SELECT multiply FROM units
                                                    WHERE unit = ?""",
                                                                 (self.second_unit,)).fetchall()[0][
                                0]
                        except Exception:
                            continue
                        self.result = float(
                            self.number) / self.first_coeff * self.second_coeff
                        self.succesfully_transformed += 1
                        self.writer.writerow(
                            [self.number, self.first_unit, self.second_unit, self.result])
            self.ready_label.setText("Готово!")
            # подсчет успешно преобразованных строк
            self.amount_label.setText(f"Успешно преобразованные строки:"
                                      f" {self.succesfully_transformed}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
