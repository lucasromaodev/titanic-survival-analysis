import downloadTitanicCsv
import dataCleasing

def main():
    csv_file_path = downloadTitanicCsv.download_titanic_csv()
    dataCleasing.clean_titanic_dataset(csv_file_path)
    
if __name__ == "__main__":
    main()
