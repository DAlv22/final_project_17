def unique_values(dataframe):
    for column in dataframe.columns:
        unique_values = dataframe[column].unique()
        print(f"Valores únicos en la columna '{column}':")
        print(unique_values)
        print()



def analyze_dataset(df, name):
    print(f"Análisis del conjunto de datos: {name}\n")
    
    # Información del conjunto de datos
    print("Información del conjunto de datos:")
    print(df.info())
    print("\n")
    
    # Valores únicos en cada columna
    print("Valores únicos en cada columna:")
    unique_values(df)
    print("\n")
    
    # Resumen estadístico
    print("Resumen estadístico:")
    print(df.describe())
    print("\n")
    
    # Conteo de valores nulos
    print("Conteo de valores nulos:")
    print(df.isnull().sum())
    print("\n")
    
    # Filas duplicadas
    print(f"Número total de filas duplicadas en este archivo es de {df.duplicated().sum()} filas.\n")
    
    # Muestra las primeras filas del conjunto de datos
    print("Primeras filas del conjunto de datos:")
    print(df.head(10))
    print("\n")

def analyze_all_datasets(contract_data, personal_data, internet_data, phone_data):
    analyze_dataset(contract_data, "contract")
    analyze_dataset(personal_data, "personal")
    analyze_dataset(internet_data, "internet")
    analyze_dataset(phone_data, "phone")




    # access each datase
if __name__ == "__main__":
    folder_path = 'files/datasets/input/'
    data = load_data(folder_path)
    contract_data = data['contract']
    personal_data = data['personal']
    internet_data = data['internet']
    phone_data = data['phone']