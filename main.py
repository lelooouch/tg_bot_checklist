import logging, asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message

TOKEN = 'token'

bot = Bot(token=TOKEN)
logging.basicConfig(level=logging.INFO)
dp = Dispatcher()

f = []
with open('data.txt', 'r', encoding='utf-8') as file:
    for i in file:
        i = i.replace('\n', '')
        f.append(i.split('\t'))
print(f)

# Радиотехника
proshel_radiotehnika_ochno_budjet = ['📻 Радиотехника (Бюджетные места)']
proshel_radiotehnika_ochno_platno = ['📻 Радиотехника (Платные места)']
proshel_radiotehnika_ochno_otdelnaya_kvota = ['📻 Радиотехника (Отдельная квота)']
proshel_radiotehnika_ochno_osobaya_kvota = ['📻 Радиотехника (Особая квота)']
proshel_radiotehnika_zaochno = ['📻 Радиотехника (Заочно, платно)']

# Программная Инженерия
proshel_prog_inj_ochno_budjet = ['🤖 Программная Инженерия (Бюджетные места)']
proshel_prog_inj_ochno_platno = ['🤖 Программная Инженерия (Платные места)']
proshel_prog_inj_ochno_otdelnaya_kvota = ['🤖 Программная Инженерия (Отдельная квота)']
proshel_prog_inj_ochno_osobaya_kvota = ['🤖 Программная Инженерия (Особая квота)']

# Прикладная Информатика ()
proshel_p_inf_ochno_budjet = ['💻 Прикладная Информатика (Бюджетные места)']
proshel_p_inf_ochno_platno = ['💻 Прикладная Информатика (Платные места)']
proshel_p_inf_ochno_otdelnaya_kvota = ['💻 Прикладная Информатика (Отдельная квота)']
proshel_p_inf_ochno_osobaya_kvota = ['💻 Прикладная Информатика (Особая квота)']
proshel_p_inf_zaochno = ['💻 Прикладная Информатика (Заочно, платно)']
proshel_p_inf_ochnozaochno = ['💻 Прикладная Информатика (Очно-заочно, платно)']

# Прикладной ИИ
proshel_pii_ochno_budjet = ['💡 Прикладной ИИ (Бюджетные места)']
proshel_pii_ochno_platno = ['💡 Прикладной ИИ (Платные)']
proshel_pii_ochno_otdelnaya_kvota = ['💡 Прикладной ИИ (Отдельная квота)']
proshel_pii_ochno_osobaya_kvota = ['💡 Прикладной ИИ (Особая квота)']

# Алгоримы ИИ
proshel_aii_ochno_budjet = ['🧠 Алгоримы ИИ (Бюджетные места)']
proshel_aii_ochno_platno = ['🧠 Алгоримы ИИ (Платные места)']
proshel_aii_ochno_osobaya_kvota = ['🧠 Алгоримы ИИ (Особая квота)']
proshel_aii_ochno_otdelnaya_kvota = ['🧠 Алгоримы ИИ (Отдельная квота)']

# Безопасность компьютерных систем
proshel_bks_ochno_budjet = ['🔒 Безопасность компьютерных систем (Бюджетные места)']
proshel_bks_ochno_platno = ['🔒 Безопасность компьютерных систем (Платные места)']
proshel_bks_ochno_osobaya_kvota = ['🔒 Безопасность компьютерных систем (Особая квота)']
proshel_bks_ochno_otdelnaya_kvota = ['🔒 Безопасность компьютерных систем (Отдельная квота)']
proshel_bks_ochnozaochno = ['🔒 Безопасность компьютерных систем (Очно-заочно, платно)']

# Инфокоммуникационные технологии и системы связи
proshel_itss_ochno_budjet = ['🛜 Инфокоммуникационные технологии и системы связи (Бюджетные места)']
proshel_itss_ochno_platno = ['🛜 Инфокоммуникационные технологии и системы связи (Платные места)']
proshel_itss_ochno_osobaya_kvota = ['🛜 Инфокоммуникационные технологии и системы связи (Особая квота)']
proshel_itss_ochno_otdelnaya_kvota = ['🛜 Инфокоммуникационные технологии и системы связи (Отдельная квота)']

# Конструирование и технология электронных средств
proshel_ktes_ochno_budjet = ['📱 Конструирование и технология электронных средств (Бюджетные места)']
proshel_ktes_ochno_platno = ['📱 Конструирование и технология электронных средств (Платные места)']
proshel_ktes_ochno_otdelnaya_kvota = ['📱 Конструирование и технология электронных средств (Отдельная квота)']
proshel_ktes_ochno_osobaya_kvota = ['📱 Конструирование и технология электронных средств (Особая квота)']

# Технология полиграфического и упаковочного производства
proshel_tpup_ochno_budjet = ['📦 Технология полиграфического и упаковочного производства (Бюджетные места)']
proshel_tpup_ochno_platno = ['📦 Технология полиграфического и упаковочного производства (Платные места)']
proshel_tpup_ochno_otdelnaya_kvota = ['📦 Технология полиграфического и упаковочного производства (Отдельная квота)']
proshel_tpup_ochno_osobaya_kvota = ['📦 Технология полиграфического и упаковочного производства (Особая квота)']

# Управление в технических системах
proshel_uts_ochno_budjet = ['🖥️ Управление в технических системах (Бюджетные места)']
proshel_uts_ochno_platno = ['🖥️ Управление в технических системах (Платные места)']
proshel_uts_ochno_otdelnaya_kvota = ['🖥️ Управление в технических системах (Отдельная квота)']
proshel_uts_ochno_osobaya_kvota = ['🖥️ Управление в технических системах (Особая квота)']

# Информатика и вычислительная техника
proshel_ivt_ochno_budjet = ['🛸 Информатика и вычислительная техника (Бюджетные места)']
proshel_ivt_ochno_platno = ['🛸 Информатика и вычислительная техника (Платные места)']
proshel_ivt_ochno_otdelnaya_kvota = ['🛸 Информатика и вычислительная техника (Отдельная квота)']
proshel_ivt_ochno_osobaya_kvota = ['🛸 Информатика и вычислительная техника (Особая квота)']
proshel_ivt_zaochno = ['🛸 Информатика и вычислительная техника (Заочно, платно)']

lists = [proshel_radiotehnika_ochno_budjet, proshel_radiotehnika_ochno_platno,
         proshel_radiotehnika_ochno_otdelnaya_kvota, proshel_radiotehnika_ochno_osobaya_kvota,
         proshel_radiotehnika_zaochno, proshel_prog_inj_ochno_budjet, proshel_prog_inj_ochno_platno,
         proshel_prog_inj_ochno_otdelnaya_kvota, proshel_prog_inj_ochno_osobaya_kvota,
         proshel_p_inf_ochno_budjet, proshel_p_inf_ochno_platno, proshel_p_inf_ochno_otdelnaya_kvota,
         proshel_p_inf_ochno_osobaya_kvota, proshel_p_inf_zaochno, proshel_p_inf_ochnozaochno,
         proshel_pii_ochno_budjet, proshel_pii_ochno_platno, proshel_pii_ochno_otdelnaya_kvota,
         proshel_pii_ochno_osobaya_kvota, proshel_aii_ochno_budjet, proshel_aii_ochno_platno,
         proshel_aii_ochno_osobaya_kvota, proshel_aii_ochno_otdelnaya_kvota, proshel_bks_ochno_budjet,
         proshel_bks_ochno_platno, proshel_bks_ochno_osobaya_kvota, proshel_bks_ochno_otdelnaya_kvota,
         proshel_bks_ochnozaochno, proshel_itss_ochno_budjet, proshel_itss_ochno_platno,
         proshel_itss_ochno_osobaya_kvota, proshel_itss_ochno_otdelnaya_kvota, proshel_ktes_ochno_budjet,
         proshel_ktes_ochno_platno, proshel_ktes_ochno_otdelnaya_kvota, proshel_ktes_ochno_osobaya_kvota,
         proshel_tpup_ochno_budjet, proshel_tpup_ochno_platno, proshel_tpup_ochno_otdelnaya_kvota,
         proshel_tpup_ochno_osobaya_kvota, proshel_uts_ochno_budjet, proshel_uts_ochno_platno,
         proshel_uts_ochno_otdelnaya_kvota, proshel_uts_ochno_osobaya_kvota, proshel_ivt_ochno_budjet,
         proshel_ivt_ochno_platno, proshel_ivt_ochno_otdelnaya_kvota, proshel_ivt_ochno_osobaya_kvota,
         proshel_ivt_zaochno]

ids = []

for i in range(310, -1, -1):
    for j in f:
        # Радиотехника
        # Очно бюджет
        if j[1] == '1' and j[2] == 'Основные места в рамках КЦП' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Радиотехника' and len(proshel_radiotehnika_ochno_budjet) <= 32 and j[0] not in ids:
            ids.append(j[0])
            proshel_radiotehnika_ochno_budjet.append([j[0], j[6]])

        # Очно платно
        elif j[1] == '1' and j[2] == 'Платно' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Радиотехника' and len(proshel_radiotehnika_ochno_platno) <= 6 and (j[0] not in ids):
            ids.append(j[0])
            proshel_radiotehnika_ochno_platno.append([j[0], j[6]])

        # Очно отдельная квота
        elif j[1] == '1' and j[2] == 'Отдельная квота' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Радиотехника' and len(proshel_radiotehnika_ochno_otdelnaya_kvota) <= 4 and (j[0] not in ids):
            ids.append(j[0])
            proshel_radiotehnika_ochno_otdelnaya_kvota.append([j[0], j[6]])

        # Очно Особая квота
        elif j[1] == '1' and j[2] == 'Отдельная квота' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Радиотехника' and len(proshel_radiotehnika_ochno_osobaya_kvota) <= 4 and (j[0] not in ids):
            ids.append(j[0])
            proshel_radiotehnika_ochno_osobaya_kvota.append([j[0], j[6]])

        # Заочно платно
        elif j[1] == '1' and j[2] == 'Платно' and j[3] == 'Заочно' and j[6] == str(i) \
        and j[7] == 'Радиотехника' and len(proshel_radiotehnika_zaochno) <= 60 and (j[0] not in ids):
            ids.append(j[0])
            proshel_radiotehnika_zaochno.append([j[0], j[6]])


        # Программная инженерия
        # Очно бюджет
        elif j[1] == '1' and j[2] == 'Основные места в рамках КЦП' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Программная инженерия' and len(proshel_prog_inj_ochno_budjet) <= 80 and (j[0] not in ids):
            ids.append(j[0])
            proshel_prog_inj_ochno_budjet.append([j[0], j[6]])

        # Очно платно
        elif j[1] == '1' and j[2] == 'Платно' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Программная инженерия' and len(proshel_prog_inj_ochno_platno) <= 200 and (j[0] not in ids):
            ids.append(j[0])
            proshel_prog_inj_ochno_platno.append([j[0], j[6]])

        # Очно отдельная квота
        elif j[1] == '1' and j[2] == 'Отдельная квота' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Программная инженерия' and len(proshel_prog_inj_ochno_otdelnaya_kvota) <= 10 and (j[0] not in ids):
            ids.append(j[0])
            proshel_prog_inj_ochno_otdelnaya_kvota.append([j[0], j[6]])

        # Очно Особая квота
        elif j[1] == '1' and j[2] == 'Особая квота' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Программная инженерия' and len(proshel_prog_inj_ochno_osobaya_kvota) <= 10 and (j[0] not in ids):
            ids.append(j[0])
            proshel_prog_inj_ochno_osobaya_kvota.append([j[0], j[6]])


        # Прикладная информатика
        # Очно бюджет
        elif j[1] == '1' and j[2] == 'Основные места в рамках КЦП' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Прикладная информатика' and len(proshel_p_inf_ochno_budjet) <= 130 and (j[0] not in ids):
            ids.append(j[0])
            proshel_p_inf_ochno_budjet.append([j[0], j[6]])

        # Очно платно
        elif j[1] == '1' and j[2] == 'Платно' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Прикладная информатика' and len(proshel_p_inf_ochno_platno) <= 160 and (j[0] not in ids):
            ids.append(j[0])
            proshel_p_inf_ochno_platno.append([j[0], j[6]])

        # Очно отдельная квота
        elif j[1] == '1' and j[2] == 'Отдельная квота' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Прикладная информатика' and len(proshel_p_inf_ochno_otdelnaya_kvota) <= 17 and (j[0] not in ids):
            ids.append(j[0])
            proshel_p_inf_ochno_otdelnaya_kvota.append([j[0], j[6]])

        # Очно Особая квота
        elif j[1] == '1' and j[2] == 'Отдельная квота' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Прикладная информатика' and len(proshel_p_inf_ochno_osobaya_kvota) <= 17 and (j[0] not in ids):
            ids.append(j[0])
            proshel_p_inf_ochno_osobaya_kvota.append([j[0], j[6]])

        # Заочно платно
        elif j[1] == '1' and j[2] == 'Платно' and j[3] == 'Заочно' and j[6] == str(i) \
        and j[7] == 'Прикладная информатика' and len(proshel_p_inf_zaochno) <= 90 and (j[0] not in ids):
            ids.append(j[0])
            proshel_p_inf_zaochno.append([j[0], j[6]])

        # Очно-заочно платно
        elif j[1] == '1' and j[2] == 'Платно' and j[3] == 'Очно-заочно' and j[6] == str(i) \
        and j[7] == 'Прикладная информатика' and len(proshel_p_inf_ochnozaochno) <= 100 and (j[0] not in ids):
            ids.append(j[0])
            proshel_p_inf_ochnozaochno.append([j[0], j[6]])


        # Прикладной ИИ
        # Очно бюджет
        elif j[1] == '1' and j[2] == 'Основные места в рамках КЦП' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Прикладной ИИ' and len(proshel_pii_ochno_budjet) <= 75 and (j[0] not in ids):
            ids.append(j[0])
            proshel_pii_ochno_budjet.append([j[0], j[6]])

        # Очно платно
        elif j[1] == '1' and j[2] == 'Платно' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Прикладной ИИ' and len(proshel_pii_ochno_platno) <= 45 and (j[0] not in ids):
            ids.append(j[0])
            proshel_pii_ochno_platno.append([j[0], j[6]])

        # Очно отдельная квота
        elif j[1] == '1' and j[2] == 'Отдельная квота' and j[3] == 'Очно' and j[6] == str(i) and \
        j[7] == 'Прикладной ИИ' and len(proshel_pii_ochno_otdelnaya_kvota) <= 10 and (j[0] not in ids):
            ids.append(j[0])
            proshel_pii_ochno_otdelnaya_kvota.append([j[0], j[6]])

        # Очно Особая квота
        elif j[1] == '1' and j[2] == 'Особая квота' and j[3] == 'Очно' and j[6] == str(i) and \
        j[7] == 'Прикладной ИИ' and len(proshel_pii_ochno_osobaya_kvota) <= 10 and (j[0] not in ids):
            ids.append(j[0])
            proshel_pii_ochno_osobaya_kvota.append([j[0], j[6]])


        # Алгоритмы ИИ
        # Очно бюджет
        elif j[1] == '1' and j[2] == 'Основные места в рамках КЦП' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Алгоритмы ИИ' and len(proshel_aii_ochno_budjet) <= 80 and (j[0] not in ids):
            ids.append(j[0])
            proshel_aii_ochno_budjet.append([j[0], j[6]])

        # Очно платно
        elif j[1] == '1' and j[2] == 'Платно' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Алгоритмы ИИ' and len(proshel_aii_ochno_platno) <= 80 and (j[0] not in ids):
            ids.append(j[0])
            proshel_aii_ochno_platno.append([j[0], j[6]])

        # Очно отдельная квота
        elif j[1] == '1' and j[2] == 'Отдельная квота' and j[3] == 'Очно' and j[6] == str(i) and \
        j[7] == 'Алгоритмы ИИ' and len(proshel_aii_ochno_otdelnaya_kvota) <= 10 and (j[0] not in ids):
            ids.append(j[0])
            proshel_aii_ochno_otdelnaya_kvota.append([j[0], j[6]])

        # Очно Особая квота
        elif j[1] == '1' and j[2] == 'Особая квота' and j[3] == 'Очно' and j[6] == str(i) and \
        j[7] == 'Алгоритмы ИИ' and len(proshel_aii_ochno_osobaya_kvota) <= 10 and (j[0] not in ids):
            ids.append(j[0])
            proshel_aii_ochno_osobaya_kvota.append([j[0], j[6]])


        # Безопасность компьютерных систем
        # Очно бюджет
        elif j[1] == '1' and j[2] == 'Основные места в рамках КЦП' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Безопасность компьютерных систем' and len(proshel_bks_ochno_budjet) <= 88 and (j[0] not in ids):
            ids.append(j[0])
            proshel_bks_ochno_budjet.append([j[0], j[6]])

        # Очно платно
        elif j[1] == '1' and j[2] == 'Платно' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Безопасность компьютерных систем' and len(proshel_bks_ochno_platno) <= 75 and (j[0] not in ids):
            ids.append(j[0])
            proshel_bks_ochno_platno.append([j[0], j[6]])

        # Очно отдельная квота
        elif j[1] == '1' and j[2] == 'Отдельная квота' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Безопасность компьютерных систем' and len(proshel_bks_ochno_otdelnaya_kvota) <= 11 and (j[0] not in ids):
            ids.append(j[0])
            proshel_bks_ochno_otdelnaya_kvota.append([j[0], j[6]])

        # Очно Особая квота
        elif j[1] == '1' and j[2] == 'Отдельная квота' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Безопасность компьютерных систем' and len(proshel_bks_ochno_osobaya_kvota) <= 11 and (j[0] not in ids):
            ids.append(j[0])
            proshel_bks_ochno_osobaya_kvota.append([j[0], j[6]])

        # Очно-заочно платно
        elif j[1] == '1' and j[2] == 'Платно' and j[3] == 'Очно-заочно' and j[6] == str(i) \
        and j[7] == 'Безопасность компьютерных систем' and len(proshel_bks_ochnozaochno) <= 50 and (j[0] not in ids):
            ids.append(j[0])
            proshel_bks_ochnozaochno.append([j[0], j[6]])


        # Инфокоммуникационные технологии и системы связи
        # Очно бюджет
        elif j[1] == '1' and j[2] == 'Основные места в рамках КЦП' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Инфокоммуникационные технологии и системы связи' and len(proshel_itss_ochno_budjet) <= 48 and (j[0] not in ids):
            ids.append(j[0])
            proshel_itss_ochno_budjet.append([j[0], j[6]])

        # Очно платно
        elif j[1] == '1' and j[2] == 'Платно' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Инфокоммуникационные технологии и системы связи' and len(proshel_itss_ochno_platno) <= 10 and (j[0] not in ids):
            ids.append(j[0])
            proshel_itss_ochno_platno.append([j[0], j[6]])

        # Очно отдельная квота
        elif j[1] == '1' and j[2] == 'Отдельная квота' and j[3] == 'Очно' and j[6] == str(i) and \
        j[7] == 'Инфокоммуникационные технологии и системы связи' and len(proshel_itss_ochno_osobaya_kvota) <= 6 and (j[0] not in ids):
            ids.append(j[0])
            proshel_itss_ochno_osobaya_kvota.append([j[0], j[6]])

        # Очно Особая квота
        elif j[1] == '1' and j[2] == 'Особая квота' and j[3] == 'Очно' and j[6] == str(i) and \
        j[7] == 'Инфокоммуникационные технологии и системы связи' and len(proshel_itss_ochno_otdelnaya_kvota) <= 6 and (j[0] not in ids):
            ids.append(j[0])
            proshel_itss_ochno_otdelnaya_kvota.append([j[0], j[6]])


        # Конструирование и технология электронных средств
        # Очно бюджет
        elif j[1] == '1' and j[2] == 'Основные места в рамках КЦП' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Конструирование и технология электронных средств' and len(proshel_ktes_ochno_budjet) <= 58 and (j[0] not in ids):
            ids.append(j[0])
            proshel_ktes_ochno_budjet.append([j[0], j[6]])

        # Очно платно
        elif j[1] == '1' and j[2] == 'Платно' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Конструирование и технология электронных средств' and len(proshel_ktes_ochno_platno) <= 6 and (j[0] not in ids):
            ids.append(j[0])
            proshel_ktes_ochno_platno.append([j[0], j[6]])

        # Очно отдельная квота
        elif j[1] == '1' and j[2] == 'Отдельная квота' and j[3] == 'Очно' and j[6] == str(i) and \
        j[7] == 'Конструирование и технология электронных средств' and len(proshel_ktes_ochno_otdelnaya_kvota) <= 8 and (j[0] not in ids):
            ids.append(j[0])
            proshel_ktes_ochno_otdelnaya_kvota.append([j[0], j[6]])

        # Очно Особая квота
        elif j[1] == '1' and j[2] == 'Особая квота' and j[3] == 'Очно' and j[6] == str(i) and \
        j[7] == 'Конструирование и технология электронных средств' and len(proshel_ktes_ochno_osobaya_kvota) <= 8 and (j[0] not in ids):
            ids.append(j[0])
            proshel_ktes_ochno_osobaya_kvota.append([j[0], j[6]])


        # Технология полиграфического и упаковочного производства
        # Очно бюджет
        elif j[1] == '1' and j[2] == 'Основные места в рамках КЦП' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Технология полиграфического и упаковочного производства' and len(proshel_tpup_ochno_budjet) <= 35 and (j[0] not in ids):
            ids.append(j[0])
            proshel_tpup_ochno_budjet.append([j[0], j[6]])
        # Очно платно
        elif j[1] == '1' and j[2] == 'Платно' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Технология полиграфического и упаковочного производства' and len(proshel_tpup_ochno_platno) <= 20 and (j[0] not in ids):
            ids.append(j[0])
            proshel_tpup_ochno_platno.append([j[0], j[6]])

        # Очно отдельная квота
        elif j[1] == '1' and j[2] == 'Отдельная квота' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Технология полиграфического и упаковочного производства' and len(proshel_tpup_ochno_otdelnaya_kvota) <= 5 and (j[0] not in ids):
            ids.append(j[0])
            proshel_tpup_ochno_otdelnaya_kvota.append([j[0], j[6]])

        # Очно Особая квота
        elif j[1] == '1' and j[2] == 'Особая квота' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Технология полиграфического и упаковочного производства' and len(proshel_tpup_ochno_osobaya_kvota) <= 5 and (j[0] not in ids):
            ids.append(j[0])
            proshel_tpup_ochno_osobaya_kvota.append([j[0], j[6]])


        # Управление в технических системах
        # Очно бюджет
        elif j[1] == '1' and j[2] == 'Основные места в рамках КЦП' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Управление в технических системах' and len(proshel_uts_ochno_budjet) <= 40 and (j[0] not in ids):
            ids.append(j[0])
            proshel_uts_ochno_budjet.append([j[0], j[6]])
        # Очно платно
        elif j[1] == '1' and j[2] == 'Платно' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Управление в технических системах' and len(proshel_uts_ochno_platno) <= 6 and (j[0] not in ids):
            ids.append(j[0])
            proshel_uts_ochno_platno.append([j[0], j[6]])

        # Очно отдельная квота
        elif j[1] == '1' and j[2] == 'Отдельная квота' and j[3] == 'Очно' and j[6] == str(i) and \
        j[7] == 'Управление в технических системах' and len(proshel_uts_ochno_otdelnaya_kvota) <= 5 and (j[0] not in ids):
            ids.append(j[0])
            proshel_uts_ochno_otdelnaya_kvota.append([j[0], j[6]])

        # Очно Особая квота
        elif j[1] == '1' and j[2] == 'Особая квота' and j[3] == 'Очно' and j[6] == str(i) and \
        j[7] == 'Управление в технических системах' and len(proshel_uts_ochno_osobaya_kvota) <= 5 and (j[0] not in ids):
            ids.append(j[0])
            proshel_uts_ochno_osobaya_kvota.append([j[0], j[6]])


        # Информатика и вычислительная техника
        # Очно бюджет
        elif j[1] == '1' and j[2] == 'Основные места в рамках КЦП' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Информатика и вычислительная техника' and len(proshel_ivt_ochno_budjet) <= 160 and (j[0] not in ids):
            ids.append(j[0])
            proshel_ivt_ochno_budjet.append([j[0], j[6]])
        # Очно платно
        elif j[1] == '1' and j[2] == 'Платно' and j[3] == 'Очно' and j[6] == str(i) \
        and j[7] == 'Информатика и вычислительная техника' and len(proshel_ivt_ochno_platno) <= 125 and (j[0] not in ids):
            ids.append(j[0])
            proshel_ivt_ochno_platno.append([j[0], j[6]])

        # Очно отдельная квота
        elif j[1] == '1' and j[2] == 'Отдельная квота' and j[3] == 'Очно' and j[6] == str(i) and \
        j[7] == 'Информатика и вычислительная техника' and len(proshel_ivt_ochno_otdelnaya_kvota) <= 20 and (j[0] not in ids):
            ids.append(j[0])
            proshel_ivt_ochno_otdelnaya_kvota.append([j[0], j[6]])

        # Очно Особая квота
        elif j[1] == '1' and j[2] == 'Особая квота' and j[3] == 'Очно' and j[6] == str(i) and \
        j[7] == 'Информатика и вычислительная техника' and len(proshel_ivt_ochno_osobaya_kvota) <= 20 and (j[0] not in ids):
            ids.append(j[0])
            proshel_ivt_ochno_osobaya_kvota.append([j[0], j[6]])

        # Заочно квота
        elif j[1] == '1' and j[2] == 'Платно' and j[3] == 'Заочно' and j[6] == str(i) and \
        j[7] == 'Информатика и вычислительная техника' and len(proshel_ivt_zaochno) <= 20 and (j[0] not in ids):
            ids.append(j[0])
            proshel_ivt_zaochno.append([j[0], j[6]])

def akt_proh(s):
    s = s.replace('0', '0️⃣')
    s = s.replace('1', '1️⃣')
    s = s.replace('2', '2️⃣')
    s = s.replace('3', '3️⃣')
    s = s.replace('4', '4️⃣')
    s = s.replace('5', '5️⃣')
    s = s.replace('6', '6️⃣')
    s = s.replace('7', '7️⃣')
    s = s.replace('8', '8️⃣')
    s = s.replace('9', '9️⃣')
    return s


start_info = InlineKeyboardButton(text='Информация', callback_data='info')
start_chats = InlineKeyboardButton(text='Чаты', callback_data='chats')
start_lists = InlineKeyboardButton(text='Списки', callback_data='lists')

start_m = [[start_info], [start_chats], [start_lists]]
start_markup = InlineKeyboardMarkup(inline_keyboard=start_m)

# info_m = [[info_urfu], [info_irit_rtf], [info_priem_rtf], info_vk_rtf]
# info_markup = InlineKeyboardMarkup(inline_keyboard=info_m)
@dp.message()
async def msg(message: Message):
    if message.text == '/start':
        await message.answer(text='Приветствую! Что тебя интересует?', reply_markup=start_markup)
    else:
        o = 0
        aktualniy_prohodnoi = 0
        q = ''
        user_id = message.text
        for l in lists:
            for i in range(1, len(l)):
                if l[i][0] == user_id:
                    q += f'На данный момент вы проходите на направление \n\n {l[0]}'
                    q += f'\n\nВаше место в рейтинге: {i}\n'
                    for j in range(1, len(l)):
                        if i != j: q += f'\n ⏺ {str(j)}) ' + ' '.join(l[j])
                        if i == j: q += f'\n ✅ {str(j)}) ' + ' '.join(l[j])
                        aktualniy_prohodnoi = l[j][1]
                    o = 1
        if o == 1:
            q += f'\n\n🌟 Актуальный проходной балл на прогрмамму: {akt_proh(aktualniy_prohodnoi)}'
            q += f'\n\n❗ Помните, что списки могут быстро изменяться несколько раз в день. Важно учитывать, что ваше нахождение в них не гарантирует поступление, а лишь прогнозирует его'
            await message.reply(text=q)
        if o == 0:
            await message.reply(text='❎ Похоже, вас нет в списках')


@dp.callback_query()
async def cb_data(callback: CallbackQuery):
    if callback.data == 'lists':
        await callback.message.answer(text='✏️ Введи свой идентификационный номер')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())