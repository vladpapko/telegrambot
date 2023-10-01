import telebot
import pandas as pd

bot = telebot.TeleBot("6674929433:AAHHNAXdSmJZNKUn9WG9Mp_MLG97Orm3X3k")

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот для анализа данных. Чтобы начать анализ данных нажми на кнопочку /analyze.")

@bot.message_handler(commands=['analyze'])
def handle_analyze(message):
    try:
        data = pd.read_excel("lab_pi_101.xlsx")
        last_row = data.shape[0]
        skore = data['Группа'].str.contains('ПИ101').sum()
        student_PI101 = len(data[data['Группа'] == 'ПИ101']['Личный номер студента'].unique())
        pi101 = ', '.join(map(str, data[data['Группа'] == 'ПИ101']['Личный номер студента'].unique()))
        control = ', '.join(map(str, data['Уровень контроля'].unique()))
        years = ', '.join(map(str, sorted(data['Год'].unique())))

        result_message = (
            f"В исходном датасете содержалось {last_row} оценок, из них {skore} относятся к группе ПИ101.\n"
            f"В датасете находятся оценки {student_PI101} студентов со следующими номерами: {pi101}\n"
            f"Используемые виды контроля: {control}\n"
            f"Данные представлены по следующим учебным годам: {years}"
        )

        bot.send_message(message.chat.id, result_message)
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка при анализе данных: {str(e)}")

if __name__ == '__main__':
    bot.polling(none_stop=True)