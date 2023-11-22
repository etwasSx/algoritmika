# Подключение модулей PyQt для создания дексопных приложений. Подключение виджетов

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QButtonGroup, QRadioButton,
    QPushButton, QLabel)

# Подключаем модуль для перемешивания списка
from random import shuffle


# Класс Question. Новая структура хранения вопросов в приложении.
# 5 свойств. Вопрос, правильный ответ, и 3 неправильных
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        # все строки надо задать при создании объекта, они запоминаются в свойства
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


# Создание списка с вопросами, Создаем без промежуточных переменных
# (Вопрос, Правильны ответ, 3 неправильных ответа)
questions_list = []
questions_list.append(Question('Вопрос1', 'Правильный ответ1', 'Неверный ответ1', 'Неверный ответ1', 'Неверный ответ1'))
questions_list.append(Question('Вопрос2', 'Правильный ответ2', 'Неверный ответ2', 'Неверный ответ2', 'Неверный ответ2'))
questions_list.append(Question('Вопрос3', 'Правильный ответ3', 'Неверный ответ3', 'Неверный ответ3', 'Неверный ответ3'))

# Создание экземпляра приложения
app = QApplication([])

# Создание кнопки Ответить/Следующий вопрос
btn_OK = QPushButton('Ответить')  # кнопка ответа

# Создание надписи в котором будет вопрос
lb_Question = QLabel('Самый сложный вопрос в мире!')  # текст вопроса

# Группа с вопросам. И надпись для группы
RadioGroupBox = QGroupBox("Варианты ответов")  # группа на экране для переключателей с ответами

# 4 кнопки для вариантов ответов с их названиями. Мы их изменять будем
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

# это для группировки переключателей, чтобы управлять их поведением
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# линии для расположения элементов
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()  # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)  # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)  # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)

# разместили столбцы в одной строке
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

# готова "панель" с вариантами ответов
RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox("Результат теста")

# здесь размещается надпись "правильно" или "неправильно"
lb_Result = QLabel('прав ты или нет?')

# здесь будет написан текст правильного ответа
lb_Correct = QLabel('ответ будет тут!')

# Оформляем расположение элементов для окна с результатом
layout_res = QVBoxLayout()
# Результат lb_Result размещаем в левом (Qt.AlignLeft) - верхнем углу(Qt.AlignTop)
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
# Правильный ответ распологаем по центру-горизонтальному
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)

# И к нашей группе результатов добавляем полученный слой с оформлением
AnsGroupBox.setLayout(layout_res)

# Расположение элементов в рабочем окне
layout_line1 = QHBoxLayout()  # слой с вопросом
layout_line2 = QHBoxLayout()  # слой с вариантами ответов или результатами теста
layout_line3 = QHBoxLayout()  # слой с кнопкой "Ответить"/"Следующий вопрос"

# Распологаем Вопрос по центру
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
# скроем панель с ответом, сначала должна быть видна панель вопросов
AnsGroupBox.hide()

# Кнопка Ответить/Следующий вопрос. Увеличиваем размер
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)  # кнопка должна быть большой
layout_line3.addStretch(1)

# Самый главный слой, который прикрепим к главному окну
layout_card = QVBoxLayout()

# Добавляем к нему ранее полученные слои и оформляем
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)  # пробелы между содержимым


# Функция для отображения панели результатов
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()  # Прячем вопросы
    AnsGroupBox.show()  # Показываем ответы
    btn_OK.setText('Следующий вопрос')  # Меняем текст кнопки


# Показать вопрос.
def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()  # Показываем вопросы
    AnsGroupBox.hide()  # Прячем ответы
    btn_OK.setText('Ответить')  # меняем текст кнопки на Ответить
    # сбросить выбранную радио-кнопку
    RadioGroup.setExclusive(False)  # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)  # Сброс кнопок до состояния "Не выбрано"
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)  # вернули ограничения, теперь только одна радиокнопка может быть выбрана


# Список с кнопками
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


# Функция для создания вопроса. Принимает на вход q. Экзмепляр класса Question
def ask(q: Question):
    ''' функция записывает значения вопроса и ответов в соответствующие виджеты,
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers)  # перемешали список из кнопок, теперь на первом месте списка какая-то непредсказуемая кнопка
    answers[0].setText(q.right_answer)  # первый элемент списка заполним правильным ответом, остальные - неверными
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)  # вопрос
    lb_Correct.setText(q.right_answer)  # ответ
    show_question()  # показываем панель вопросов


def show_correct(res):
    ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    lb_Result.setText(res)
    show_result()


def check_answer():
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        # правильный ответ!
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # неправильный ответ!
            show_correct('Ты ошибся!')



def next_question():
    ''' задает следующий вопрос из списка '''
    # этой функции нужна переменная, в которой будет указываться номер текущего вопроса
    # эту переменную можно сделать глобальной, либо же сделать свойством "глобального объекта" (app или window)
    # мы заведем (ниже) свойство window.cur_question.
    window.cur_question += 1  # переходим к следующему вопросу
    if window.cur_question >= len(questions_list):
        window.cur_question = 0  # если список вопросов закончился - идем сначала
    q = questions_list[window.cur_question]  # взяли вопрос
    ask(q)  # спросили


# Функция для кнопки Ответить/Следующий вопрос
def click_OK():
    ''' определяет, надо ли показывать другой вопрос либо проверить ответ на этот '''
    if btn_OK.text() == 'Ответить':
        check_answer()  # проверка ответа
    else:
        next_question()  # следующий вопрос


# Создаем главное окно приложения
window = QWidget()

# К этому окну прикрепляем главный слой
window.setLayout(layout_card)
# Название приложения
window.setWindowTitle('Memo Card')
# текущий вопрос из списка сделаем свойством объекта "окно", так мы сможем спокойно менять его из функции:
window.cur_question = -1  # по-хорошему такие переменные должны быть свойствами,
# только надо писать класс, экземпляры которого получат такие свойства,
# но python позволяет создать свойство у отдельно взятого экземпляра


btn_OK.clicked.connect(click_OK)  # по нажатии на кнопку выбираем, что конкретно происходит

# все настроено, осталось задать вопрос и показать окно
next_question()
# размеры окна
window.resize(400, 300)
# отобразить окно
window.show()
# оставить приложение на экране
app.exec()
