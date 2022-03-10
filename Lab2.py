#!/usr/bin/env python
# coding: utf-8

# # Лабораторная работа №2 
# 
# ## Выполнил студент группы БСТ2003 Журавлёв Сергей Алексеевич
# 
# ## Задание №1

# ### Бинарный поиск

# In[2]:


def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index


# Бинарный поиск работает по принципу «разделяй и властвуй». Он быстрее, чем линейный поиск, но требует, чтобы массив был отсортирован перед выполнением алгоритма.
# 
# Предполагая, что мы ищем значение val в отсортированном массиве, алгоритм сравнивает val со значением среднего элемента массива, который мы будем называть mid.
# 
# Если mid — это тот элемент, который мы ищем (в лучшем случае), мы возвращаем его индекс.
# Если нет, мы определяем, в какой половине массива мы будем искать val дальше, основываясь на том, меньше или больше значение val значения mid, и отбрасываем вторую половину массива.
# Затем мы рекурсивно или итеративно выполняем те же шаги, выбирая новое значение для mid, сравнивая его с val и отбрасывая половину массива на каждой итерации алгоритма.
# Алгоритм бинарного поиска можно написать как рекурсивно, так и итеративно. В Python рекурсия обычно медленнее, потому что она требует выделения новых кадров стека.
# 
# Поскольку хороший алгоритм поиска должен быть максимально быстрым и точным, давайте рассмотрим итеративную реализацию бинарного поиска:

# ### Интерполяционный поиск

# In[3]:


def InterpolationSearch(lys, val):
    low = 0
    high = (len(lys) - 1)
    while low <= high and val >= lys[low] and val <= lys[high]:
        index = low + int(((float(high - low) / ( lys[high] - lys[low])) * ( val - lys[low])))
        if lys[index] == val:
            return index
        if lys[index] < val:
            low = index + 1;
        else:
            high = index - 1;
    return -1


# lys — наш входной массив.
# val — искомый элемент.
# index — вероятный индекс искомого элемента. Он вычисляется как более высокое значение, когда значение val ближе по значению к элементу в конце массива (lys[high]), и более низкое, когда значение val ближе по значению к элементу в начале массива (lys[low]).
# low — начальный индекс массива.
# high — последний индекс массива.
# Алгоритм осуществляет поиск путем вычисления значения индекса:
# 
# Если значение найдено (когда lys[index] == val), возвращается индекс.
# Если значение val меньше lys[index], то значение индекса пересчитывается по формуле для левого подмассива.
# Если значение val больше lys[index], то значение индекса пересчитывается по формуле для правого подмассива.

# ### Поиск Фибоначчи

# In[4]:


def FibonacciSearch(lys, val):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(lys)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1;
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(lys)-1))
        if (lys[i] < val):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (lys[i] > val):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else :
            return i
    if(fibM_minus_1 and index < (len(lys)-1) and lys[index+1] == val):
        return index+1;
    return -1


# Поиск Фибоначчи — это еще один алгоритм «разделяй и властвуй», который имеет сходство как с бинарным поиском, так и с jump search. Он получил свое название потому, что использует числа Фибоначчи для вычисления размера блока или диапазона поиска на каждом шаге.
# 
# Числа Фибоначчи  — это последовательность чисел 0, 1, 1, 2, 3, 5, 8, 13, 21 …, где каждый элемент является суммой двух предыдущих чисел.
# 
# Алгоритм работает с тремя числами Фибоначчи одновременно. Давайте назовем эти три числа fibM, fibM_minus_1 и fibM_minus_2. Где fibM_minus_1 и fibM_minus_2 — это два числа, предшествующих fibM в последовательности:
# 
# fibM = fibM_minus_1 + fibM_minus_2
# 
# Мы инициализируем значения 0, 1, 1 или первые три числа в последовательности Фибоначчи. Это поможет нам избежать  IndexError в случае, когда наш массив lys содержит очень маленькое количество элементов.
# 
# Затем мы выбираем наименьшее число последовательности Фибоначчи, которое больше или равно числу элементов в нашем массиве lys, в качестве значения fibM. А два числа Фибоначчи непосредственно перед ним — в качестве значений fibM_minus_1 и fibM_minus_2. Пока в массиве есть элементы и значение fibM больше единицы, мы:
# 
# Сравниваем val со значением блока в диапазоне до fibM_minus_2 и возвращаем индекс элемента, если он совпадает.
# Если значение больше, чем элемент, который мы в данный момент просматриваем, мы перемещаем значения fibM, fibM_minus_1 и fibM_minus_2 на два шага вниз в последовательности Фибоначчи и меняем индекс на индекс элемента.
# Если значение меньше, чем элемент, который мы в данный момент просматриваем, мы перемещаем значения fibM, fibM_minus_1 и fibM_minus_2 на один шаг вниз в последовательности Фибоначчи.

# ### Поиск "Бинарное дерево"

# In[ ]:


узел класса:

    def init(self, data):

        self.left = Нет
        self.right = Нет
        self.data = данные

     вставка def(self, data):

        если self.data:
            если данные < self.data:
                если self.left  нет:
                    self.left = узел(данные)
                ещё:
                    self.left.insert(данные)
             данные elif >> self.data:
                если self.right  нет:
                    self.right = узел(данные)
                ещё:
                    self.right.insert(данные)
        ещё:
            self.data = данные

    def val(self, lkpval):
        если lkpval < self.data:
            если self.left  нет:
                print(lkpval, "не найден.")
                возврат False
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            если self.right  нет:
                print(lkpval, "не найден.")
                возврат False
            вернуть self.right.findval(lkpval)
        ещё:
            print(self.data, ' найден.')
            верните True

    def PrintTree(self):
        если self.left:
            self.left.PrintTree()
        печать(self.data),
        если self.right:
            self.right.PrintTree()

def make_a_tree(обр.:
    root = Node(arr[0])
    для i в arr[1::]:
        root.insert(i)
    вернуть корень

 вставка def(mas):
    print("Хотите внести элемент? ")
    ans = input()
    if ans=="да" or ans =="Да":
        el = int(input("Введите число: "))
        index = int(input("Введите индекс: "))
        mas.insert(индекс, el)
        Печать(mas, n + 1)



 удаление def(mas):
    print("Хотите удалить элемент? ")
    ans = input()
    if ans == "да" or ans == "Да":
        index = int(input("Введите индекс: "))
        del mas[индекс]
        Печать(mas, n - 1)


# ### Задание №2
# 

# In[ ]:


def generate_array(length=100): # генерируем случайный массив
    массив = []
    в то время как len(массив) < длина:
        array.append(random.randint(0, 100))
    возвращаемый массив
#для хэша
класс ClassForRehash:
    def __init__(self, value1):
        self.value1 = value1
        self.hash = int(((value1 % ClassForRehash.MAX_HASH_TABLE) * 331) & 127) % ClassForRehash.MAX_HASH_TABLE)
        self.hashh = int(value1)

    MAX_HASH_TABLE = 8

# просто рехэширование
класс SimpleRehashTable:

    def init__(self, длина):
        self.table = [None] * длина

    def add_el(self, элемент):
        original_hash = element.hash
        если self.table[original_hash]  отсутствует:
            self.table[original_hash] = элемент
            print("объект со значением %i имеет хэш: %i (рехеширование не требовалось)"
                  % (self.table[original_hash].value1, element.hash))
            Возврат

        """""
 простое рехеширование
        """""
        new_hash = original_hash + 1
        while new_hash != original_hash:
            если new_hash >=> len(self.table):
                new_hash = 0
                продолжить
            если self.table[new_hash] равен None:
                element.hash = new_hash
                self.table[new_hash] = элемент
                print("объект со значением %i имеет хэш: %i (рехешировано. коллизия была в хеше: %i)"
                      % (self.table[new_hash].value1, element.hash, original_hash))
                Возврат
            new_hash += 1
        print("таблица заполнена!")
        Возврат
#вывод
simple_re = SimpleRehashTable(ClassForRehash.MAX_HASH_TABLE)
для i в диапазоне(len(simple_re.table) + 2):
    simple_re.add_el(ClassForRehash(random.randint(0, 8)))


#случайное

класс RandomRehashTable:

    def __init__(self, длина):
        self.table = [None] * длина

    def add_el(self, элемент):
        original_hash = element.hash
        если self.table[original_hash]  отсутствует:
            self.table[original_hash] = элемент
            print("объект со значением %i имеет хэш: %i (рехеширование не требовалось)"
                  % (self.table[original_hash].value1, original_hash))
            Возврат

        """""
 случайное рехеширование
        """""
        table_len = len(self.table)
        r = 1
        for ii in range(10): # range(число попыток определить новый хеш)
            r *= 5
            r = r % (4 * table_len)
            new_hash = r // 4
            если self.table[new_hash] равен None:
                element.hash = new_hash
                self.table[new_hash] = элемент
                print("объект со значением %i имеет хэш: %i (рехешировано. коллизия была в хеше: %i)"
                      % (self.table[new_hash].value1, element.hash, original_hash))
                Возврат
        print("Не удалось найти свободный хеш в таблице!")
        Возврат
#вывод
random_re = RandomRehashTable(ClassForRehash.MAX_HASH_TABLE)
для i в диапазоне(len(random_re.table) + 2):
    random_re.add_el(ClassForRehash(random.randint(0, 9)))

#метод цепочек
класс ChainRehashTable:

    def __init__(self, длина):
        self.table = [None] * длина
    def add_el(self, элемент):
        """""
 метод цепочек
        """""
        original_hash = element.hashh
        печать(element.hashh)
        если self.table[original_hash]  Нет:
            self.table[original_hash] = [элемент]
            Возврат
        ещё:
            self.table[original_hash].append(элемент)
            Возврат


# вывод
chain_re = ChainRehashTable(ClassForRehash.MAX_HASH_TABLE)
для i в диапазоне(len(chain_re.table)):
    chain_re.add_el(ClassForRehash(random.randint(0, 7)))
hash = 0
for x in chain_re.table: # вывод хеш таблицы для метода цепочек
    print("[hash: %i]" % hash, end=" ")
    если x равно None:
        print("Пусто")
    ещё:
        для y в x:
            print(y.value1, end=" ")
        печать("")
    hash += 1


# ### Задание № 3:

# In[ ]:



board = [[0 for i in range (8)]for j in range(8)]
cnt = 0
def setQueen(i, j):
  for x in range(8):
    board[x][j] += 1
    board[i][x] += 1
    if 0 <= i + j - x < 8:
      board[i + j - x][x] += 1
    if 0 <= i - j + x < 8:
      board[i - j +x][x] += 1
  board[i][j] = -1

def removeQueen(i, j):
  for x in range(8):
    board[x][j] -= 1
    board[i][x] -= 1
    if 0 <= i + j - x < 8:
      board[i + j - x][x] -= 1
    if 0 <= i - j + x < 8:
      board[i - j +x][x] -= 1
  board[i][j] = 0

def printPosition():
  global cnt
  cnt += 1
  abc = "abcdefgh"
  ans = []
  for i in range(8):
    for j in range(8):
      if board[i][j] == -1:
        ans.append(abc[j] + str(i+1))
  print(", ".join(ans))

def solve(i):
  for j in range(8):
    if board[i][j] == 0:
      setQueen(i, j)
      if i == 7:
        printPosition()
      else:
        solve(i + 1)
      removeQueen(i, j)

solve(0)
print(cnt)


# Основным процессом решения данной задачи является цикл for. Сначала мы рассматриваем строки и наличие в них ферзей. Если находится более одного - ошибка. 
# Далее цикл for распространяется на вертикальные строки и в самомок конце на диагонали.
