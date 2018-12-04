def increasing(s):
        t = True
        for i in range(1, len(s)):
                if s[i] <= s[i-1]:
                        t = False
                        break
        return t

def descension(s):
        res = ''
        for x in s:
                if x == '0':
                        res += x
                else:
                        res += str(int(x)-1)
        return res

def evenodd(s):
        even = 0
        for i in range(len(s)):
                if int(s[i]) % 2 == 0:
                        even += 1
        return even

a = input('Введите число: ')
if increasing(a):
        print('В порядке возрастания')
else:
        print('В порядке убывания')
b = descension(a)
c = evenodd(a)
print('Четных чисел -', c)
print(b)

