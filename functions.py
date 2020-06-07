train_mass = 22680
train_acceleration = 10
train_distance = 100
c = 3*10**8

bomb_mass = 1

def f_to_c(f_temp):
  f_temp = 0
  c_temp = 0
  
  c_temp = (f_temp - 32)*(5/9)
  
  return c_temp

def c_to_f(c_temp):
  c_temp = 0
  f_temp = 0
  
  f_temp = c_temp*(9/5) + 32
  
  return f_temp

def get_force(mass,acceleration):
  
  return mass*acceleration

def get_energy(mass,c):
  return mass*c^2

def get_work(mass,acceleration,distance):
  force = get_force(mass,acceleration)
  
  work = force*distance
  

f100_in_celsius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)
train_force = get_force(train_mass,train_acceleration)
bomb_energy = get_energy(bomb_mass,c)
train_work = get_work(train_mass,train_acceleration,train_distance)

print(train_force)

print("The GE train supplies", str(train_force), "Newtons of force.")

print("A 1kg bomb supplies", bomb_energy, "Joules.")

print("The GE train does", train_work, "Joules of work over", train_distance, "meters.")

