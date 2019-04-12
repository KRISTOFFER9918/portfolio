n=int(input("skriv ett tal"))
if n % 3 == 0:
 print(n, "kan delas med 3.")
else:
  print(n, "kan inte delas med 3. ")


  for n in range(1, 21):
 if n % 2==0 or n % 3==0:
     print(n)


n=int(input("skriv ett heltal:"))
if n % 2==0 and n>=10:
 print("ditt tal är större än 10 och är jämnt")
else:
  print("ditt tal är inte större än 10")


  x=int(input("vad är temperatruren"))
if x<5:
    print("då ska du stanna hemma")
elif 5<x<15:
    print("då ska du gå till bibloteket")
else:
    print("då ska du ut cykla")


    a = int(input("hur mycket pengar vill du sätta in: ?"))
if a>0:
  print("du har lagt in", a, "kr")
elif a<0:
    print("du kan inte sätta in summa under noll")
b = int(input("hur mycket vill du ta ut: ?"))
b = a - b
print("du har tagit ut",a-b, "kr och har kvar",b, "kr på ditt bankkonto")



c = int(input())
fahrenheit = ((c*9)/5) +32
print(fahrenheit)


n = input("n?")
y = 0
x = n
for n in range(1, x):
   y = y + 1/n


print("vilken viktklass motsvarar dig.")
vikt = int(input("uppge din vikt i kg:  "))
längd = int(input("uppge din längd i cm:  "))
längd = längd / 100
BMI = (vikt / (längd ** 2))
if BMI < 20:
   print("Viktklass= Undervikt")
elif BMI >= 20 and BMI < 25:
   print("Viktklass= Normalvikt")
elif BMI >= 25 and BMI < 30:
   print("Viktklass= Övervikt")
elif BMI >= 30:
   print("Viktklass= Fetma") 
  

  lista= [1,105,105,2,4]
lista.append(4)
print(lista)


lista= [1,105,105,2,4]
print(sum(lista)/len(lista))
print(lista)                             medelvärdet



lista= [1,105,105,2,4]
lista.sort()                            storleksordning
print(lista)



lista=[1,105,105,2,4]
for x in range (1,106):
  a=lista.count(x)                                   105 förekommer 2 gånger
  print("i listan",x,"förekommer",a,"gånger")



print(lista[2])                    skriv andra för att få första




lektion 10

import random
namn=["a,b,c,d,e"]
print (random.choice(namn))


import random
namn=["a","b","c","d","e"]
print (random.choice(namn))



smaklista1=["vanilj","mango","choklad"]
smaklista2=["vanilj","mango","choklad"]

for smak1 in smaklista1:
  for smak2 in smaklista2:

    print(smak1,smak2)
smaklista2.pop(0)


smaklista1=["byxa1","byxa2","byxa3","byxa4"]
smaklista2=["tröja1","tröja2","tröja3"]                     4 olika byxor och 3 olika tröjor

for smak1 in smaklista1:
  for smak2 in smaklista2:

    print(smak1,smak2)
  smaklista2.pop(0)


smaklista1=["byxa1","byxa2","byxa3","byxa4"]                4 oloika byxor och 4 olika tröjor
smaklista2=["tröja1","tröja2","tröja3","tröja4"]

for smak1 in smaklista1:
  for smak2 in smaklista2:

    print(smak1,smak2)
  smaklista2.pop(0)




tal_1=int(input("skriv in ett tal1"))
tal_2=int(input("skriv ett tal som tal_1 ska höjas till"))
print(tal_1**tal_2)


for n in range (1,101):
 if n % 2 == 1 :
  print(n)


  
import turtle
t = turtle.Turtle()

t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)



Sheashark

Console.WriteLine("Hello World!");
            int nr = 100;
            Console.WriteLine(nr);
            nr = 555;
            Console.WriteLine(nr);
            Console.ReadKey();


            



 Console.Write("ange ålder");
            int ålder = Convert.ToInt32(Console.ReadLine());
            if (ålder >= 0 && ålder <= 12)
                
            {
                Console.WriteLine("Du ska ha vit mössa");
            }

            else if (ålder >= 19 && ålder <= 25)
            {
                Console.WriteLine("Du ska ha röd mössa");
            }

            else if (ålder >= 26 && ålder <= 99)
            {
                Console.WriteLine("Du ska ha blå mössa");
            }

            else
            {
                Console.WriteLine("ogiltig ålder");
            }


            Console.ReadLine();
        }





                                                           fahrenheit till celsius

        namespace metod
{
    class Program
    {
        static int CelsiusToFarenheit(int celsius)
        {
            int farenheit = ((celsius * 9 / 5) + 32);
            return farenheit;
        }

        static void Main(string[] args)
        {
            Console.Write("skriv in grader i celsius: ");

            int celsius = Convert.ToInt32(Console.ReadLine());
            int farenheit = CelsiusToFarenheit(celsius);
            Console.WriteLine(celsius + " grader Celsius blir " + farenheit + "grader farenheit.");
            Console.ReadKey();
        }

     
    }
}



































