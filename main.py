time=input("Enter the time: ")
time=int(time)
print("1.Taxi")
print("2.Minibus")
print("3.Commercial")
typeVehicle=input("Enter the type of vehicle: ")

cost=0

if typeVehicle=="1":
    if time==1:
        cost=5;
    else:
        hourlyCost=10;
        for i in range(1,time):
            hourlyCost=hourlyCost*(1+0.20);
        cost=hourlyCost * time;
elif typeVehicle=="2":
    if time==1:
        cost=6;
    else:
        hourlyCost=15;
        for i in range(1,time):
            hourlyCost=hourlyCost*(1+0.25);
        cost=hourlyCost * time;
else:
    if time==1:
        cost=6.5;
    else:
        hourlyCost=20;
        for i in range(1,time):
            hourlyCost=hourlyCost*(1+0.30);
        cost=hourlyCost * time;
print(cost)