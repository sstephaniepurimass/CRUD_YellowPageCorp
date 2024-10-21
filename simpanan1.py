# print("==========================================================================================================================================\n")
# print("============================= Direktori Pencarian Perusahaan Industri Besar dan Sedang di Kota Surabaya ==================================\n")
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

# # Import data from another file (data_company)
# from data_company import directory_large_company

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
        
#         # Display all company names
#         for item in directory_large_company:
#             print(f"{item['NameCompany']:20}")

#         # Ask if data is available
#         company_name = input("Apakah Anda mencari data perusahaan? (ya/tidak): ").strip().lower()
#         if company_name == "ya":
#             search_name = input("Masukkan nama perusahaan yang dicari: ")
#             found = False
#             print("  Data Perusahaan")
#             print("=" * 20)
#             for item in directory_large_company:
#                 if search_name.lower() in item['NameCompany'].lower():
#                     print(f"{item['NameCompany']:20} {item['NoReg']} {item['Product']} {item['Address']} {item['PostCode']} {item['Email']} {item['UniqCode']}")
#                     found = True
#             if not found:
#                 print("Data does not exist.")

#         input("Tekan Enter untuk kembali ke menu display...")  # Return to display menu
#         display()  # Go back to display menu

#     elif input_user == "2":
#         print("  Product Company")
#         print("=" * 20)
        
#         # Display all products
#         for item in directory_large_company:
#             print(f"{item['Product']:20}")

#         # Ask if data is available
#         product_name = input("Apakah Anda mencari data produk? (ya/tidak): ").strip().lower()
#         if product_name == "ya":
#             search_product = input("Masukkan nama produk yang dicari: ")
#             found = False
#             print("  Data Produk")
#             print("=" * 20)
#             for item in directory_large_company:
#                 if search_product.lower() in item['Product'].lower():
#                     print(f"{item['Product']:20} {item['NameCompany']} {item['NoReg']} {item['Address']} {item['PostCode']} {item['Email']} {item['UniqCode']}")
#                     found = True
#             if not found:
#                 print("Data does not exist.")

#             # After showing product data, prompt for UniqCode
#             if found:
#                 uniq_code = input("Masukkan UniqCode untuk informasi lebih lanjut: ")
#                 # You can implement any further action here based on UniqCode

#         input("Tekan Enter untuk kembali ke menu display...")  # Return to display menu
#         display()  # Go back to display menu

#     elif input_user == "3":
#         return  # Back to Main Menu
#     else:
#         print("Nomor option yang anda masukkan tidak tersedia! Silahkan input 1/2/3")


# Print headers
# Import data from another file (data_company)
from data_company import directory_large_company


# Initialize the counter
total_count = len(directory_large_company)

# Print headers
print("=" * 150)
print("=" * 80 + " Direktori Pencarian Perusahaan Industri Besar dan Sedang di Kota Surabaya " + "=" * 80)
print("=" * 150)

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

        for item in directory_large_company:
            print(f"{item['NameCompany']:20}")

        name_company_ = input("Apakah nama perusahaan yang anda cari tersedia? (1.Ya / 2.Tidak): ")
        if name_company_ == "1":
            print("  NameCompany        NoReg         Product                   Address              PostCode            Email                 UniqCode")
            print("=" * 135)

            found = False
            for item in directory_large_company:
                print(f"{item['NameCompany']:20} {item['NoReg']:10} {item['Product']:25} {item['Address']:25} {item['PostCode']:10} {item['Email']:30} {item['UniqCode']:10}")
                found = True

            if not found:
                print("Data does not exist.")

        print(f"Total data saat ini: {total_count}")  # Display total count
        input("Tekan Enter untuk kembali ke Menu Display")
        display()

def create():
    """To add new data"""
    global total_count  # Use the global variable

    print("""                       ******************** 1. Create Data Menu *************************\n
                        ----------------- Nomor Option ------------------------\n
                        1 = Input to add new data  
                        2 = Back to Main Menu  
        
                      **********************************************************\n
            """)

    input_user = input("Masukkan nomor option yang ingin anda jalankan:  ") 

    if input_user == "1":
        uniq_code = input("Masukkan kode unik perusahaan (tidak bisa dirubah): ").strip().lower()

        print("Silakan masukkan detail perusahaan yang ingin ditambahkan:")
        name_company = input("Masukkan nama perusahaan: ")
        no_reg = input("Masukkan nomor registrasi: ")
        product = input("Masukkan produk: ")
        address = input("Masukkan alamat: ")
        post_code = input("Masukkan kode pos: ")
        email = input("Masukkan email: ")

        new_company = {
            "NameCompany": name_company,
            "NoReg": no_reg,
            "Product": product,
            "Address": address,
            "PostCode": post_code,
            "Email": email,
            "UniqCode": uniq_code
        }

        directory_large_company.append(new_company)
        total_count += 1  # Increment the total count
        print("Data berhasil ditambahkan.")
        print(f"Total data saat ini: {total_count}")  # Display total count

        input("Tekan Enter untuk melihat data yang diperbarui...")
        display()


def update():
    """To update data"""
    global total_count  # Use the global variable

    print("""                       ******************** 1. Update Data Menu *************************\n
                        ----------------- Nomor Option ------------------------\n
                        1 = Update Data 
                        2 = Back to Main Menu  
        
                      **********************************************************\n
            """)

    input_user = input("Masukkan nomor option yang ingin anda jalankan:  ") 

    if input_user == "1":
        uniq_code = input("Masukkan kode unik perusahaan yang ingin diupdate: ").strip().lower()
        
        company_to_update = next((item for item in directory_large_company if item['UniqCode'].lower() == uniq_code), None)

        if company_to_update:
            print("Data yang ada:")
            print(f"  NameCompany: {company_to_update['NameCompany']}")
            print(f"  NoReg: {company_to_update['NoReg']}")
            print(f"  Product: {company_to_update['Product']}")
            print(f"  Address: {company_to_update['Address']}")
            print(f"  PostCode: {company_to_update['PostCode']}")
            print(f"  Email: {company_to_update['Email']}")
            print(f"  UniqCode: {company_to_update['UniqCode']}")
            
            proceed = input("Apakah anda ingin melanjutkan update data? (1.Ya / 2.Tidak): ")
            if proceed == "1":
                name_company = input("Masukkan nama perusahaan baru (tekan Enter untuk tetap): ")
                no_reg = input("Masukkan nomor registrasi baru (tekan Enter untuk tetap): ")
                product = input("Masukkan produk baru (tekan Enter untuk tetap): ")
                address = input("Masukkan alamat baru (tekan Enter untuk tetap): ")
                post_code = input("Masukkan kode pos baru (tekan Enter untuk tetap): ")
                email = input("Masukkan email baru (tekan Enter untuk tetap): ")

                if name_company:
                    company_to_update['NameCompany'] = name_company
                if no_reg:
                    company_to_update['NoReg'] = no_reg
                if product:
                    company_to_update['Product'] = product
                if address:
                    company_to_update['Address'] = address
                if post_code:
                    company_to_update['PostCode'] = post_code
                if email:
                    company_to_update['Email'] = email

                print("Data berhasil diupdate.")
                input("Tekan Enter untuk melihat data yang diperbarui...")
                display()  
            else:
                print("Update dibatalkan.")

        else:
            print("Data tidak ditemukan dengan kode unik tersebut.")

    elif input_user == "2":
        return  
    else:
        print("Nomor option yang anda masukkan tidak tersedia! Silahkan input 1/2")

def delete():
    """To delete data"""
    global total_count  # Use the global variable

    print("""                       ******************** 1. Delete Data Menu *************************\n
                        ----------------- Nomor Option ------------------------\n
                        1 = Delete Data 
                        2 = Back to Main Menu  
        
                      **********************************************************\n
            """)

    input_user = input("Masukkan nomor option yang ingin anda jalankan:  ") 

    if input_user == "1":
        uniq_code = input("Masukkan kode unik perusahaan yang ingin dihapus: ").strip().lower()

        company_to_delete = next((item for item in directory_large_company if item['UniqCode'].lower() == uniq_code), None)

        if company_to_delete:
            print("Data yang akan dihapus:")
            print(f"  NameCompany: {company_to_delete['NameCompany']}")
            print(f"  NoReg: {company_to_delete['NoReg']}")
            print(f"  Product: {company_to_delete['Product']}")
            print(f"  Address: {company_to_delete['Address']}")
            print(f"  PostCode: {company_to_delete['PostCode']}")
            print(f"  Email: {company_to_delete['Email']}")
            print(f"  UniqCode: {company_to_delete['UniqCode']}")
            
            proceed = input("Apakah anda ingin menghapus data ini? (1.Ya / 2.Tidak): ")
            if proceed == "1":
                directory_large_company.remove(company_to_delete)
                total_count -= 1  # Decrement the total count
                print("Data berhasil dihapus.")
                print(f"Total data saat ini: {total_count}")  # Display total count
            else:
                print("Penghapusan dibatalkan.")
        else:
            print("Data tidak ditemukan dengan kode unik tersebut.")

# Remember to include the total_count in those functions where necessary.

# Main program loop
while True:
    main_menu()
    input_user = input("Masukkan nomor option yang ingin anda jalankan:  ")
    
    if input_user == "1":
        display()  
    elif input_user == "2":
        create()  
    elif input_user == "3":
        update()  
    elif input_user == "4":
        delete()  
    elif input_user == "5":
        print("Anda telah keluar dari program.")
        break
    else:
        print("Nomor option yang anda masukkan tidak tersedia! Silahkan input 1/2/3/4/5")