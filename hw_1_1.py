#Количество дней от Рождества Хрестового до начала курса (19.08.2018)
DATE_OF_PY = (2018 * 12 * 30) + (11 * 30) + 19

# Ввод имени и фамилии, приветствие
name = input("Enter your nama: ")
surname = input("Enter your surname: ")
print("Hello, ",surname,name)

#Ввод даты рождения и подсчет количества дней от Рождества Хрестового до дня рождения
bday_day = int(input("Enter day of your B-DAY: "))
bday_month = int(input("Enter month of your B-DAY: "))
bday_year = int(input("Enter year of your B-DAY: "))

date_of_bday = (bday_year * 12 * 30) + (bday_month * 30) + bday_day

#Ввод сегодняшней даты и подсчет количества дней от Рождества Хрестового до сегодняшнего дня
today_day = int(input("Enter day of today: "))
today_month = int(input("Enter todays month: "))
today_year = int(input("Enter todays year: "))

date_of_today = (today_year * 12 * 30) + (today_month * 30) + today_day

#Количество прожитых дней/месяцов/лет
old_day =  date_of_today - date_of_bday
old_month = old_day // 30
old_year = old_month // 12
print("You {} moth old".format(old_month))
print("You {} year old".format(old_year))

# Количество мучительных дней/месяцей/лет от рождения до начала курса
wait_day = DATE_OF_PY - date_of_bday
wait_month = wait_day // 30
wait_year = wait_month // 12
all_wait_month = wait_month % 12
all_wait_day = wait_day & 30

print("{}, you wait for Python {} day or {} month or {} year, this is {} day {} month {} year of your life".format(name, \
    wait_day,wait_month,wait_year,all_wait_day,all_wait_month,wait_year))
#Погрешность получается из-за не учета высокосных годов и усредньоного количества дней в месяце