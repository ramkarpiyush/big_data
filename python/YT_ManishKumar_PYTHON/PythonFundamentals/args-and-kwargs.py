def get_square(*args):
    val_sq = sum(map(lambda x:x**2,args))
    return val_sq

print(get_square(2,2,2))


def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Piyush", "Ramkar")

# Finding the maximum value:
def my_fun(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_fun(3, 7, 2, 9, 1))


def my_fun2(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_fun2("emil123", age = 25, city = "Oslo", hobby = "coding")


print("Start \n On a mission to master Big Data...")

from loguru import logger

def final_cart_amount(*args, discount=0.1):
  result = 0
  for amount in args:
    result = result+amount

  print(result)
  amount_after_discount = result-(result*discount)

  return amount_after_discount

final_amount_tobe_paid = final_cart_amount(100,500,100,300,500)

logger.info(final_amount_tobe_paid)