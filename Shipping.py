#Sal's Shipping exercise from "Control Flow" section:
weight = 41.5 #lb
flat_charge = 20.00 #$
total_charge = flat_charge #$
premium_ground_shipping_charge = 125.00 #$
print("Cost of premium ground shipping is:")
print(premium_ground_shipping_charge)

#Ground Shipping:
print("Cost of ground shipping not premium is:")
if weight > 10: 
  total_charge += weight*4.75 #$
  print(round(total_charge, 2))
elif weight > 6:
  total_charge += weight*4.00 #$
  print(round(total_charge, 2))
elif weight > 2:
  total_charge += weight*3.00 #$
  print(round(total_charge, 2))
elif weight >= 0:
  total_charge += weight*1.50 #$
  print(round(total_charge, 2))
else: print("ERROR - Negative weight cannot exist") 

#Drone Shipping:
print("Cost of drone shipping is:")
if weight > 10: 
  total_charge = weight*14.25 #$
  print(round(total_charge, 2))
elif weight > 6:
  total_charge = weight*12.00 #$
  print(round(total_charge, 2))
elif weight > 2:
  total_charge = weight*9.00 #$
  print(round(total_charge, 2))
elif weight >= 0:
  total_charge = weight*4.50 #$
  print(round(total_charge, 2))
else: print("ERROR - Negative weight cannot exist")