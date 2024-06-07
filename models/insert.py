import csv
from sqlalchemy import Sequence
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker  
from models.connection import get_oracle_connection
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Define a database connection engine
engine = create_engine('oracle://', creator=get_oracle_connection)

# Create a declarative base
Base = declarative_base()



class ProducaoPlastico(Base):
    __tablename__ = 'gs_producao_plastico'

    id = Column(Integer, Sequence('id_producao_seq'), primary_key=True)
    entidade = Column(String(100), nullable=False)  
    ano = Column(Integer, unique=True, nullable=False)
    producao_anual = Column(Integer, nullable=False)


class ParticipacaoDespejo(Base):
    __tablename__ = 'gs_participacao_despejo_residuo_plastico'

    id = Column(Integer, Sequence('id_despejo_seq'), primary_key=True)
    entidade = Column(String(100), nullable=False, unique=True)  
    codigo = Column(String(5), unique=True)
    ano = Column(Integer, nullable=False)
    participacao = Column(Float, nullable=False)

# Create tables in the database
Base.metadata.create_all(engine)

# Function to read CSV file and insert data into the corresponding table
def insert_csv_data_into_table(session, csv_file, TableClass):
    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            

            
            for row in reader:
                # Ignore the first column (index column)
                row = {key: value for key, value in row.items() if key != ''}
                
                print("Row:", row)  # Add this line to debug
                
                record = TableClass(**row)
                session.add(record)
                
        session.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()



def main():
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # CSV files and corresponding table classes
    csv_files = ['testeplastico.csv', 'testedespejo.csv']
    table_classes = [ProducaoPlastico, ParticipacaoDespejo]
    
    for csv_file, TableClass in zip(csv_files, table_classes):
        insert_csv_data_into_table(session, csv_file, TableClass)
    
    session.close()

if __name__ == "__main__":
    main()
