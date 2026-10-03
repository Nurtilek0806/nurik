# name = "Нуртилек"
# age = 27
# city = "Баткен обл. Баткен р-ну. Самаркандек айылы Адилет көч №52"

# print(name)
# print(age)
# print(city)

# a = int(input("Биринчи сан:"))
# b = int(input("Экинчи сан:"))
# c = int(input("Үчүнчү сан:"))
# d = int(input("Төртүнчү сан"))

# print("Кошуу", a + b)
# print("Кемитүү", a - b)
# print("Көбөйтү", a * b)
# print("Бөлүү", a / b,)
# print("Узундугу менен Туурасы", (a*b))
# print("Аянты жана Периметири", (2*(a+b)))

# print ("Салам алейкум")

# jash = int(input("Жашыңызды кириңиз:"))

# if jash <= 18:
#     print("Кирүүгө уруксат берилет!")

# else:
#     print("Кирүүгө мүмкүн эмес")

# ball = int(input("Топтогон баллды киргизиңиз (0-100):"))

# if ball < 0 or ball > 100:
#         print("Ката: Мындай балл болушу мүмкүн эмес! 0 менен 100дүн ортосундагы санды жазыңыз")
# elif ball >= 90:
#         print("Сиздин бааңыз: 5 (эң жакшы)")
# elif ball >= 75:
#         print("Сиздин бааңыз: 4 (жакшы)")
# elif ball >= 50:
#         print("Сиздин алган бааңыз: 3 (канаттандырарлык)")
# else:
#         print("Сиздин бааңыз: 2 (канааттандырарлык эмес, дагын арекет кылыңыз)")
    
# jup = int(input("Бир сан жазыңыз"))

# if jup % 6 == 0:
#     print("Жуп сан")
# else:
#     print("Так сан")


# jash = int(input("Жашыңызды киргизиңиз! "))

# if jash > 7 == 0:
#     print(f"Сизге билет бекер, Баасы: {kb} сом")

# else:
#     print("Билеттин баасы, 250 сом ")
# butun_san = int(input("Бир бүтүн санды жазыңыз! "))

# if butun_san < 0 > 0.5:
#     print(f"Бул оң (позитивдүү)сан")

# else:
#     print("Бул нөл сан") 


# print( " --- Таанышуу ---")

# aty = input("Атыңды жаз: ")
# shaary = input("Кайсыл жерден болосуң? ")
# ishtegen = input("Жумуш жериңди толук жаз? ")
# print(f"Салам, {aty}! Сен {shaary} Шаарынан экенсиң {ishtegen } Жумуш жериңди толук жаз. \n")

# print("---3. Тик бурчтук ---")
# uzundugu = float(input("Узундугун (a) киргизиңиз: "))
# tuurasy = float(input("Туурасын (b) киргизиңиз: "))

# ayanty = uzundugu * tuurasy
# perimetri = 2 * (uzundugu + tuurasy)

# print(f"Аянты (a * b): {ayanty}")
# print("Периметри (2 * (a + b)): {perimetri} \n")

# print("---5. Кассир ---")
# baasy = float(input("Товардын баасыны киргизиңиз: "))
# sany = int(input("Товардын санын киргизиңиз: "))

# jalpy_summa = baasy * sany
# arzandatuu = jalpy_summa * 0.10
# tolo_summasy = jalpy_summa - arzandatuu

# print(f"Жалпы баштапкы суммасы: {jalpy_summa} сом")
# print(f"10% арзандатуу: {arzandatuu} сом")
# print(f"Арзандатуу менен төлөнүүчү акыркы сумма: {tolo_summasy} сом")

# ---4.Парол текшерүү ---
# aty ="Nurtılek_571"
# menin_syr_sozum ="0806"
# syr_log =input("Лигиниңизди киргизиңиз:")
# syr_soz =input("Паролуңузду киргизиңиз:")

# if syr_log == aty and syr_soz == menin_syr_sozum:
#     print("Кош келдиңиз!")
# elif syr_soz != aty and syr_log == menin_syr_sozum:
#     print("Логиниңизди киргизгенде катачылык бар, Кайра жазып көрүңүз")
# elif syr_log == aty and syr_soz != menin_syr_sozum:
#     print("Паролуңузду киргизгенде катачылыктар бар, Кайрадан жазып көрүңуз!")

# else:
#     print("Логин катасы, Парол катасы")

# count = 1 
# while count <= 5:
#     print(count)
#     count += 1


# for i in range(010):
#     if i == 5:
#         break
#     print(i)

# for i in range (5):
#     if i == 2:
#         continue
#         print(i)

# n = 8
# for i in range (1, 11):
#     print(f"{n} * {i} = {n * i}")

# marks = [5, 4, 3, 5, 4,]
# total = 0
# for m in marks:
#     total += m
#     print("Сумма:", total)
#     print("Орточо", total / len (marks))

# i = 1
# while i <= 5:
#     print(i)
#     i +=1
# for i in range(1, 31,3):
#         print(i)
# for i in range(1, 11, 1):
#     print(i)

# summa = 0

# for i in range(1, 11):
#     summa += i

# print(summa)

# men = "Мен Абдикаллаков Нуртилек Жоробаевич 1999-жылы 8-Июньда Баткен обл. Баткен р-ну. Самаркандек айылында Карапайым үй-бүлөдо жарык дүйнөгө келгем"
# natyija = "Жаш"
# a = 2026
# b = 1999
# c = a - b 
# print(men)
# print("Менин жашым:", c, natyija)

