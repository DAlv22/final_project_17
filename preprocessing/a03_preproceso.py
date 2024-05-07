# Librerias -----------------------------------------------
import pandas as pd
import re

# Data change ---------------------------------------------

def change_data_type(df):
    """
    Cambia el tipo de dato de la columna 'TotalCharges' a numérico.
    Elimina filas con valores nulos en 'TotalCharges'.
    """
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df = df.drop(df[df['TotalCharges'].isna()].index)
    df = df.reset_index(drop=True)
    return df

# Merge datasets -------------------------------------------

def merge_datasets(contract, internet, personal, phone):
    """
    Combina los datasets en uno solo utilizando la columna 'customerID' como clave de unión.
    """
    df = contract.merge(internet, how='left', on='customerID')
    df = df.merge(personal, how='left', on='customerID')
    df = df.merge(phone, how='left', on='customerID')
    return df

# Fill missing values ---------------------------------------- 

def fill_missing_values(df):
    """
    Rellena los valores nulos en columnas específicas con 'No' o 'No Service'.
    """
    for col in ["OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies", "MultipleLines"]:
        df[col] = df[col].fillna("No")
    
    df["InternetService"] = df["InternetService"].fillna("No Service")
    return df

# Create new columns ------------------------------------------

def create_columns(df):
    """
    Crea las columnas 'exited' y 'days_since_join'.
    """
    # Creación de la columna 'exited'
    df['exited'] = (df['EndDate'] != 'No').astype(int)
    
    # Creación de la columna 'days_since_join'
    df.loc[df['EndDate'] == 'No', 'EndDate'] = '2020-02-01 00:00:00'
    df['BeginDate'] = pd.to_datetime(df['BeginDate'], format='%Y-%m-%d')
    df['EndDate'] = pd.to_datetime(df['EndDate'], format='%Y-%m-%d %H:%M:%S')
    extraction_date = pd.to_datetime('2020-02-01 00:00:00')
    df['days_since_join'] = (extraction_date - df['BeginDate']).dt.days
    
    return df

# Snake case ----------------------------------------------

def to_snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def preprocess_columns(df):
    """
    Convertir nombres de columnas a snake_case y convertir columnas con valores "Yes" y "No" a valores binarios (0 y 1)
    """
    df.columns = [to_snake_case(col) for col in df.columns]

    for col in df.columns:
        if set(df[col].unique()) == {"No", "Yes"}:
            df[col] = (df[col] == "Yes").astype(int)

    df["gender"] = (df["gender"] == "Male").astype("int")

    return df