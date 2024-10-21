# ===================================
# [Direktori Pencarian Perusahaan Industri Besar dan Sedang di Kota Surabaya]
# ===================================
# Developed by. Stephanie Purimas
# JCDS - 0412


# /************************************/  

# Welcoming Program
print("===== Direktori Pencarian Perusahaan Industri Besar dan Sedang di Kota Surabaya =====\n")   

# Create Main Menu
def main_menu():
    print("""                                       MAIN MENU
                    ******************** Nomor Option **********************
                    1 = display   (Melihat semua data yang sudah tersedia)
                    2 = create    (Membuat data baru yang belum tersedia)
                    3 = update    (Memperbarui data yang sudah tersedia)
                    4 = delete    (Menghapus data yang sudah tersedia)
                    5 = exit      (Meninggalkan Program)
            """)

# Import data dari file lain (data_company)
from data_company import directory_large_company

def display():                                     
    """Summary to show all the data."""
    print("  NameCompany        NoReg         Product                   Address              PostCode            Email                 UniqCode")
    print("=" * 135)
    
    for item in directory_large_company:
        print(f"{item['NameCompany']:20} {item['NoReg']:10} {item['Product']:25} {item['Address']:25} {item['PostCode']:10} {item['Email']:30} {item['UniqCode']:10}") # mengambil dari list dict dan dimasukan ke f{}

def create():                                  # Nomor Option 2
#     """Function for create new data
#     """
#     return "Data yang baru sudah tersimpan "
    print("berikut merupakan data yang telah tersedia")
    display()
















# def update():                                   # Nomor Option 3
#     """Function for update the data
#     """
#     return "Data yang diupdate telah tersimpan"

# def delete():                                   # Nomor Option 4
#     """Function for delete the data
#     """
#     return "Data telah dihapus"


# Main program loop
while True:
    main_menu()  # Display the main menu
    input_user = input("Masukkan nomor option yang ingin anda jalankan:  ") 
    
    if input_user == "1":
        display()  # Call display function
    elif input_user == "2":
    #     print("Data yang baru sudah tersimpan.")
    # elif input_user == "3":
    #     print("Data yang diupdate telah tersimpan.")
    # elif input_user == "4":
    #     print("Data telah dihapus.")
    # elif input_user == "5":
    #     print("Anda telah keluar dari program.")
    #     break
    # else:
    #     print("Nomor option yang anda masukkan tidak tersedia! Silahkan input 1/2/3/4/5")