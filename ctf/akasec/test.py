import pywintrace

def read_etl(file_path):
    try:
        parser = pywintrace.etl.ETLParser(file_path)
        for event in parser:
            print(event)
    except Exception as e:
        print(f"Error reading ETL file: {e}")

if __name__ == "__main__":
    file_path = 'memdump1.mem'
    read_etl(file_path)
