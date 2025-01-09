height=5.9
weight=75

#BMI weight in kg/(height*height in meters)
'''heightinMeter=height*0.4536
bmi=weight/(heightinMeter*heightinMeter)
print('BMI : ',bmi)'''

def calcBMI(height,weight):
    heightinMeter=height*0.4536
    bmi=weight/(heightinMeter * heightinMeter)
    return bmi

print(calcBMI(6.0,67))
