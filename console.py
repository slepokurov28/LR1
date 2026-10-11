import sys




args = sys.argv[1:]


coeffs = []
for i in range(3):
   ok = False
   while not ok:
       if i < len(args):
           val_str = args[i]
       else:
           names = ['A', 'B', 'C']
           val_str = input(f"Введите коэффициент {names[i]}: ")
       try:
           val = float(val_str)
           coeffs.append(val)
           ok = True
       except ValueError:
           print(f"Некорректное значение '{val_str}', повторите ввод.")




A, B, C = coeffs




D = B * B - 4 * A * C
print(f"\nДискриминант D = {D}")


roots = []


if A == 0:


   if B == 0:
       if C == 0:
           print("Бесконечно много решений")
       else:
           print("Нет решений")
   else:
       t = -C / B
       if t >= 0:
           roots.append(t ** 0.5)
           roots.append(-(t ** 0.5))
elif D < 0:
   print("Действительных корней нет")
elif D == 0:
   t = -B / (2 * A)
   if t >= 0:
       roots.append(t ** 0.5)
       roots.append(-(t ** 0.5))
   else:
       print("Действительных корней нет")
else:
   t1 = (-B + D ** 0.5) / (2 * A)
   t2 = (-B - D ** 0.5) / (2 * A)
   if t1 >= 0:
       roots.append(t1 ** 0.5)
       roots.append(-(t1 ** 0.5))
   if t2 >= 0:
       roots.append(t2 ** 0.5)
       roots.append(-(t2 ** 0.5))
   if not roots:
       print("Действительных корней нет")


if roots:
   roots = sorted(set(round(r, 10) for r in roots))
   print("Действительные корни:")
   for r in roots:
       print(f"  x = {r}")
