

def stringSearch(s, x):
    i=j=0
    lengthS = len(s)# Длина строки в которой ищем
    lengthX = len(x)# -||- которую ищем
    # пока не достигли одного из концов
    while i<=lengthS - lengthX and j<lengthX:
     # если совпали буквы продвигаемся по обеим строкам
        if s[i+j]==x[j]:
            j+=1
        # иначе двигаемся по строке(+1), начиная с 0 символа подстроки
        else:
            i+=1
            j=0
    # если дошли до конца подстроки - нашли, иначе - нет
    return i if j==lengthX else None

stroka="fwdfbubajfe"
pod="buba"

print(f"Подстрока начинается с {stringSearch(stroka,pod)} индекса")