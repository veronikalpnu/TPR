import pandas as pd
from colorama import init, Fore, Back, Style

pd.options.display.max_columns = 9
pd.set_option('display.width', 1400)
init(autoreset=True) 

with open('headphones.txt') as fileobject:
    headphones = []
    headphones = fileobject.readlines()
    headphones = [line.rstrip('\n') for line in headphones]

print(Style.BRIGHT + Fore.BLUE + "Наушники:",*headphones,sep="\n")
print("\n")

with open('parameters.txt') as fileparameters:
    parameters = []
    parameters = fileparameters.readlines()
    parameters = [line.rstrip('\n') for line in parameters]

print(Style.BRIGHT + Fore.BLUE + "Параметри:",*parameters,sep="\n")
print("\n")

with open('importance.txt') as fileimportance:
    importance = []
    importance = fileimportance.readlines()
    importance = [line.rstrip('\n') for line in importance]

file1 = open ('1.txt' , 'r')
exp1 = []
exp1 = [ line.split() for line in file1]

file2 = open ('2.txt' , 'r')
exp2 = []
exp2 = [ line.split() for line in file2]

file3 = open ('3.txt' , 'r')
exp3 = []
exp3 = [ line.split() for line in file3]

file4 = open ('4.txt' , 'r')
exp4 = []
exp4 = [ line.split() for line in file4]

def Price (headphone):
    price = float(importance[0]) * (float(exp1[headphone][0])+float(exp2[headphone][0])+float(exp3[headphone][0])+float(exp4[headphone][0]))
    return price

def Frequency (headphone):
    frequency = float(importance[1]) * (float(exp1[headphone][1])+float(exp2[headphone][1])+float(exp3[headphone][1])+float(exp4[headphone][1]))
    return frequency

def Design (headphone):
    design = float(importance[2]) * (float(exp1[headphone][2])+float(exp2[headphone][2])+float(exp3[headphone][2])+float(exp4[headphone][2]))
    return design

def Weight (headphone):
    weight = float(importance[3]) * (float(exp1[headphone][3])+float(exp2[headphone][3])+float(exp3[headphone][3])+float(exp4[headphone][3]))
    return weight

def Mic (headphone):
    mic = float(importance[4]) * (float(exp1[headphone][4])+float(exp2[headphone][4])+float(exp3[headphone][4])+float(exp4[headphone][4]))
    return mic

def Squelch (headphone):
    squelch = float(importance[5]) * (float(exp1[headphone][5])+float(exp2[headphone][5])+float(exp3[headphone][5])+float(exp4[headphone][5]))
    return squelch

def Func (headphone):
    func = float(importance[6]) * (float(exp1[headphone][6])+float(exp2[headphone][6])+float(exp3[headphone][6])+float(exp4[headphone][6]))
    return func

#SteelSeries Arctis 5 2019 Edition Black (SS61504)
price1 = Price(0)
frequency1 = Frequency(0)
design1 = Design(0)
weight1 = Weight(0)
mic1 = Mic(0)
squelch1 = Squelch(0)
func1 = Func(0)

#HyperX Cloud Alpha (HX-HSCA-RD/EE)
price2 = Price(1)
frequency2 = Frequency(1)
design2 = Design(1)
weight2 = Weight(1)
mic2 = Mic(1)
squelch2 = Squelch(1)
func2 = Func(1)

#PlayStation 5 Pulse 3D Wireless Headset White
price3 = Price(2)
frequency3 = Frequency(2)
design3 = Design(2)
weight3 = Weight(2)
mic3 = Mic(2)
squelch3 = Squelch(2)
func3 = Func(2)

#Logitech Lightspeed Wireless RGB Gaming Headset G733 KDA (981-000990)
price4 = Price(3)
frequency4 = Frequency(3)
design4 = Design(3)
weight4 = Weight(3)
mic4 = Mic(3)
squelch4 = Squelch(3)
func4 = Func(3)

#RAZER Kraken BT Kitty Edition, Quartz Pink (RZ04-03520100-R3M1)
price5 = Price(4)
frequency5 = Frequency(4)
design5 = Design(4)
weight5 = Weight(4)
mic5 = Mic(4)
squelch5 = Squelch(4)
func5 = Func(4)

#Sum

sum1 = price1 + design1 + frequency1 + squelch1 + mic1 + func1 + weight1
sum2 = price2 + design2 + frequency2 + squelch2 + mic2 + func2 + weight2
sum3 = price3 + design3 + frequency3 + squelch3 + mic3 + func3 + weight3
sum4 = price4 + design4 + frequency4 + squelch4 + mic4 + func4 + weight4
sum5= price5 + design5 + frequency5 + squelch5 + mic5 + func5 + weight5

parameters.append('')
importance.append('')

df = pd.DataFrame({'№': ['1', '2', '3', '4', '5', '6', '7', 'Сума'],
                   'Параметри': parameters,
                   'Вага': importance,
                   headphones[0]: [price1, frequency1, design1, weight1, mic1, squelch1, func1, sum1],
                   headphones[1]: [price2, frequency2, design2, weight2, mic2, squelch2, func2, sum2],
                   headphones[2]: [price3, frequency3, design3, weight3, mic3, squelch3, func3, sum3],
                   headphones[3]: [price4, frequency4, design4, weight4, mic4, squelch4, func4, sum4],
                   headphones[4]: [price5, frequency5, design5, weight5, mic5, squelch5, func5, sum5]})

print(Style.BRIGHT + Fore.GREEN + "Результат:")
print(df)
print('\n')

winer = ''
points = ''

if sum1 > sum5 and sum1 > sum3 and sum1 > sum2 and sum1 > sum4:
    winer = headphones[0]
    points = sum1
elif sum2 > sum5 and sum2 > sum3 and sum2 > sum1 and sum2 > sum4:
    winer = headphones[1]
    points = sum2
elif sum3 > sum5 and sum3 > sum2 and sum3 > sum1 and sum3 > sum4:
    winer = headphones[2]
    points = sum3
elif sum4 > sum5 and sum4 > sum2 and sum4 > sum1 and sum4 > sum3:
    winer = headphones[3]
    points = sum4
elif sum5 > sum4 and sum5 > sum2 and sum5 > sum1 and sum5 > sum3:
    winer = headphones[4]
    points = sum5
else:
    print("Щось пішло не так при обличсленнях переможця, або переможець не один!")

print(Fore.YELLOW + "Найкращим варіантом вийшов -",winer, '-', points)
print('\n')