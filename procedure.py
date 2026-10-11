import sys
import math




def get_coef(index, prompt):


   while True:
       try:
           coef_str = sys.argv[index]
       except IndexError:
           coef_str = None


       if coef_str is None:
           print(prompt)
           coef_str = input()


       try:
           coef = float(coef_str)
           return coef
       except ValueError:
           print('Некорректное значение коэффициента. Повторите ввод.')
           if index < len(sys.argv):
               sys.argv[index] = None




def get_roots(a, b, c):


   result = []




   if a == 0.0:
       if b == 0.0:
           return result
       t = -c / b
       if t > 0.0:
           sqt = math.sqrt(t)
           result.append(sqt)
           result.append(-sqt)
       elif t == 0.0:
           result.append(0.0)
       return result




   D = b * b - 4 * a * c


   if D < 0.0:
       return result


   if D == 0.0:
       t = -b / (2.0 * a)
       if t > 0.0:
           sqt = math.sqrt(t)
           result.append(sqt)
           result.append(-sqt)
       elif t == 0.0:
           result.append(0.0)
       return result


   # D > 0.0
   sqD = math.sqrt(D)
   t1 = (-b + sqD) / (2.0 * a)
   t2 = (-b - sqD) / (2.0 * a)


   if t1 > 0.0:
       sqt1 = math.sqrt(t1)
       result.append(sqt1)
       result.append(-sqt1)
   elif t1 == 0.0:
       result.append(0.0)


   if t2 > 0.0:
       sqt2 = math.sqrt(t2)
       result.append(sqt2)
       result.append(-sqt2)
   elif t2 == 0.0:
       result.append(0.0)


   return result




def main():


   a = get_coef(1, 'Введите коэффициент А:')
   b = get_coef(2, 'Введите коэффициент B:')
   c = get_coef(3, 'Введите коэффициент C:')


   roots = get_roots(a, b, c)
   unique_roots = sorted(set(roots))


   len_roots = len(unique_roots)
   if len_roots == 0:
       print('Нет действительных корней')
   elif len_roots == 1:
       print('Один корень:', unique_roots[0])
   elif len_roots == 2:
       print('Два корня:', unique_roots[0], 'и', unique_roots[1])
   elif len_roots == 3:
       print('Три корня:', unique_roots[0], ',', unique_roots[1], 'и', unique_roots[2])
   else:
       print('Четыре корня:', unique_roots[0], ',', unique_roots[1],
             ',', unique_roots[2], 'и', unique_roots[3])




if __name__ == "__main__":
   main()
