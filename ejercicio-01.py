#ejercicio 1
numero_1 = input("Introduce el primer numero")

print(numero_1)

#ej2
def max_of_three(a, b, c):
    return a if a >= b and a >= c else b if b >= c else c

#ej3
def my_len(seq):
    count = 0
    for _ in seq:
        count += 1
    return count

#ej4
def is_vowel(c):
    return c.lower() in "aeiou"

#ej5
def translate(text):
    result = ""
    for c in text:
        if c.isalpha() and not is_vowel(c):
            result += c + "o" + c
        else:
            result += c
    return result

#ej6
def sum_list(nums):
    total = 0
    for n in nums:
        total += n
    return total

def multiply(nums):
    result = 1
    for n in nums:
        result *= n
    return result

#ej7
def reverse(s):
    rev = ""
    for c in s:
        rev = c + rev
    return rev

#ej8
def is_palindrome(s):
    return s == reverse(s)

#ej9
def is_member(x, a):
    for item in a:
        if item == x:
            return True
    return False

#ej10
def overlapping(a, b):
    for x in a:
        for y in b:
            if x == y:
                return True
    return False

#ej11
def generate_n_chars(n, c):
    result = ""
    for _ in range(n):
        result += c
    return result

#ej12
def histogram(lst):
    for n in lst:
        print("*" * n)

#ej13
def max_in_list(lst):
    max_val = lst[0]
    for n in lst:
        if n > max_val:
            max_val = n
    return max_val

#ej14
def word_lengths(words):
    return [len(w) for w in words]

#ej15
def find_longest_word(words):
    return max(len(w) for w in words)

#ej16
def filter_long_words(words, n):
    return [w for w in words if len(w) > n]

#ej17
import string

def is_phrase_palindrome(s):
    cleaned = ""
    for c in s.lower():
        if c.isalpha():
            cleaned += c
    return cleaned == cleaned[::-1]

#ej18
def is_pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet <= set(sentence.lower())

#ej19
def bottles_of_beer():
    for n in range(99, 0, -1):
        print(f"{n} bottles of beer on the wall, {n} bottles of beer.")
        print(f"Take one down, pass it around, {n-1} bottles of beer on the wall.\n")

#ej20
lexicon = {
    "merry":"god", "christmas":"jul", "and":"och",
    "happy":"gott", "new":"nytt", "year":"år"
}

def translate(words):
    return [lexicon[w] for w in words]

#ej21
def char_freq(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return freq

#ej22
def rot13(text, key):
    result = ""
    for c in text:
        result += key.get(c, c)
    return result

#ej23
import re

def correct(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\.(\w)", r". \1", text)
    return text

#ej24
def make_3sg_form(verb):
    if verb.endswith("y"):
        return verb[:-1] + "ies"
    if verb.endswith(("o","ch","s","sh","x","z")):
        return verb + "es"
    return verb + "s"

#ej25
def make_ing_form(verb):
    if verb.endswith("ie"):
        return verb[:-2] + "ying"
    if verb.endswith("e") and verb not in ["be","see","flee","knee"]:
        return verb[:-1] + "ing"
    if (len(verb) >= 3 and
        verb[-1] not in "aeiou" and
        verb[-2] in "aeiou" and
        verb[-3] not in "aeiou"):
        return verb + verb[-1] + "ing"
    return verb + "ing"

#ej26
from functools import reduce

def max_in_list(lst):
    return reduce(lambda a, b: a if a > b else b, lst)

#ej27

lengths1 = []
for w in words:
    lengths1.append(len(w))

lengths2 = list(map(len, words))

lengths3 = [len(w) for w in words]

#ej28
from functools import reduce

def find_longest_word(words):
    return reduce(lambda a, b: a if len(a) > len(b) else b, words)

#ej29
def filter_long_words(words, n):
    return list(filter(lambda w: len(w) > n, words))

#ej30
def translate(words):
    return list(map(lambda w: lexicon[w], words))

#ej31
def my_map(func, seq):
    return [func(x) for x in seq]

def my_filter(func, seq):
    return [x for x in seq if func(x)]

def my_reduce(func, seq):
    result = seq[0]
    for x in seq[1:]:
        result = func(result, x)
    return result

#ej32
def file_palindromes(filename):
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if is_phrase_palindrome(line):
                print(line)

#ej33
def semordnilaps(filename):
    with open(filename) as f:
        words = [line.strip() for line in f]
    for w in words:
        if reverse(w) in words and w < reverse(w):
            print(w, reverse(w))

#ej34
filename = input("File name: ")

f = open(filename, "r")
text = f.read()
f.close()

freq = {}

for c in text:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

keys = []
for k in freq:
    keys.append(k)

keys.sort()

print("CHAR | FREQ")
print("-----------")
for k in keys:
    print(repr(k), " | ", freq[k])

#ej35
import os
import time

d = {
 'a':'alfa','b':'bravo','c':'charlie','d':'delta','e':'echo',
 'f':'foxtrot','g':'golf','h':'hotel','i':'india','j':'juliett',
 'k':'kilo','l':'lima','m':'mike','n':'november','o':'oscar',
 'p':'papa','q':'quebec','r':'romeo','s':'sierra','t':'tango',
 'u':'uniform','v':'victor','w':'whiskey','x':'x-ray',
 'y':'yankee','z':'zulu'
}

text = input("Text: ")
pause_letter = 0.5
pause_word = 1.0

for c in text:
    if c == " ":
        time.sleep(pause_word)
    else:
        cl = c.lower()
        if cl in d:
            os.system("say " + d[cl])
            time.sleep(pause_letter)

#ej36
filename = input("File name: ")

f = open(filename)
text = f.read().lower()
f.close()

words = text.split()
freq = {}

for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

for w in freq:
    if freq[w] == 1:
        print(w)

#ej37
src = input("Source file: ")
dst = input("Output file: ")

f1 = open(src)
f2 = open(dst, "w")

n = 1
for line in f1:
    f2.write(str(n) + ": " + line)
    n += 1

f1.close()
f2.close()

#ej38
filename = input("File name: ")

f = open(filename)
text = f.read()
f.close()

words = text.split()

total_chars = 0
total_words = 0

for w in words:
    count = 0
    for _ in w:
        count += 1
    total_chars += count
    total_words += 1

print(total_chars / total_words)

#ej39
import random

name = input("Hello! What is your name?\n")
number = random.randint(1, 20)

print("Well,", name + ", I am thinking of a number between 1 and 20.")

guesses = 0
while True:
    guess = int(input("Take a guess.\n"))
    guesses += 1

    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    else:
        print("Good job,", name + "!", "You guessed my number in", guesses, "guesses!")
        break

#ej40
import random

colors = ["black", "white", "brown", "green", "yellow", "orange"]
word = random.choice(colors)

letters = []
for c in word:
    letters.append(c)

random.shuffle(letters)

anagram = ""
for c in letters:
    anagram += c

print("Colour word anagram:", anagram)

while True:
    guess = input("Guess the colour word!\n")
    if guess == word:
        print("Correct!")
        break

#ej41
secret = "tiger"

while True:
    guess = input()

    result = ""
    used = []

    for i in range(5):
        if guess[i] == secret[i]:
            result += "[" + guess[i] + "]"
            used.append(i)
        elif guess[i] in secret:
            result += "(" + guess[i] + ")"
        else:
            result += guess[i]

    print("Clue:", result)

    if guess == secret:
        break

#ej42
filename = input("File: ")

f = open(filename)
text = f.read()
f.close()

sentence = ""

for c in text:
    sentence += c
    if c in ".?!":
        print(sentence.strip())
        sentence = ""

#ej43

#ej44

#ej45

#ej46
