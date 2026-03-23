
print("choose btween 1-4 ")
print("Choose what do you want to do ? \n 1. Calculate cube volume \n 2. Calculate cylinder volume.\n 3. Calculate cone volume \n 4.Exit " )
choice =input(" Enter your choice : ")
if choice == '1':
        length = float(input("Enter the length length of the cube: "))
        if length >= 0:
            volume = length ** 3
            print(f"Cube volume: {volume:.2f}")
        else:
             print("Side length cannot be negative, \n try again in another time... ")
    
elif choice == '2':     #2. Calculate cylinder volume.  
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        if radius >= 0 and height >= 0:
            volume =  radius ** 2 * height
            print(f"Cylinder volume: {volume:.2f}")
        else:
            print("Radius and height cannot be negative , \n please try again ")

elif choice == '3':  #3. Calculate cone volume  
        radius = float(input("Enter the radius of the cone: "))
        height = float(input("Enter the height of the cone: "))
        if radius >= 0 and height >= 0:
            volume = (1/3) *  radius ** 2 * height
            print(f"Cone volume: {volume:.2f}")
        else:
            print("Radius and height cannot be negative! , try again... ")
elif choice == '4': #4. Exit
     print("Goodby......") 
     exit
else:
     print("Invalid choice\n please try again another time , and input anumber brtween (1-4).... ")
                     
