#!/usr/bin/env python
# coding: utf-8

# In[8]:



import random



lenght=int(input('Ingresa la longitud deseada de tu contraseña, la misma debe tener por lo menos 8 caracteres: '))

while lenght<8:
    lenght=int(input('Recorda que la contraseña debe tener por lo menos 8 caracteres: '))

base=('bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()-_=+[{}]|<,.>/?`')


def generador_contraseña(lenght, base):
    pass_list=list(base)

    final_list=(random.choices(pass_list, k=lenght))

    cadena = ''.join(final_list)

    print(cadena)
    
    
generador_contraseña(lenght, base)


# In[ ]:





# In[ ]:



    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




