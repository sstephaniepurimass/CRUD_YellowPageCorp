# ===================================
# [Direktori Pencarian Perusahaan Industri Besar dan Sedang di Kota Surabaya]
# ===================================
# Developed by. Stephanie Purimas
# JCDS - 0412


# /************************************/
print("===== Direktori Pencarian Perusahaan Industri Besar dan Sedang di Kota Surabaya =====")   
# /===== Data Model =====/
# Create your data model here


directory_large_company = []  # <-- This should be here to store the company data
data_large_company = {
        "NameCompany" : "",
        "NoReg" : "",
        "Product" : "",
        "Address" : "",
        "PostCode" : "",
        "Email" : "",
        "UniqCode" : "",
        } 


# /===== Feature Program =====/
# Create your feature program here
  

print("""      
                    ******************** Nomor Option **********************
                    1 = display   (Melihat semua data yang sudah tersedia)
                    2 = create    (Membuat data baru yang belum tersedia)
                    3 = update    (Memperbarui data yang sudah tersedia)
                    4 = delete    (Menghapus data yang sudah tersedia)
                    5 = exit      (Meninggalkan Program)
            """)

############################################################


from data_company import directory_large_company

def display():
    """Summary to show all the data."""
    if not directory_large_company:  # Check if the directory is empty
        print("Tidak ada data perusahaan yang tersedia.")
        return
    
    print("  NameCompany        NoReg         Product                   Address              PostCode            Email                 UniqCode")
    print("=" * 135)

    for item in directory_large_company:  
        print(f"{item['NameCompany']:20} {item['NoReg']:10} {item['Product']:25} {item['Address']:25} {item['PostCode']:10} {item['Email']:30} {item['UniqCode']:10}")

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

# Import data from another file (data_company)
from data_company import directory_large_company

def display():
    """Summary to show all the data."""
    print("""                       ******************** 1. Display Data Menu *************************\n
                        ----------------- Nomor Option ------------------------\n
                        1 = Shown All Name Company 
                        2 = Shown All Product Company 
                        3 = Back to Main Menu  
        
                      **********************************************************\n
            """)

    input_user = input("Masukkan nomor option yang ingin anda jalankan:  ") 

    if input_user == "1":
        print("  NameCompany")
        print("=" * 20)
        
        # Display all company names
        for item in directory_large_company:
            print(f"{item['NameCompany']:20}")

        # Ask if data is available
        company_name = input("Apakah Anda mencari data perusahaan? (ya/tidak): ").strip().lower()
        if company_name == "ya":
            search_name = input("Masukkan nama perusahaan yang dicari: ")
            found = False
            print("  Data Perusahaan")
            print("=" * 20)
            for item in directory_large_company:
                if search_name.lower() in item['NameCompany'].lower():
                    print(f"{item['NameCompany']:20} {item['NoReg']} {item['Product']} {item['Address']} {item['PostCode']} {item['Email']} {item['UniqCode']}")
                    found = True
            if not found:
                print("Data does not exist.")

        input("Tekan Enter untuk kembali ke menu display...")  # Return to display menu
        display()  # Go back to display menu

    elif input_user == "2":
        print("  Product Company")
        print("=" * 20)
        
        # Display all products
        for item in directory_large_company:
            print(f"{item['Product']:20}")

        # Ask if data is available
        product_name = input("Apakah Anda mencari data produk? (ya/tidak): ").strip().lower()
        if product_name == "ya":
            search_product = input("Masukkan nama produk yang dicari: ")
            found = False
            print("  Data Produk")
            print("=" * 20)
            for item in directory_large_company:
                if search_product.lower() in item['Product'].lower():
                    print(f"{item['Product']:20} {item['NameCompany']} {item['NoReg']} {item['Address']} {item['PostCode']} {item['Email']} {item['UniqCode']}")
                    found = True
            if not found:
                print("Data does not exist.")

            # After showing product data, prompt for UniqCode
            if found:
                uniq_code = input("Masukkan UniqCode untuk informasi lebih lanjut: ")
                # You can implement any further action here based on UniqCode

        input("Tekan Enter untuk kembali ke menu display...")  # Return to display menu
        display()  # Go back to display menu

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
        create()  # Call create function (make sure it's defined)
    elif input_user == "3":
        update()  # Call update function (make sure it's defined)
    elif input_user == "4":
        delete()  # Call delete function (make sure it's defined)
    elif input_user == "5":
        print("Anda telah keluar dari program.")
        break
    else:
        print("Nomor option yang anda masukkan tidak tersedia! Silahkan input 1/2/3/4/5")

# /===== Main Program =====/
while True:  
    print("""      
                    ******************** Nomor Option **********************
                    1 = display   (Melihat semua data yang sudah tersedia)
                    2 = create    (Membuat data baru yang belum tersedia)
                    3 = exit      (Meninggalkan Program)
            """)

    input_user = input("Masukkan nomor option yang ingin anda jalankan:  ") 
    
    if input_user == "1":
        display()  
    elif input_user == "2":
        if directory_large_company:
            print("Data sudah tersedia.")
        else:
            print("Data belum tersedia. Mari kita buat data baru.")
            create()  
    elif input_user == "3":
        print("Anda telah keluar dari program.")
        break
    else:
        print("Nomor option yang anda masukkan tidak tersedia! Silahkan input 1/2/3.")