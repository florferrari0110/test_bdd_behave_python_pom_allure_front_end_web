import random
import string

def before_all(context):
    start = 'test'
    random_number = ''.join(random.choice(string.digits)
                                          for _ in range(3))
    user_name = start + random_number
    
    context.username=user_name
    context.password='prueba'