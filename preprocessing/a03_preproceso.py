# Librerias ------------------------------------------- 



# Cleaning columns ---------------------------------------- 

def limpiar_columnas(dataset):
                return dataset

users_behavior = limpiar_columnas(users_behavior_raw)

# Eliminating duplicates per period ---------------------------------------- 

# ...

# Checking NAs ---------------------------------------- 

# ...

# Guardar datos ---------------------------------------- 

users_behavior.to_csv("files/datasets/intermediate/a01_users_behavior_cleaned.csv", index=False)


