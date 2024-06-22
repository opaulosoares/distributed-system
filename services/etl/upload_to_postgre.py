import pandas as pd
import psycopg2
import logging
import math

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define PostgreSQL connection details
pg_host = "your_postgres_host"
pg_database = "your_database"
pg_user = "your_user"
pg_password = "your_password"

# Function to create PostgreSQL connection
def get_pg_connection():
    try:
        connection = psycopg2.connect(
            host=pg_host,
            database=pg_database,
            user=pg_user,
            password=pg_password
        )
        logger.info("Successfully connected to PostgreSQL.")
        return connection
    except Exception as e:
        logger.error(f"Error connecting to PostgreSQL: {e}")
        raise

# Function to create tables
def create_tables(conn):
    create_lab_table = """
    CREATE TABLE IF NOT EXISTS laboratories (
        cnpj VARCHAR PRIMARY KEY,
        name VARCHAR
    );
    """
    
    create_medicine_table = """
    CREATE TABLE IF NOT EXISTS medicines (
        substancia VARCHAR,
        cnpj VARCHAR,
        laboratorio VARCHAR,
        codigo_ggrem VARCHAR,
        registro VARCHAR,
        ean1 VARCHAR,
        ean2 VARCHAR,
        produto VARCHAR,
        apresentacao VARCHAR,
        classe_terapeutica VARCHAR,
        tipo_produto VARCHAR,
        regime_preco VARCHAR,
        pf_sem_impostos VARCHAR,
        pf_0 VARCHAR,
        pf_12 VARCHAR,
        pf_12_alc VARCHAR,
        pf_17 VARCHAR,
        pf_17_alc VARCHAR,
        pf_17_5 VARCHAR,
        pf_17_5_alc VARCHAR,
        pf_18 VARCHAR,
        pf_18_alc VARCHAR,
        pf_19 VARCHAR,
        pf_19_alc VARCHAR,
        pf_19_5 VARCHAR,
        pf_19_5_alc VARCHAR,
        pf_20 VARCHAR,
        pf_20_alc VARCHAR,
        pf_20_5 VARCHAR,
        pf_21 VARCHAR,
        pf_21_alc VARCHAR,
        pf_22 VARCHAR,
        pf_22_alc VARCHAR,
        pmc_sem_imposto VARCHAR,
        pmc_0 VARCHAR,
        pmc_12 VARCHAR,
        pmc_12_alc VARCHAR,
        pmc_17 VARCHAR,
        pmc_17_alc VARCHAR,
        pmc_17_5 VARCHAR,
        pmc_17_5_alc VARCHAR,
        pmc_18 VARCHAR,
        pmc_18_alc VARCHAR,
        pmc_19 VARCHAR,
        pmc_19_alc VARCHAR,
        pmc_19_5 VARCHAR,
        pmc_19_5_alc VARCHAR,
        pmc_20 VARCHAR,
        pmc_20_alc VARCHAR,
        pmc_20_5 VARCHAR,
        pmc_21 VARCHAR,
        pmc_21_alc VARCHAR,
        pmc_22 VARCHAR,
        pmc_22_alc VARCHAR,
        restricao_hospitalar VARCHAR,
        cap VARCHAR,
        confaz_87 VARCHAR,
        icms_0 VARCHAR,
        analise_recursal VARCHAR,
        lista_concessao_credito_tributario VARCHAR,
        comercializacao_2022 VARCHAR,
        tarja VARCHAR,
        destinacao_comercial VARCHAR,
        PRIMARY KEY (codigo_ggrem)
    );
    """

    with conn.cursor() as cursor:
        cursor.execute(create_lab_table)
        cursor.execute(create_medicine_table)
        conn.commit()

# Function to insert laboratory records
def insert_laboratories(conn, laboratories):
    insert_query = """
    INSERT INTO laboratories (cnpj, name) VALUES (%s, %s)
    ON CONFLICT (cnpj) DO NOTHING;
    """
    with conn.cursor() as cursor:
        for lab in laboratories:
            cursor.execute(insert_query, (lab['CNPJ'], lab['LABORATÓRIO']))
        conn.commit()

# Function to insert medicine records
def insert_medicines(conn, medicines):
    insert_query = """
    INSERT INTO medicines (substancia, cnpj, laboratorio, codigo_ggrem, registro, ean1, ean2, produto, apresentacao,
                           classe_terapeutica, tipo_produto, regime_preco, pf_sem_impostos, pf_0, pf_12, pf_12_alc,
                           pf_17, pf_17_alc, pf_17_5, pf_17_5_alc, pf_18, pf_18_alc, pf_19, pf_19_alc, pf_19_5,
                           pf_19_5_alc, pf_20, pf_20_alc, pf_20_5, pf_21, pf_21_alc, pf_22, pf_22_alc, pmc_sem_imposto,
                           pmc_0, pmc_12, pmc_12_alc, pmc_17, pmc_17_alc, pmc_17_5, pmc_17_5_alc, pmc_18, pmc_18_alc,
                           pmc_19, pmc_19_alc, pmc_19_5, pmc_19_5_alc, pmc_20, pmc_20_alc, pmc_20_5, pmc_21, pmc_21_alc,
                           pmc_22, pmc_22_alc, restricao_hospitalar, cap, confaz_87, icms_0, analise_recursal,
                           lista_concessao_credito_tributario, comercializacao_2022, tarja, destinacao_comercial)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (codigo_ggrem) DO NOTHING;
    """
    with conn.cursor() as cursor:
        for med in medicines:
            cursor.execute(insert_query, (
                med["SUBSTÂNCIA"], med["CNPJ"], med["LABORATÓRIO"], med["CÓDIGO GGREM"], med["REGISTRO"], med["EAN 1"], 
                med["EAN 2"], med["PRODUTO"], med["APRESENTAÇÃO"], med["CLASSE TERAPÊUTICA"], 
                med["TIPO DE PRODUTO (STATUS DO PRODUTO)"], med["REGIME DE PREÇO"], med["PF Sem Impostos"], med["PF 0%"], 
                med["PF 12%"], med["PF 12% ALC"], med["PF 17%"], med["PF 17% ALC"], med["PF 17,5%"], med["PF 17,5% ALC"], 
                med["PF 18%"], med["PF 18% ALC"], med["PF 19%"], med["PF 19% ALC"], med["PF 19,5%"], med["PF 19,5% ALC"], 
                med["PF 20%"], med["PF 20% ALC"], med["PF 20,5%"], med["PF 21%"], med["PF 21% ALC"], med["PF 22%"], 
                med["PF 22% ALC"], med["PMC Sem Imposto"], med["PMC 0%"], med["PMC 12%"], med["PMC 12% ALC"], 
                med["PMC 17%"], med["PMC 17% ALC"], med["PMC 17,5%"], med["PMC 17,5% ALC"], med["PMC 18%"], 
                med["PMC 18% ALC"], med["PMC 19%"], med["PMC 19% ALC"], med["PMC 19,5%"], med["PMC 19,5% ALC"], 
                med["PMC 20%"], med["PMC 20% ALC"], med["PMC 20,5%"], med["PMC 21%"], med["PMC 21% ALC"], med["PMC 22%"], 
                med["PMC 22% ALC"], med["RESTRIÇÃO HOSPITALAR"], med["CAP"], med["CONFAZ 87"], med["ICMS 0%"], 
                med["ANÁLISE RECURSAL"], med["LISTA DE CONCESSÃO DE CRÉDITO TRIBUTÁRIO (PIS/COFINS)"], 
                med["COMERCIALIZAÇÃO 2022"], med["TARJA"], med["DESTINAÇÃO COMERCIAL"]
            ))
        conn.commit()

# Function to run PostgreSQL transactions for laboratories in batches
def run_pg_lab_transactions(laboratories, batch_size=100):
    connection = get_pg_connection()
    total_batches = math.ceil(len(laboratories) / batch_size)
    with connection:
        create_tables(connection)
        for i in range(total_batches):
            batch = laboratories[i * batch_size: (i + 1) * batch_size]
            insert_laboratories(connection, batch)
    logger.info("Successfully created laboratory records in PostgreSQL.")

# Function to run PostgreSQL transactions for medicines in batches
def run_pg_med_transactions(medicines, batch_size=100):
    connection = get_pg_connection()
    total_batches = math.ceil(len(medicines) / batch_size)
    with connection:
        for i in range(total_batches):
            batch = medicines[i * batch_size: (i + 1) * batch_size]
            insert_medicines(connection, batch)
    logger.info("Successfully created medicine records in PostgreSQL.")

# Read XLS file into a DataFrame
xls_file_path = "/app/xls_conformidade_site_20240604_162827951.xls"
try:
    df = pd.read_excel(xls_file_path, skiprows=41)  # Skip the first 41 rows
    df.columns = df.columns.str.strip()  # Strip any leading/trailing spaces from column names
    logger.info("Successfully read XLS file into DataFrame.")
except Exception as e:
    logger.error(f"Error reading XLS file: {e}")
    raise

# Specify the columns to be read
columns = [
    "SUBSTÂNCIA", "CNPJ", "LABORATÓRIO", "CÓDIGO GGREM", "REGISTRO", "EAN 1", "EAN 2", "PRODUTO",
    "APRESENTAÇÃO", "CLASSE TERAPÊUTICA", "TIPO DE PRODUTO (STATUS DO PRODUTO)", "REGIME DE PREÇO",
    "PF Sem Impostos", "PF 0%", "PF 12%", "PF 12% ALC", "PF 17%", "PF 17% ALC", "PF 17,5%", 
    "PF 17,5% ALC", "PF 18%", "PF 18% ALC", "PF 19%", "PF 19% ALC", "PF 19,5%", "PF 19,5% ALC",
    "PF 20%", "PF 20% ALC", "PF 20,5%", "PF 21%", "PF 21% ALC", "PF 22%", "PF 22% ALC",
    "PMC Sem Imposto", "PMC 0%", "PMC 12%", "PMC 12% ALC", "PMC 17%", "PMC 17% ALC", "PMC 17,5%",
    "PMC 17,5% ALC", "PMC 18%", "PMC 18% ALC", "PMC 19%", "PMC 19% ALC", "PMC 19,5%", 
    "PMC 19,5% ALC", "PMC 20%", "PMC 20% ALC", "PMC 20,5%", "PMC 21%", "PMC 21% ALC", 
    "PMC 22%", "PMC 22% ALC", "RESTRIÇÃO HOSPITALAR", "CAP", "CONFAZ 87", "ICMS 0%",
    "ANÁLISE RECURSAL", "LISTA DE CONCESSÃO DE CRÉDITO TRIBUTÁRIO (PIS/COFINS)",
    "COMERCIALIZAÇÃO 2022", "TARJA", "DESTINAÇÃO COMERCIAL"
]

# Check if all columns exist in the DataFrame, strip any leading/trailing spaces
df.columns = df.columns.str.strip()
missing_columns = [col for col in columns if col not in df.columns]
if missing_columns:
    logger.error(f"Missing columns in the DataFrame: {missing_columns}")
    raise KeyError(f"Missing columns: {missing_columns}")

df = df[columns]

# Create list of unique laboratories
unique_laboratories = df[['CNPJ', 'LABORATÓRIO']].drop_duplicates().to_dict('records')

# Convert DataFrame rows to a list of dictionaries for medicines
medicines = df.to_dict('records')

# Run the transactions in batches
try:
    run_pg_lab_transactions(unique_laboratories, batch_size=100)
    run_pg_med_transactions(medicines, batch_size=100)
    logger.info("Data uploaded to PostgreSQL successfully!")
except Exception as e:
    logger.error(f"Error uploading data to PostgreSQL: {e}")
    raise
