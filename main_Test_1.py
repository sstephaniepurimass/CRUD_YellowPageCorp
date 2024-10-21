print("==========================================================================================================================================\n")
print("============================= Direktori Pencarian Perusahaan Industri Besar dan Sedang di Kota Surabaya ==================================\n")
print("==========================================================================================================================================\n")

# Create Main Menu
def main_menu():
    print("""                       ******************** Main Menu *************************\n
                        ----------------- Nomor Option ------------------------\n
                        1 = display ---- (Melihat semua data yang sudah tersedia)
                        2 = create ----- (Membuat data baru yang belum tersedia)
                        3 = update ----- (Memperbarui data yang sudah tersedia)
                        4 = delete ----- (Menghapus data yang sudah tersedia)
                        5 = exit -------   (Meninggalkan Program)\n
                      **********************************************************\n
            """)

# Import data dari file lain (data_company)
from data_company import directory_large_company

def display():
    """Summary to show all the data."""
    print("""                       ******************** 1. Display Data Menu *************************\n
                        ----------------- Nomor Option ------------------------\n
                        1 = Shown All Data 
                        2 = Shown Data based on Name Company 
                        3 = Back to Main Menu  
        
                      **********************************************************\n
            """)

    input_user = input("Masukkan nomor option yang ingin anda jalankan:  ") 

    if input_user == "1":
        print("  NameCompany        NoReg         Product                   Address              PostCode            Email                 UniqCode")
        print("=" * 135)
        
        for item in directory_large_company:
            print(f"{item['NameCompany']:20} {item['NoReg']:10} {item['Product']:25} {item['Address']:25} {item['PostCode']:10} {item['Email']:30} {item['UniqCode']:10}")

    elif input_user == "2":
        company_name = input("Masukkan nama perusahaan yang ingin dicari: ")
        found = False
        print("  NameCompany        NoReg         Product                   Address              PostCode            Email                 UniqCode")
        print("=" * 135)
        
        for item in directory_large_company:
            if company_name.lower() in item['NameCompany'].lower():
                print(f"{item['NameCompany']:20} {item['NoReg']:10} {item['Product']:25} {item['Address']:25} {item['PostCode']:10} {item['Email']:30} {item['UniqCode']:10}")
                found = True
        
        if not found:
            print("Perusahaan tidak ditemukan.")

    elif input_user == "3":
        return  # Back to Main Menu
    else:
        print("Nomor option yang anda masukkan tidak tersedia! Silahkan input 1/2/3")

def create():
    """to input new data """
    print("""                       ******************** 1. Create Data Menu *************************\n
                        ----------------- Nomor Option ------------------------\n
                        1 = Shown All Data 
                        2 = Shown Data based on Name Company 
                        3 = Back to Main Menu  
        
                      **********************************************************\n
            """)

    input_user = input("Masukkan nomor option yang ingin anda jalankan:  ") 

    if input_user == "1":
        print("  NameCompany        NoReg         Product                   Address              PostCode            Email                 UniqCode")
        print("=" * 135)
        
        for item in directory_large_company:
            print(f"{item['NameCompany']:20} {item['NoReg']:10} {item['Product']:25} {item['Address']:25} {item['PostCode']:10} {item['Email']:30} {item['UniqCode']:10}")

    elif input_user == "2":
        company_name = input("Masukkan nama perusahaan yang ingin dicari: ")
        found = False
        print("  NameCompany        NoReg         Product                   Address              PostCode            Email                 UniqCode")
        print("=" * 135)
        
        for item in directory_large_company:
            if company_name.lower() in item['NameCompany'].lower():
                print(f"{item['NameCompany']:20} {item['NoReg']:10} {item['Product']:25} {item['Address']:25} {item['PostCode']:10} {item['Email']:30} {item['UniqCode']:10}")
                found = True
        
        if not found:
            print("Perusahaan tidak ditemukan.")

    elif input_user == "3":
        return  # Back to Main Menu
    else:
        print("Nomor option yang anda masukkan tidak tersedia! Silahkan input 1/2/3")

# Main program loop
while True:
    main_menu()  # Display the main menu
    input_user = input("Masukkan nomor option yang ingin anda jalankan:  ")
    
    if input_user == "1":
        display()  # Call display function
    elif input_user == "2":
        create()  # Call create function (assuming it's defined elsewhere)
    elif input_user == "3":
        update()  # Call update function (assuming it's defined elsewhere)
    elif input_user == "4":
        delete()  # Call delete function (assuming it's defined elsewhere)
    elif input_user == "5":
        print("Anda telah keluar dari program.")
        break
    else:
        print("Nomor option yang anda masukkan tidak tersedia! Silahkan input 1/2/3/4/5")