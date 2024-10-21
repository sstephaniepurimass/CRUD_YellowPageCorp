

# # Import data from another file (data_company)
# from data_company import directory_large_company

# # Initialize the counter
# total_count = len(directory_large_company)

# print("==========================================================================================================================================\n")
# print("============================= Direktori Pencarian Perusahaan Industri di Kota Surabaya ==================================\n")
# print("==========================================================================================================================================\n")

# # Create Main Menu
# def main_menu():
#     print("""                       ******************** Main Menu *************************\n
#                         ----------------- Nomor Option ------------------------\n
#                         1 = display ---- (Melihat semua data yang sudah tersedia)
#                         2 = create ----- (Membuat data baru yang belum tersedia)
#                         3 = update ----- (Memperbarui data yang sudah tersedia)
#                         4 = delete ----- (Menghapus data yang sudah tersedia)
#                         5 = exit -------   (Meninggalkan Program)\n
#                       **********************************************************\n
#             """)

# def main_menu():
#     print("""                       ******************** Main Menu *************************\n
#                         ----------------- Nomor Option ------------------------\n
#                         1 = display ---- (Melihat semua data yang sudah tersedia)
#                         2 = create ----- (Membuat data baru yang belum tersedia)
#                         3 = update ----- (Memperbarui data yang sudah tersedia)
#                         4 = delete ----- (Menghapus data yang sudah tersedia)
#                         5 = exit -------   (Meninggalkan Program)\n
#                       **********************************************************\n
#             """)

# def display():
#     """Summary to show all the data."""
#     print("""                       ******************** 1. Display Data Menu *************************\n
#                         ----------------- Nomor Option ------------------------\n
#                         1 = Shown All Name Company 
#                         2 = Shown All Product Company 
#                         3 = Back to Main Menu  
        
#                       **********************************************************\n
#             """)

#     input_user = input("Masukkan nomor option yang ingin anda jalankan:  ") 

#     if input_user == "1":
#         print("  NameCompany")
#         print("=" * 20)

#         for item in directory_large_company:
#             print(f"{item['NameCompany']:20}")

#         name_company_ = input("Apakah nama perusahaan yang anda cari tersedia? (1.Ya / 2.Tidak): ")
#         if name_company_ == "1":
#             print("  NameCompany        NoReg         Product                   Address              PostCode            Email                 UniqCode")
#             print("=" * 135)

#             found = False
#             for item in directory_large_company:
#                 print(f"{item['NameCompany']:20} {item['NoReg']:10} {item['Product']:25} {item['Address']:25} {item['PostCode']:10} {item['Email']:30} {item['UniqCode']:10}")
#                 found = True

#             if not found:
#                 print("Data does not exist.")
#     elif input_user == "2":
#         company_name = input("Masukkan nama perusahaan yang ingin dicari: ")
#         found = False
#         print("  NameCompany        NoReg         Product                   Address              PostCode            Email                 UniqCode")
#         print("=" * 135)
        
#         for item in directory_large_company:
#             if company_name.lower() in item['NameCompany'].lower():
#                 print(f"{item['NameCompany']:20} {item['NoReg']:10} {item['Product']:25} {item['Address']:25} {item['PostCode']:10} {item['Email']:30} {item['UniqCode']:10}")
#                 found = True
        
#         if not found:
#             print("Perusahaan tidak ditemukan.")

#     elif input_user == "3":
#         return  # Back to Main Menu
#     else:
#         print("Nomor option yang anda masukkan tidak tersedia! Silahkan input 1/2/3")


        
#         input("Tekan Enter untuk kembali ke Menu Display")
#         display()

# def create():
#     """To add new data"""
#     global total_count  # Use the global variable

#     print("""                       ******************** 1. Create Data Menu *************************\n
#                         ----------------- Nomor Option ------------------------\n
#                         1 = Input to add new data  
#                         2 = Back to Main Menu  
        
#                       **********************************************************\n
#             """)

#     input_user = input("Masukkan nomor option yang ingin anda jalankan:  ") 

#     if input_user == "1":
#         uniq_code = input("Masukkan kode unik perusahaan (tidak bisa dirubah): ").strip().lower()

#         print("Silakan masukkan detail perusahaan yang ingin ditambahkan:")
#         name_company = input("Masukkan nama perusahaan: ")
#         no_reg = input("Masukkan nomor registrasi: ")
#         product = input("Masukkan produk: ")
#         address = input("Masukkan alamat: ")
#         post_code = input("Masukkan kode pos: ")
#         email = input("Masukkan email: ")

#         new_company = {
#             "NameCompany": name_company,
#             "NoReg": no_reg,
#             "Product": product,
#             "Address": address,
#             "PostCode": post_code,
#             "Email": email,
#             "UniqCode": uniq_code
#         }

#         directory_large_company.append(new_company)
#         total_count += 1  # Increment the total count
#         print("Data berhasil ditambahkan.")
#         print(f"Total data saat ini: {total_count}")  # Display total count

#         input("Tekan Enter untuk melihat data yang diperbarui...")
#         main_menu()


# def update():
#     """To update data"""
#     global total_count  # Use the global variable

#     print("""                       ******************** 1. Update Data Menu *************************\n
#                         ----------------- Nomor Option ------------------------\n
#                         1 = Update Data 
#                         2 = Back to Main Menu  
        
#                       **********************************************************\n
#             """)

#     input_user = input("Masukkan nomor option yang ingin anda jalankan:  ") 

#     if input_user == "1":
#         uniq_code = input("Masukkan kode unik perusahaan yang ingin diupdate: ").strip().lower()
        
#         company_to_update = next((item for item in directory_large_company if item['UniqCode'].lower() == uniq_code), None)

#         if company_to_update:
#             print("Data yang ada:")
#             print(f"  NameCompany: {company_to_update['NameCompany']}")
#             print(f"  NoReg: {company_to_update['NoReg']}")
#             print(f"  Product: {company_to_update['Product']}")
#             print(f"  Address: {company_to_update['Address']}")
#             print(f"  PostCode: {company_to_update['PostCode']}")
#             print(f"  Email: {company_to_update['Email']}")
#             print(f"  UniqCode: {company_to_update['UniqCode']}")
            
#             proceed = input("Apakah anda ingin melanjutkan update data? (1.Ya / 2.Tidak): ")
#             if proceed == "1":
#                 name_company = input("Masukkan nama perusahaan baru (tekan Enter untuk tetap): ")
#                 no_reg = input("Masukkan nomor registrasi baru (tekan Enter untuk tetap): ")
#                 product = input("Masukkan produk baru (tekan Enter untuk tetap): ")
#                 address = input("Masukkan alamat baru (tekan Enter untuk tetap): ")
#                 post_code = input("Masukkan kode pos baru (tekan Enter untuk tetap): ")
#                 email = input("Masukkan email baru (tekan Enter untuk tetap): ")

#                 if name_company:
#                     company_to_update['NameCompany'] = name_company
#                 if no_reg:
#                     company_to_update['NoReg'] = no_reg
#                 if product:
#                     company_to_update['Product'] = product
#                 if address:
#                     company_to_update['Address'] = address
#                 if post_code:
#                     company_to_update['PostCode'] = post_code
#                 if email:
#                     company_to_update['Email'] = email

#                 print("Data berhasil diupdate.")
#                 input("Tekan Enter untuk melihat data yang diperbarui...")
#                 main_menu()  
#             else:
#                 print("Update dibatalkan.")

#         else:
#             print("Data tidak ditemukan dengan kode unik tersebut.")

#     elif input_user == "2":
#         return  
#     else:
#         print("Nomor option yang anda masukkan tidak tersedia! Silahkan input 1/2")

# def delete():
#     """To delete data"""
#     global total_count  # Use the global variable

#     print("""                       ******************** 1. Delete Data Menu *************************\n
#                         ----------------- Nomor Option ------------------------\n
#                         1 = Delete Data 
#                         2 = Back to Main Menu  
        
#                       **********************************************************\n
#             """)

#     input_user = input("Masukkan nomor option yang ingin anda jalankan:  ") 

#     if input_user == "1":
#         uniq_code = input("Masukkan kode unik perusahaan yang ingin dihapus: ").strip().lower()

#         company_to_delete = next((item for item in directory_large_company if item['UniqCode'].lower() == uniq_code), None)

#         if company_to_delete:
#             print("Data yang akan dihapus:")
#             print(f"  NameCompany: {company_to_delete['NameCompany']}")
#             print(f"  NoReg: {company_to_delete['NoReg']}")
#             print(f"  Product: {company_to_delete['Product']}")
#             print(f"  Address: {company_to_delete['Address']}")
#             print(f"  PostCode: {company_to_delete['PostCode']}")
#             print(f"  Email: {company_to_delete['Email']}")
#             print(f"  UniqCode: {company_to_delete['UniqCode']}")
            
#             proceed = input("Apakah anda ingin menghapus data ini? (1.Ya / 2.Tidak): ")
#             if proceed == "1":
#                 directory_large_company.remove(company_to_delete)
#                 total_count -= 1  # Decrement the total count
#                 print("Data berhasil dihapus.")
#                 print(f"Total data saat ini: {total_count}")  # Display total count
#             else:
#                 print("Penghapusan dibatalkan.")
#         else:
#             print("Data tidak ditemukan dengan kode unik tersebut.")

# # Remember to include the total_count in those functions where necessary.

# # Main program loop
# while True:
#     main_menu()
#     input_user = input("Masukkan nomor option yang ingin anda jalankan:  ")
    
#     if input_user == "1":
#         display()  
#     elif input_user == "2":
#         create()  
#     elif input_user == "3":
#         update()  
#     elif input_user == "4":
#         delete()  
#     elif input_user == "5":
#         print("Anda telah keluar dari program.")
#         break
#     else:
#         print("Nomor option yang anda masukkan tidak tersedia! Silahkan input 1/2/3/4/5")


##############################################################################
######## OPSI PAKAI FUNCTION



# Initialize the counter
total_count = len(directory_large_company)

def print_header():
    print("==========================================================================================================================================\n")
    print("============================= Direktori Pencarian Perusahaan Industri di Kota Surabaya ==================================\n")
    print("==========================================================================================================================================\n")

def main_menu():
    print("""                       ******************** Main Menu *************************\n
                        ----------------- Nomor Option ------------------------\n
                        1 = display company-----(Melihat semua data yang sudah tersedia)
                        2 = add company --------(Membuat data baru yang belum tersedia)
                        3 = update company------(Memperbarui data yang sudah tersedia)
                        4 = delete company------(Menghapus data yang sudah tersedia)
                        5 = exit ---------------(Meninggalkan Program)\n
                      **********************************************************\n
            """)

def user_input(text, valid_options):
    while True:
        input_value = input(text)
        if input_value in valid_options:
            return input_value
        if input_value == "5" :
            print("Option yang anda masukkan tidak valid")
            return main_menu()
        else:
            print("Input tidak valid. Silakan masukkan salah satu dari: ")
            for option in valid_options:
                print(f"- {option}")

def display_company():
    print ()  # menambah baris kosong

    print("""                     ******************** 1. Display Data Menu **********************\n
                        ----------------- Nomor Option ------------------------\n
                        1 = Shown All Name Company 
                        2 = Shown All Product Company 
                        3 = Back to Main Menu  \n
                    ****************************************************************\n
            """)

    input_value = user_input("Masukkan nomor option yang ingin anda jalankan: ", ["1", "2", "3","4","5"])

    print ()  # menambah baris kosong
    if input_value == "1":
        print("  NameCompany")
        print("=" * 20)
        for item in directory_large_company:
            print(f"{item['NameCompany']:20}")

        if user_input("Apakah nama perusahaan yang anda cari tersedia? (1.Ya / 2.Tidak): ", ["1", "2"]) == "1":
            print("  NameCompany        NoReg         Product                   Address              PostCode            Email                 UniqCode")
            print("=" * 135)
            for item in directory_large_company:
                print(f"{item['NameCompany']:20} {item['NoReg']:10} {item['Product']:25} {item['Address']:25} {item['PostCode']:10} {item['Email']:30} {item['UniqCode']:10}")
    elif input_value == "2":
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

def add_company():
    global total_count  # Use the global variable

    print("""                       ******************** 1. Create Data Menu *************************\n
                        ----------------- Nomor Option ------------------------\n
                        1 = Input to add new data  
                        2 = Back to Main Menu  \n
          
                      **********************************************************\n
            """)

    if user_input("Masukkan nomor option yang ingin anda jalankan: ", ["1", "2"]) == "1":
        uniq_code = input("Masukkan kode unik perusahaan (kode tidak bisa dirubah): ")

        print("Silakan masukkan detail perusahaan yang ingin ditambahkan:")
        add_new_company = {
            "NameCompany": input("Masukkan nama perusahaan: "),
            "NoReg": input("Masukkan nomor registrasi: "),
            "Product": input("Masukkan produk: "),
            "Address": input("Masukkan alamat: "),
            "PostCode": input("Masukkan kode pos: "),
            "Email": input("Masukkan email: "),
            "UniqCode": uniq_code
        }

        directory_large_company.append(add_new_company)
        total_count += 1  # Increment the total count
        print("Data berhasil ditambahkan.")
        print(f"Total data saat ini: {total_count}")  # Display total count
        # TAMPILKAN SEMUA DATA DALAM BENTUK TABEL
def update_company():
    global total_count  # Use global variable

    print("""                       ******************** 1. Update Data Menu *************************\n
                        ----------------- Nomor Option ------------------------\n
                        1 = Update Data 
                        2 = Back to Main Menu  
                      **********************************************************\n
            """)

    if user_input("Masukkan nomor option yang ingin anda jalankan: ", ["1", "2"]) == "1":
        uniq_code = input("Masukkan kode unik perusahaan yang ingin diupdate: ")
        
        company_update = next((item for item in directory_large_company if item['UniqCode'] == uniq_code), None)

        if company_update:
            print("Data yang tersedia:")
            for key, value in company_update.items():
                print(f"  {key}: {value}")

            add_input = user_input("Apakah anda ingin melanjutkan update data? (1.Ya / 2.Tidak): ", ["1", "2"])
            if add_input == "1":
                for key in company_update.keys():
                    new_value = input(f"Masukkan {key} baru (tekan Enter untuk tetap): ")
                    if new_value:
                        company_update[key] = new_value
                print("Data berhasil diupdate")
            else:
                print("Update dibatalkan")
        else:
            print("Data tidak ditemukan dengan kode unik tersebut")

def delete_company():
    global total_count  # Use the global variable

    print("""                       ******************** 1. Delete Data Menu *************************\n
                        ----------------- Nomor Option ------------------------\n
                        1 = Delete Data 
                        2 = Back to Main Menu  
                      **********************************************************\n
            """)

    if user_input("Masukkan nomor option yang ingin anda jalankan: ", ["1", "2"]) == "1":
        uniq_code = input("Masukkan kode unik perusahaan yang ingin dihapus: ")

        company_delete = next((item for item in directory_large_company if item['UniqCode'] == uniq_code), None)

        if company_delete:
            print("Data yang akan dihapus:")
            for key, value in company_delete.items():
                print(f"  {key}: {value}")
            
            if user_input("Apakah anda ingin menghapus data ini? (1.Ya / 2.Tidak): ", ["1", "2"]) == "1":
                directory_large_company.remove(company_delete)
                total_count -= 1  # Decrement the total count
                print("Data berhasil dihapus")
                print(f"Total data saat ini: {total_count}")  # Display total count
            else:
                print("Penghapusan dibatalkan")
        else:
            print("Data tidak ditemukan dengan kode unik tersebut")

# Main program loop
print_header()
while True:
    main_menu()
    input_value = user_input("Masukkan nomor option yang ingin anda jalankan: ", ["1", "2", "3", "4", "5"])
    
    if input_value == "1":
        display_company()  
    elif input_value == "2":
        add_company()  
    elif input_value == "3":
        update_company()  
    elif input_value == "4":
        delete_company()  
    elif input_value == "5":
        print("Anda akan keluar dari program.")
        break
 

 #check nama variabel done
 #check input kata done
 # check docstring
 #validasi kalo 3 kali
 # ganti nama display,create, etc