# Sal's Shipping
# Sonny Li

weight = 80

# Ground Shipping 🚚

if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Ground Shipping $", cost_ground)
      
# Ground Shipping Premimum 🚚💨

cost_ground_premium = 125.00

print("Ground Shipping Premimium $", cost_ground_premium)

# Drone Shipping 🛸

if weight <= 2:
  cost_drone = weight * 4.5
elif weight <= 6:
  cost_drone = weight * 9.00
elif weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

print("Drone Shipping: $", cost_drone)




#or establish the prices before the eilf statements and use the "+=" function to change the values of the prices like so:

#constants
weight = 4.8
price = 0
reg_price = 20
prem_price = 125

#Ground Shipping
if weight <= 2:
  reg_price += weight*1.50
elif weight > 2 and weight <= 6:
  reg_price += weight*3
elif weight > 6 and weight <= 10:
  reg_price += weight*4
else:
  reg_price += weight*4.75

print("Ground Shipping Price: $", reg_price)
print("Ground Shipping Premium Price: $",prem_price)

#Drone Shipping
if weight <= 2:
  price += weight*4.50
elif weight > 2 and weight <= 6:
  price += weight*9
elif weight > 6 and weight <= 10:
  price += weight*12
else:
  price += weight*14.25

print("Drone Shipping Price: $",price)
