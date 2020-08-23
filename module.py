import json
import numpy as np

def Init_Json(l,fileName):
     with open(fileName,'w') as f:
        json.dump(l,f)


def Get_Json(fileName):
    with open(fileName,'r') as f:
        l=json.load(f)
        return l


def MakeBestProfit():
    pass


def CheckIngredient(IngredientName,number):
    with open("FoodStorage.json",'r') as f:
        l=json.load(f)
        if IngredientName in l and number <= (l[IngredientName]):
            return 1
        else:
            return 0


def TakeIngredientOut(IngredientName,number):
    with open("FoodStorage.json",'r+') as f:
        l=json.load(f)
        if IngredientName in l and number<=l[IngredientName]:
            l.update({IngredientName:(-number+l[IngredientName])})
            Init_Json(l,"FoodStorage.json")
        else:
            print("Cannot afford that !!!, shortage of {} {}".format(number-l[IngredientName],IngredientName))


def AddIngredient(IngredientName,number):
    with open("FoodStorage.json",'r+') as f:
        l=json.load(f)
        if number != 0 and IngredientName in l:
            l.update({IngredientName:(number+l[IngredientName])})
            Init_Json(l,"FoodStorage.json")
        else:
            print("ERROR!!!")
    


def GetMeal(Meal):
    with open("Meals.json",'r') as f:
        l=json.load(f)
        Ingredients=["gio","trung","cha","pate","bo","ga","com","pho","banh my","rau"]
        for x in Ingredients:
            if x in Meal and CheckIngredient(x,1):
                TakeIngredientOut(x,1)


def GetProfit(Meal):
    Money=np.array([100,50,100,100,50,20,50,50,80,10])
    with open("Meals.json",'r') as f:
        l=json.load(f)
        if Meal in l:
            Profit=np.dot(Money,np.array(l[Meal]))
            return Profit


def MakeRecipe(Meal):
    Recipe=[]
    Ingredients=["gio","trung","cha","pate","bo","ga","com","pho","banh my","rau"]
    l=""
    for x in Ingredients:    
        if x in Meal:
            Recipe.append(1)
            l=l+x
        else:
            Recipe.append(0)
    if l.split().sort()==Meal.split().sort():
        return  {Meal:Recipe} 


def InitMeals():
    Meals={}
    A=int(input("Enter the number of meals: "))
    for i in range(A):
        Meal=input("Enter the meal {} : ".format(i+1))
        Meals.update(MakeRecipe(Meal))
    return Meals


def Order():
    l=[]
    while(1):
        print("1.Com ga---------------------70")
        print("2.Com trung------------------100")
        print("3.Com rau--------------------60")
        print("4.Banh my trung--------------130") 
        print("5.Banh my pate---------------180")
        print("6.Banh my bo-----------------130")
        print("7.Com bo---------------------100")
        print("8.Com cha--------------------150")
        print('9.Com gio--------------------150')
        print("10.Banh my gio---------------180")
        print("0. Exit")
        opt=int(input("Enter the details: "))
        if opt==1:
            l.append("com ga")
            GetMeal("com ga")
        elif opt==2:
            l.append("com trung")
            GetMeal("com trung")
        elif opt==3:
            l.append("com rau")
            GetMeal("com rau")
        elif opt==4:
            l.append("banh my trung")
            GetMeal("banh my trung")
        elif opt==5:
            l.append("banh my pate")
            GetMeal("banh my pate")
        elif opt==6:
            l.append("banh my bo")
            GetMeal("banh my bo")
        elif opt==7:
            l.append("com bo")
            GetMeal("com bo")
        elif opt==8:
            l.append("com cha")
            GetMeal("com cha")
        elif opt==9:
            l.append("com gio")
            GetMeal("com gio")
        elif opt==10:
            l.append("banh my gio")
            GetMeal("banh my gio")
        elif opt==0:
            break;
    return l



def GetTotalProfit(order):
    total=0
    for x in order:
        total=total+GetProfit(x)
    return total



Ingredients={"banh my":20,"com":20,"trung":20,"gio":20,"cha":20,"pate":20,"bo":20,"ga":20,"rau":20,"pho":20}

print(GetTotalProfit(Order()))

