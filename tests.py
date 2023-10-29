# PyTest #

# Задача 1
'''
import pytest

def what_number(n):
    if n > 0:
        return 'positive'
    if n < 0:
        return 'negative'

@pytest.mark.parametrize('x, expected',
                         [(5, 'positive'),
                          (-5, 'negative')])

def test_positive_or_nagative(x, expected):
    assert what_number(x) == expected
'''

# Задача 2
'''
import pytest

def even_number(n):
    if n % 2 == 0:
        return 'positive'
    elif n % 2 != 0:
        return 'negative'

@pytest.mark.parametrize('x, expected',
                         [(2, 'positive'),
                          (3, 'negative')])

def test_even_number(x, expected):
    assert even_number(x) == expected
'''

# Задача 3
'''
import pytest

def lenght_number(n):
    return len(str(n))

@pytest.mark.parametrize('x, expected',
                         [(123456, 6),
                          (123, 3),
                          (123456789, 9)])

def test_lenght_number(x, expected):
    assert lenght_number(x) == expected
'''

# Задача 4
'''
import pytest

def list_sum(list):
    sum = 0
    for i in range(0, len(list)):
        sum += list[i]
    return sum

@pytest.mark.parametrize('x, expected',
                         [([1, 2, 3], 6),
                          ([1, 2, 3, 4, 5], 15),
                          ([5, 6, 7], 18)])

def test_list_sum(x, expected):
    assert list_sum(x) == expected
'''

# Задача 5
'''
import pytest

def str_transformation_list(str):
    sum = 0

    str = str.replace(',', ' ')
    str = str.split()

    for i in range(0, len(str)):
        str[i] = int(str[i])
        sum += str[i]
    return sum

@pytest.mark.parametrize('x, expected',
                         [('12,36,54', 102),
                          ('320,123,540', 983),
                          ('4,1,3', 8),
                          ('1,23,456', 480)])

def test_str_transformation_list(x, expected):
    assert str_transformation_list(x) == expected
'''


# Unittest # Unittest # Unittest # Unittest # Unittest # Unittest # Unittest # Unittest # Unittest # Unittest


# Задание 1
'''
import unittest

def date_str_trans_motorcade(str):
    str = str.replace('-', ' ')
    str = tuple(str.split(' '))
    str = str[::-1]
    return str

class TestUM(unittest.TestCase):
    def testEqual(self):
        self.failUnlessEqual(date_str_trans_motorcade('2025-12-31'), ('31', '12', '2025'))
'''

# Задание 2
'''
import unittest

def sum_list(list):
    sum = 0

    for i in range(0, len(list)):
        list[i] = int(list[i])
        sum += list[i]

    return sum

class testUM(unittest.TestCase):
    def testEqual(self):
        self.failUnlessEqual(sum_list(['1','2','3','4','5']), 15)
'''

# Задание 3
'''
import unittest
def one_division_two(list):
    sum1 = 0
    sum2 = 0

    for i in range(0, len(list) // 2):
        sum1 += list[i]

    for i in range(len(list) // 2, len(list)):
        sum2 += list[i]

    return sum1 / sum2

list = [1, 2, 3, 4, 5, 6]
division_result = 0.4

class testUM(unittest.TestCase):
    def testEqual(self):
        self.failUnlessEqual(one_division_two(list), division_result)
'''

# Задание 4
'''
import unittest
def merge_dictionaries(dictionary1, dictionary2):
    return dictionary1 | dictionary2

dct1 = {
	'a': 1,
	'b': 2,
}

dct2 = {
	'c': 3,
	'd': 4,
}

dct3 = dct1 | dct2

class testUM(unittest.TestCase):
    def testEqual(self):
        self.failUnlessEqual(merge_dictionaries(dct1, dct2), dct3)
'''

# Задание 5
'''
import unittest
def sum_val_dictionary(dictionary):
    sum = 0

    #for i in range(0, len(dictionary)):
        #for j in range(0, len(dictionary[i])):
            #sum += dictionary[i][j]

    for i in dictionary:
        for j in dictionary:
            sum += dictionary[i][j]
    return sum

dct = {
	1: {
		1: 11,
		2: 12,
		3: 13,
	},
	2: {
		1: 21,
		2: 22,
		3: 23,
	},
	3: {
		1: 24,
		2: 25,
		3: 26,
	},
}

result_sum = 177

class testUM(unittest.TestCase):
    def testEqual(self):
        self.failUnlessEqual(sum_val_dictionary(dct), result_sum)
'''

# Задание 5
'''
import unittest
def min_max_list(list):
    min = 1
    max = 0

    for i in range(0, len(list)):
        if min > list[i]:
            min = list[i]

        if max < list[i]:
            max = list[i]

    return {
        'min': min,
        'max': max,
    }


list = [1, 2, 3, 4, 5]

print(min_max_list(list))

class testUM(unittest.TestCase):
    def testEqual(self):
        self.failUnlessEqual(min_max_list(list), {'min': 1, 'max': 5})
'''

# Задание 6
'''
import unittest
def count_division(list):
    d = dict()

    for i in range(0, len(list)):
        for j in range(1,list[i]+1):
            if list[i] % j == 0:
                d[j] = list[i] // j
        list[i] = d
        d = dict()
    return list
list = [1, 2, 3]
result_list = [{1: 1}, {1: 2, 2: 1}, {1: 3, 3: 1}]

class testUM(unittest.TestCase):
    def testEqual(self):
        self.failUnlessEqual(count_division(list), result_list)
'''

# Задание 7
'''
import unittest, random

def fill_list_random(list, min, max, count_elements):
    n = 0

    for i in range(0, count_elements):
        list.append(random.randint(min, max))
        list.sort()

    # Не получилось заменять повторяющееся значение на не повторяющееся
    # for i in range(0, len(list)-1):
    #     if list[i] == list[i+1]:
    #         while n == 0:
    #             n = random.randint(min, max)
    #             for j in range(0, len(list)):
    #                 if list[j] == n:
    #                     n = 0
    #             list[i] = n
    #     list.sort()

    return list

list = []

#print(fill_list_random(list, 1, 10, 5))

class testUM(unittest.TestCase):
    def testEqual(self):
        self.failIfEqual(fill_list_random(list, 1, 10, 5), [0, 0, 0, 0, 0])
'''

# Задание 8
'''
import unittest, random

def random_elements(list):
    return list[random.randint(0,len(list))]

list = ['red','orange','yellow','green','blue']

print(random_elements(list))

class testUM(unittest.TestCase):
    def testEqual(self):
        self.failIfEqual(random_elements(list), 'purple')
'''

# Задание 9
'''
import unittest

def counts_syllables(let):
    let = let.lower()
    vowels = ['а', 'о', 'у', 'э', 'ы', 'я', 'ё', 'е', 'ю', 'и'] # можно внести слоги, но их очень много
    count = 0

    for i in range(0, len(let)):
        for j in range(0, len(vowels)):
            if let[i] == vowels[j]:
                count += 1
    return count


letter = 'Привет'

#print(counts_syllables(letter))

class testUM(unittest.TestCase):
    def testEqual(self):
        self.failUnlessEqual(counts_syllables(letter), 2)
'''

# Задание 10
'''
import unittest, random

def shuffle_list(list):
    random.shuffle(list)
    return list


list = [1, 2, 3, 4, 5]

#print(shuffle_list(list))

class testUM(unittest.TestCase):
    def testEqual(self):
        self.failIfEqual(shuffle_list(list), [1, 2, 3, 4, 5])
'''