# 293 zapis binarny:
print(bin(5))
print((int(0b101)))

#294 zmienne:
a, b, c = 1, 7, 4

print(a)
print(b)
print(c)

# 295 Expressions vs Statements:

iq = 100
user_age = iq / 5  #statement (wypowiedz oświadczenie - cała linijka kodu)
iq / 5 #expression (wyraenie)

# 296 Augmented assignment operator
# Augmented - wzmocniony, rozszerzony

some_value = 5
some_value += 3
print(some_value)

# 300 Escape sequence
# kolejny symbol po \ będzie traktowany jako string 
weather = "It'\s \"kind of\" sunny"

# \t - tabulator
# \n - nowa linia

weather = "\t It'\s \"kind of\" sunny \n hope you have a good day!"
print(weather)

#301 Formatted strings

name = "Johny"
age = 55

# formatowanie od Python 3.0:
print(f'Hi {name}. You are {age} years old')

# stare formatowanie:
print('Hi {}. You are {} years old'.format(name, age))


#302 String Indexes

selfish = '01234567'
# [start:stop:stepover]
print(selfish[0:8:2])

# reverse order [::-1]
print(selfish[::-1])

# 303 String immutability

selfish = '01234567'
# selfish[1] = 100 takie cos zakonczy sie bledem, takie coś zakończy sie błędem poniewaz stringi są niemutowalne. 

# 304 Built-In Functions + Methods
# dane metody działają tylko na jednym typie danych np. na stringach

quote ="to be or not to be"

print(quote.upper()) #wszystko z wielkiej
print(quote.capitalize()) #pierwsza z wielkiej
print(quote.find('be')) #szuka string wewnatrz stringa i podaje ilosc jego wystepowan
print(quote.replace('be', 'me')) #zamienia be na me

# 305 Booleans
print(bool(0)) #fałsz
print(bool(1)) #prawda
print(bool(2000)) #prawda


# 308 Exercise: Password

name = "Jayjay"
password = "secret"
lenght = len(password)
hidden_password = lenght * '*'
print(f'{name}, your password {hidden_password} is {lenght} letters long')


# 309 Lists - MUTABLE

amazon_cart = ['notebooks', "sunglasses", "toys", "grapes"]

amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:] #przypisze do zmniennej calkiem nowa liste
new_cart[0] = 'gum'
print(new_cart) #['gum', 'sunglasses', 'toys', 'grapes']
print(amazon_cart) #['laptop', 'sunglasses', 'toys', 'grapes']


# 310 Matrix (Macierze)

matrix = [
    [1, 0, 9],
    [5, 2, 4],
    [1, 4, 8]
]

print(matrix[0][1]) #0
print(matrix[2][2]) #8


# 312 Lists methods

basket = [1, 2, 3, 4, 5, 30]

#adding:
basket.append(19) #doda nowa wartosc na koncu listy
new_list = basket
print(basket)
print(new_list)

basket.insert(3, 30) #doda nowa wartosc na 3 miejscu listy
new_list = basket
print(new_list)

basket.extend([100, 105])
new_list = basket
print(new_list)

#removing:

basket.pop()
print(basket)
basket.pop(0) #indeksujemy element ktory chcemu wyciac
print(basket)
druga_lista = basket.pop(1) #wycinamy element i przypisujemy go do zmiennej
print(druga_lista)

basket.remove(30) #podajemy pierwsza napotkana wartosc ktora chcemy usunac z listy
print(basket) 

basket.clear() #czyszczenie listy do zera
print(basket) 

#index
basket = ["a", "b", "c", "d", "e", "d"]

print(basket.index("b"))  #poda pod jakim indexem jest wartosc 2

print(basket.index("d",0, 4)) #mozemy podac od ktorego do ktorego indexu chcemy szukac

print("d" in basket) #sprawdza czy "d" jest wewnatatrz listy

print("x" in basket) #false bo "x" nie ma

print(basket.count("d")) #zlicza ilosc wystapien elementu na liscie

basket.sort() #sortuje elementy na liscie "w miejscu"
print(basket)

print(sorted(basket)) #sortuje elementy listy tworzac nowa, a pierwotna pozostawia bez zmian

new_basket = basket.copy() #kopiuje liste i przypisuje ja do nowej zmiennej

new_basket.reverse() #odwraca kolejnosc elementow na liscie, NIE SORTUJE 
print(new_basket) 

# 315 Common List Patterns

print(new_basket[::-1]) #inny sposob na odwrocenie kolejnosci elementow na liscie

print(len(new_basket)) #sprawdzenie dlugosci listy

print(list(range(20,26))) #wydrukuje liste z elementami od 20 do 25

print(list(range(101))) #wydrukuje liste od 0 do 100

sentence = "?"
new_sentence = sentence.join(["hi", "my", "name", "is", "Mati"]) #polaczy elementy z tej listy przy pomocy znaku z "sentence"
print(new_sentence) #hi?my?name?is?Mati

new_sentence = " ".join(["hi", "my", "name", "is", "Mati"]) #inny sposob na polaczenie 
print(new_sentence) #hi my name is Mati

# 316 List Unpacking

a, b, c, *pozostala_czesc, d = [1, 2, 3, 4, 5, 6, 7, 8, 9] #rozpakowywanie listy

print (a)
print(b)
print(c)
print(pozostala_czesc)
print(d)

# 317 None

weapons = None #tworzymy sobie pusta zmienna na pozniej
print(weapons)


# 318 Dictionaries

#slowniki sa nieuporzadkowane, nie mozemy sie dostac do ich wartosci przy pomocy indexu
#dostajemy wartosc ze swlonika podaja klucz

dictionary = {
    'a' : 1,
    'b' : 2
    }

print(dictionary['b']) #drukuje wartosc przypisana do klucza b

dictionary_2 = {
    'a' : [1, 2, 3],
    'b' : 'hello',
    'c' : True,
    }

print(dictionary_2['a'][1]) #drukuje drugi element z listy "a", czyli "2"
print(dictionary_2['b']) #drukuje "hello"

my_list = [
    {
    'a' : [1, 2, 3],
    'b' : 'hello',
    'c' : True
    },
    {
    'a' : [4, 5, 6],
    'b' : ['hello'],
    'x' : True
}
]

print(my_list[1]["a"][2]) #wydrukuje 6


# 320 Dictionary Keys

# klucze moga byc dowolnym niemutowalnym typem danych
#klucze musza byc unikatowe, inaczej ich wartosci sie nadpisuja

dictionary_3 = {
    False : [1, 2, 3],
    123 : "Jurek",
}

print(dictionary_3[False]) #wydrukuje [1, 2, 3]


#v321 Dictionary Methods

user = {
    'basket' : [1, 2, 3],
    'greet' : 'hello',
    'age' : 33
}

print(user.get('age')) #sprawdza zawartosc klucza 'age', jesli nie istnieje zwraca domyslnie 'None' zamiast error

print(user.get('age', 55)) #zamieniamy 'None' na 55. Wydrukuje '55'

user_2 = dict(name = "Mateusz") #metoda tworzenia listy
print(user_2) #wydrukuje liste: {'name': 'Mateusz'}

print('basket' in user) #sprawdzamy, czy dany klucz jest w slowniku - True
print('size' in user) #False

print('age' in user.keys()) #sprawdza czy w slowniku jest klucz 'age'. True

print(user.items()) #items - to klucz i wartosc na raz. Ta metoda wydrukuje calosc zawartosc slownika w postaci tuple

user_2 = user.copy() #skopiowanie slownika

(user.clear()) #czysci slownik do {}
print(user)
print(user_2)

print(user_2.pop('age')) #drukuje wartosc przypisana do klucza 'age', czyli 33
print(user_2) #drukuje slownik juz bez klucza 'age'

#print(user.popitem()) #wycina losowo wybrane pare klucz:wartosc poniewaz slownik nie jest indexowany

user_2.update({'greet':'byebye'}) #przypisze nowa wartosc do klucze 'greet'
print(user_2)

user_2.update({'country':'Poland'}) #doda do slownika nowa pare klucz:wartosc
print(user_2)

user_profile = {
    'age': 0,
    'username': ' ',
    'weapons': None,
    'is_active': False,
    'clan': None
}

print(user_profile.keys()) #wydrukuje wszystkie klucze w slowniku

user_profile.update({'weapons' : 'shotgun'})

user_profile.update({'is_banned' : False})
print(user_profile)

user_profile['is_banned'] = True #inny sposob przypisania wartosci do klucza
print(user_profile)

new_user_2 = user_profile.copy()
new_user_2.update({'age' : 23,'username': 'Jurek'})
print(new_user_2)

# 323 Tuples

my_tuple = (1, 2, 3, 4, 5) #tuple jest immutable, ale indexowana jak lista
print(my_tuple[1]) #printuje 2

print(5 in my_tuple) #true

user_3 = {
    (1, 2) : [1, 2, 3], #krotka moze byc kluczem w slowniku
    'greet' : 'hi'
}

print(user_3[(1, 2)]) #printuje [1, 2, 3]

new_tuple = my_tuple[1:2] #wydrukuje (2,) - ten przecinek jest ok
print(new_tuple)

x, y, z, *other = (1, 2, 3, 4, 5)
print(x)
print(*other)

print(my_tuple.count(5)) #zlicza wystepowanie wartosci '5'
print(my_tuple.index(3)) #podaje index wartosci '3'
print(len(my_tuple)) #podaje dlugosc tuple


#325 Sets

# sety posiadają unikalne wartosci ktore sa nieuporzadkowane. Przypominaja zbiory na matematyce

my_set = {1, 2, 3, 4, 5, 4, 5, 5}
print(my_set) #{1, 2, 3, 4, 5} 
print(len(my_set)) #drukuje 5, poniewaz nie liczy duplikatow

# usuniecie zduplikowanych wartosci z listy poprzez zamiane jej na set:
my_list = [1, 2, 3, 4, 4,4, 5, 5]
print(set(my_list)) #{1, 2, 3, 4, 5}


# Do różnicy A∖B zaliczamy wszystkie liczby, które wchodzą w skład zbioru A i nie wchodzą w skład zbioru B:

my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

print(my_set.difference(your_set)) #{1, 2, 3}


# Usuniecie elementu ze zbioru:
my_set.discard(5)
print(my_set) #{1, 2, 3, 4}

# my_set.difference_update(your_set) #usuwa z pierwszego seta wszystkie elementy drugiego
# print(my_set)

# intersection (skrzyzowanie/przeciecie). W PL to jest chyba iloczyn zbiorów
#Do iloczynu A∩B zaliczamy wszystkie liczby, które są jednocześnie w zbiorze A i w zbiorze B.

print(my_set.intersection(your_set)) #4
print(my_set & your_set) #mozna to zapisac takze w taki sposob


#disjoint (True jezeli sety nie maja wspolnych czesci, False jesli maja)
print(my_set.isdisjoint(your_set)) #Falsce bo maja wspolne '4'


# union - dodaje dwa sety do siebie, ale usuwa duplikujace sie wartosci
print(my_set.union(your_set)) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(my_set | your_set) #mozna to zapisac takze w taki sposob


#issubset - #sprawdza, czy pierwszy zbior jest podzbiorem drugiego (miesci sie w nim)
my_set_2 = {4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
print(my_set_2.issubset(your_set)) #True


school = {'Bobby','Tammy','Jammy','Sally','Danny'}
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']
print(school.difference(attendance_list))


#330 Truthy vs Falsey

print(bool(5)) #True
print(bool("Jurek")) #True

print(bool(0)) #False
print(bool("")) #False


#331 Ternary Operator (Operator trójskładnikowy)

# condition_if_true if condition else condition_if_else:

is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message) #printuje "message allowed"

is_friend = False
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message) #not allowed to message"


#334 Exercise: Logical Operators

is_magician = False
is_expert = True

if is_magician and is_expert:
    print("You are a master magician")
elif is_magician and not is_expert:
    print("at least you're getting there")
elif not is_magician:
    print("You need magic powers")


#335 IS VS ==
    
print(True == 1) #True
print('' == 1) #False
print([] == 1) #False
print(10 == 10.0) #True
print([] == []) #True

print(True is True) #True
print('1' is '1') #True
print([] is []) #False
print(10 is 10.0) #True
print([] is []) #True


#336 LOOPS

# for loop

for item in "Akumamatata": #dziala takze na liscie, zbiorze i tupli
    print(item)

for item in "Akumamatatu":
    print(item)
    print(item)
    print(item)
print(item) #wydrukuje "u" po raz czwarty, poniewaz do "item" zostanie przypisany ostatni element po zakonczonej iteracji


for item in (1, 2, 3, 4, 5):
    for x in ["a", "b", "c"]:
        print(item, x)


# ITERABLES
        
#iterable: list, dictionary, tuple, set, string
        
user = {
    "name" : "Golem",
    "age" : 5006,
    "can_swim" : False

}

for y in user:
    print(y)  #wydrukuje tylko klucze!

for y in user.items():
    print(y)  #wydrukuje pary klucz:wartosc

for y in user.values():
    print(y)  #wydrukuje tylko wartosci


for y in user.items():
    key, value = y;
    print(key, value) #wydrukuje pary klucz:wartosc

for key, value in user.items():
    print(key, value) #wydrukuje pary klucz:wartosc - LEPSZY SPOSOB


#counter:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma = 0
for i in my_list:
    suma += i
print(suma)


#339 RANGE

for number in range(0,100):
    print(number) #wydrukuje liczby kazda w nowej linii od 0 do 99

#deklaracja kroku:
for number in range(0, 10, 2): 
    print(number) #skok wartosci co 2 zaczynajac od 0

#range od najwiekszej do najmniejszej wartosci:
for number in range(10, 0, -1):
    print(number)

for _ in range(2):
    print(list(range(10))) #wyprintuje 2 listy 10 elementowe

#340 ENUMERATE (ang. wyliczac)
    
for i, char in enumerate("Helllooo"):
    print(i, char) #wydrukuje index po czym litere do niego przypisana np "0 H" itd.


#sprawdzenie pod jakim indexem jest zapisana liczna "50":
    
for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f"index of 50 is: {i}") #wydrukuje: index of 50 is: 50


#340 WHILE LOOP (ang. podczas)
        
# break - konczy dzialanie loop'a

i = 0
while i < 50:
    print(i)
    i += 1
else:
    print('done with all the work') #wydrukuje liczby a potem tego stringa


i = 0
while i < 50:
    print(i)
    i += 1
    break #zakonczy dzialanie petli while i "else" nie zostanie wykonane
else:
    print('done with all the work') #wydrukuje liczby a potem tego stringa


# for vs while:

my_list = [1, 2, 3]
for item in my_list:
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1


# BREAK, CONTINUE, PASS

# continue - po wykonaniu wraca na poczatek petli:

my_list = [1, 2, 3]
for item in my_list:
    continue
    print(item) #nie wydrukuje tego, poniewaz po powyzszym continue program wroci na poczatek petli


i = 0    
while i < len(my_list):
    i += 1
    continue
    print("UGABUGA") #nie wydrukuje tego, poniewaz po powyzszym continue program wroci na poczatek petli


# pass - nie robi nic, pokazujemy tylko w petli, ze myslimy nad tym fragmentem kodu i moze cos tam dopiszemy w przyszlosci. Wstawiamy go, zeby error nie wyskoczyl

my_list = [1, 2, 3]
for item in my_list:
    pass #myslimy nad tym, zostawiamy na pozniej 


#344 Our first GUI

#Exercise!

# Display the image below to the right hand side where the 0 is going to be ' ',
# and the 1 is going to be '*'. 

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
 

for row in picture:
    for pixel in row:
        if (pixel ==1):
            print('*', end ='')
        else:
            print(" ", end ='')
    print('') #po zakonczeniu petli przejdzie do nastepnej linii, drukujac pustego stringa


#346 FIND DUPLICATES

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)


#347 FUNCTIONS

def show_tree():
    for row in picture:
        for pixel in row:
            if (pixel ==1):
                print('*', end ='')
            else:
                print(" ", end ='')
        print('')
    
show_tree()
show_tree()
show_tree()


#348 PARAMETERS AND ARGUMENTS:

# positional parameters:
def say_hello(name, emoji):
    print(f'hellllooooo {name} {emoji}')

# positional arguments - kolejnosc podawania argumentow ma znaczenie:
say_hello('Andrei',':)') #call albo invoke - tak sie mowi na wywolanie funkcji


#349 DEFAULT PARAMETERS AND KEYWORD ARGUMENTS:

# default parameters: 
def say_hello(name = "Darth Vader", emoji = ':('):
    print(f"Helooooo {name}{emoji}")

# keywords arguments:
say_hello(name = "Bobi", emoji = ":D")

say_hello() #wywola funkcje z domyslnymi argumentami zadefiniowanymi podczas tworzenia funkcji


#350 RETURN

# bez "return":

def suma(num_1, num_2):
    num_1 + num_2

print(suma(4,5)) #takie coś wydrukuje None, poniewaz funkcja nie zwraca wartosci

# z "return":

def suma(num_1, num_2):
    return num_1 + num_2
    # function should do one thing really well.
    # function should return something

print(suma(4,5)) #print 9, poniewaz funkcja zwrocila wartosc


# def sum(num_1, num_2):
#     return num_1 + num_2 

# total = sum(10, 5)
# print(sum(10, total)) #drukuje 25, poniewaz zwrocilo 15 i wstawilo je do funkcji w miejsce zmiennej total

# print(sum(10, sum(10, 5))) #inny zapis dwoch powyzszych linijek

# def sum(num_1, num_2):
#     def another_function(n_1, n_2): #ta funcja sie tu nie odpala, tylko zostala zdefiniowana
#         return num_1 + num_2
#     return another_function(num_1, num_2) #tutaj dopiero wywolanie drugiej funkcji wiec wykonywanie kodu "sie cofnie"

# total = sum(10, 40)
# print(total) #50


#351 TESLA CODE EXERCISE

def checkDriverAge(age = 0):

    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge(2)

#353 DOCSTRINGS

def test(a):
    """
    Info: this function tests and prints param "a"
    """

test(25) #po najechaniu kursorem na nazwe funkcji wyswietli sie jej opis
# help(test) - ta linijka wydrukuje opis funkcji w terminalu
# print(test.__doc__) - drugi sposob na wydrukowanie opisu funkcji w termianlu


#354 CLEAN CODE

#najgorsza opcja:
def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 !=0:
        return False
    
#pierwsze uproszczenie:
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False   

#lepsze uproszczenie:
def is_even(num):
    if num % 2 == 0:
        return True
    return False   

#najlepsze rozwiazanie:
def is_even(num):
    return num % 2 == 0

def formatted_numbers():
    result = []

def formatted_numbers():
    result = []


#355 *ARGS AND **KWARGS
    
# *args (od arguments):

def super_func(*args): # *args pozwala podac wiele argumentow funkcji
    print(args)
    return sum(args)

print(super_func(1, 2, 3, 4, 5))

# **kwargs (od keywords):

def super_func(*args, **kwargs): # **kwargs pozawala w miejscu zmiennej wstawic wiele par kluczy
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1, 2, 3, 4, 5, num_1 = 5, num_2 = 10))

# !!! RULE !!!:
# definiujemy parametry funkcji w nastepujacej kolejnosci:
# params, *args, default parameters, **kwargs
def super_func_2(name, *args, i = 'hi', **kwargs):
    pass


#356 EXERCISE FUNCTION

def highest_even(list):
    evens = []
    for i in list:
        if i % 2 == 0:
            evens.append(i)
    return max(evens)

print(highest_even([11, 10, 2, 3, 4, 5, 8]))


#358 SCOPE RULES

#Scope - what variables do I have acces to?

a = 1

def parent():
    a = 10
    def confusion():
        return a
    return confusion()

print(parent())
print(a)
    
#359 GLOBAL KEYWORD




