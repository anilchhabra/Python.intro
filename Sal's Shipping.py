def ground_shipping_cost(weight):
  flat_charge = 20.00

  if weight <= 2:
    price_per_pound = 1.50
    
  elif weight > 2 and weight <= 6:
    price_per_pound = 3.00

  elif weight > 6 and weight <= 10:
    price_per_pound = 4.00

  elif weight > 10:
    price_per_pound = 4.75

  cost = price_per_pound*weight + flat_charge
  return cost

print(ground_shipping_cost(8.4))

premium_ground_shipping = 125.00

def drone_shipping_cost(weight):
  if weight <= 2:
    price_per_pound = 4.50
    
  elif weight > 2 and weight <= 6:
    price_per_pound = 9.00

  elif weight > 6 and weight <= 10:
    price_per_pound = 12.00

  elif weight > 10:
    price_per_pound = 14.25

  cost = price_per_pound*weight
  return cost

print(drone_shipping_cost(1.5))

def cheapest_shipping_method(weight):

  ground = ground_shipping_cost(weight)
  premium = premium_ground_shipping
  drone = drone_shipping_cost(weight)

  if ground < premium and ground < drone:
    method = "ground shipping"
    cost = ground

  elif premium < ground and premium < drone:
    method = "premium ground shipping"
    cost = premium

  elif drone < premium and drone < ground:
    method = "drone shipping"
    cost = drone

  

  print("The cheapest option available is $%.2f with %s shipping."
    % (cost,method)
  )

print(cheapest_shipping_method(4.8))
print(cheapest_shipping_method(41.5))


    
