"توابع بازگشتي"

"فاکتوریل به روش قدیمی"
ni= (3) #اگر بخوایم فاکتوریل عدد 3 رو محاسبه کنیم
fact = 1
for i in range(1, ni+1):
    fact = fact * i
print(ni, fact)

"فاکتوريل بازگشتي"
def facto(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * facto(n - 1)

"چاپ اعداد بازگشتی"
def count(z):
    if z == 0:
        return
    count(z-1)
    print(z)

"چاپ برعکس اعداد بازگشتي"
def count2(j):
    if j == 0:
        return
    count2(j+1)
    print(j)

"به روش قدیمی a,n مجموع اعداد"
def sam(a):
    s=0
    for i in range(a+1):
        s += i
    return s

"بازگشتي a,n مجموع اعداد"
def sumnew(n):
    if n==0:
        return 0
    return n+sumnew(n-1)

"به توان رساندن اعداد"
def POWER(a,b):
    if b==1:
        return a
    elif b==0:
        return 1
    x= POWER(a,b//2)
    if b%2==0:
        return x*x
    else:
        return a*x*x

"(بی نهایت)تابع فیبوناچی به روش قدیمی"
i=1
a=1
b=1
print(a)
print(b)
while i<10:
    c=a+b
    print(c)
    a=b
    b=c
    #i=i+1
    i=i-1

"تابع فیبوناچی بازگشتی"
def Fibo(n):
    if n==0 or n==1: 
        return 1
    else: 
        return Fibo(n-1)+Fibo(n-2) 
    
"بازی برج های هانوی به روش بازگشتی"
def hanoi(x="تعداد مهره",a="ستون",c="ستون",b="ستون"):
    if x==1:
        print(a,'->',c)
        return
    hanoi(x-1,a,b,c)
    print(a,'->',c)
    hanoi(x-1,b,c,a)
    return
#----------------------------------------------------------
#hanoi(3,'a','c','b')

"پیدا کردن اعضا در یک لیست *مرتب* به روش بازگشتی"
def search(h="عددي که بايد دنبالش بگردم:" ,primenum="اتام ليستت چيست؟(اعداد اول)" ,a="از بازه:" ,b="تا بازه:" ):
    if a>b:
        return "پیدا نشد"
    k=(a+b)//2
    if h==primenum[k]:
        return 
    if h<primenum[k]:
        return search(h,primenum,a,k-1)
    if h>primenum[k]:
        return search(h,primenum,k+1,b)
primenum=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

"وصل کردن دوتا لیست و مرتب کردنشان"
def Merg(L1,L2,L):
    i=0
    j=0
    while i < len (L1) and  j < len (L2):
        if L1[i] < L2[j]:
            L.append(L1[i])
            i=i+1
        else:
           L.append(L2[j])
           j=j+1
    while i < len(L1):
        L.append(L1[i])
        i=i+1
    while j < len(L2):
        L.append(L2[j])  
        j=j+1
#----------------------------------------------------------
L1=[9,6,5,2,81,11]
L2=[3,7,8,20,10]

"متصل و مرتب کردن لیست به روش بازگشتی"
def Merg(L1,L2):
    L=[]
    i=0
    j=0
    while i < len (L1) and  j < len (L2):
        if L1[i] < L2[j]:
            L.append(L1[i])
            i=i+1
        else:
           L.append(L2[j])
           j=j+1
    while i < len(L1):
        L.append(L1[i])
        i=i+1
    while j < len(L2):
        L.append(L2[j])  
        j=j+1
    return  L
#----------------------------------------------------------
def sort(L):
    if len(L)==1:
        return L
    m=len(L)//2
    L1=L[:m]
    L2=L[m:]
    L1=sort(L1)
    L2=sort(L2)
    L=Merg(L1,L2)
    return L
#----------------------------------------------------------
L=[9,6,5,2,81,11,3,7,8,20,10]
L=sort(L)
#print(L)

"مرتب سازی لیست نامرتب به روش بازگشتی"
def selsort(l):
    end=len(l)
    for i in range(end):
        m=l[i]
        k=i
        for j in range(i,end):
            if l[j]<m:
                m=l[j]
                k=j
        l[i],l[k]=l[k],l[i]
        print(l)
#----------------------------------------------------------
l=[30,25,15,10,50,45,5,35]
selsort(l)
print('--------------------------')
print(l)

"خرد کرد پول به روش قدیمی"
print("به چند روش میتوان مبلغ دریافتی شمارا با کمک اسکناس های 50هزار تومانی، 10هزار تومانی و 5هزار تومانی خرد کرد?")
x=int(input("mablagh:"))
a=x//50+1
b=x//10+1
c=x//5+1
counter=0
for i in range(a):
    for j in range(b):
        for k in range(c):
            if (i*50+j*10+k*5) == x:
                                print(i,j,k)
                                counter=counter+1
#----------------------------------------------------------
print("به" ,counter ,"مدل میتوان مبلغ را خرد کرد")

"خرد کردن پول یا سکه به روش بازگشتی"
def seke(n="عدد درخواستي",a="50",b="25",c="10"):
    if n==0:
        s.add(f'{a},{b},{c}')
        return
    if n<0:
        return
    seke(n-50,a+1,b,c)
    seke(n-25,a,b+1,c)
    seke(n-10,a,b,c+1)
#----------------------------------------------------------
s=set()
#seke(100,0,0,0)
#print(s)
#print("_________________")
#print(len(s))
