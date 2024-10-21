from data_company import directory_large_company

def header():
    print("==========================================================================================================================================")
    print("============================= Direktori Pencarian Perusahaan Industri di Kota Surabaya ==================================")
    print("==========================================================================================================================================")

def main_menu():
    print("""                       ******************** Main Menu *************************
                        ----------------- Nomor Option ------------------------
                        1 = Display Company-----(Melihat semua data yang sudah tersedia)
                        2 = Add Company --------(Membuat data baru yang belum tersedia)
                        3 = Update Company------(Memperbarui data yang sudah tersedia)
                        4 = Delete Company------(Menghapus data yang sudah tersedia)
                        5 = Exit ---------------(Meninggalkan Program)
                      **********************************************************""")

def find_company_by_uniqcode(code):
    for item in directory_large_company:
        if item['UniqCode'] == code:
            return item
    return None

def display_company_details(companies=None):
    print("  NameCompany        NoReg         Product                   Address              PostCode            Email                 UniqCode")
    print("=" * 135)
    for item in (companies or directory_large_company):
        print(f"{item['NameCompany']:20} {item['NoReg']:10} {item['Product']:25} {item['Address']:25} {item['PostCode']:10} {item['Email']:30} {item['UniqCode']:10}")

def confirm_action(prompt):
    return input(prompt) == "1"

def get_user_input(prompt, validation_func=None, max_attempts=3):
    for attempt in range(max_attempts):
        value = input(prompt)
        if validation_func is None or validation_func(value):
            return value
        print(f"Input tidak valid. Percobaan {attempt + 1} dari {max_attempts}. Silakan coba lagi.")
    print("Terlalu banyak percobaan tidak valid. Kembali ke menu utama.")
    return None

def validate_uniqcode(code):
    return len(code) == 4 and find_company_by_uniqcode(code) is not None

def validate_postcode(postcode):
    return postcode.isdigit() and len(postcode) == 6

def validate_length(value, max_length):
    return len(value) <= max_length

def validate_name(value):
    return validate_length(value, 20)

def validate_no_reg(value):
    return validate_length(value, 10)

def validate_product(value):
    return validate_length(value, 25)

def validate_address(value):
    return validate_length(value, 25)

def validate_email(value):
    return validate_length(value, 30)

def validate_display_option(option):
    return option in ["1", "2", "3"]

def validate_main_menu_option(option):
    return option in ["1", "2", "3", "4", "5"]
def display_company():
    print("""                     ******************** Display Company Menu **********************
                        ----------------- Nomor Option ------------------------
                        1 = Shown All Name Company 
                        2 = Shown All Product Company 
                        3 = Back to Main Menu  
                    ****************************************************************""")
    
    option = get_user_input("Masukkan nomor Option yang ingin anda jalankan: ", validate_display_option)
    if option is None:
        return

    if option == "1":
        print("  NameCompany\n" + "=" * 20)
        for i in directory_large_company:
            print(f"{i['NameCompany']:20}")

        if confirm_action("Apakah nama perusahaan yang Anda cari telah tersedia? 1. Sudah 2. Belum: "):
            # User confirmed that the company name is available
            display_company_details()
        else:
            # User indicated that the company name is not available
            print("Data tidak tersedia")
            
    elif option == "2":
        print("  Product\n" + "=" * 25)
        for i in directory_large_company:
            print(f"{i['Product']:25}")

        confirm_action_response = input("Apakah nama perusahaan yang Anda cari telah tersedia? 1. Sudah 2. Belum: ")
        if confirm_action_response == "1":
            code = get_user_input("Masukkan Uniqcode perusahaan [4chara, capital]: ", validate_uniqcode)
            if code is None:
                return
            company = find_company_by_uniqcode(code)
            if company:
                display_company_details([company])
            else:
                print("Data tidak ditemukan.")
        else:
            print("Data tidak tersedia")
    
    elif option == "3":
        main_menu()

        
def add_company():
    print("""                       ******************** 1. Add Company Menu *************************
                        ----------------- Nomor Option ------------------------
                        1 = Input to add new data  
                        2 = Back to Main Menu  
                      **********************************************************""")

    input_user_add_company = input("Masukkan nomor Option yang ingin anda jalankan: ")

    if input_user_add_company == "1":
        input_uniq_code = get_user_input("Masukkan Uniqcode perusahaan [4chara, capital]: ", validate_input, "uniqcode")
        if input_uniq_code is None:
            return  # Kembali ke menu utama
        
        directory_dict = {item['UniqCode']: item for item in directory_large_company}
        if input_uniq_code in directory_dict:
            print("Perusahaan sudah ada.")
            return

        print("Silakan masukkan detail perusahaan yang ingin ditambahkan:")
        name_company = get_user_input("Masukkan nama perusahaan: ", validate_name, "name")
        no_reg = get_user_input("Masukkan nomor registrasi: ", validate_no_reg, "no_reg")
        product = input("Masukkan produk: ")
        address = get_user_input("Masukkan alamat: ", validate_address, "address")
        post_code = get_user_input("Masukkan kode pos: ", validate_postcode, "postcode")
        email = get_user_input("Masukkan email: ", validate_email, "email")

        new_company = {
            "NameCompany": name_company,
            "NoReg": no_reg,
            "Product": product,
            "Address": address,
            "PostCode": post_code,
            "Email": email,
            "UniqCode": input_uniq_code 
        }
        
        directory_large_company.append(new_company)

        if confirm_action("Apakah anda ingin menyimpan data? 1.Ya / 2. Tidak: "):
            print("Data berhasil disimpan.")
        else:    
            print("Data tidak tersimpan.")

def update_company():
    print("""                       ******************** 1. Update Company Menu *************************
                        ----------------- Nomor Option ------------------------
                        1 = Update Data 
                        2 = Back to Main Menu  
                      **********************************************************""")

    input_user_update_company = input("Masukkan nomor Option yang ingin anda jalankan: ")

    if input_user_update_company == "1":
        input_uniq_code = get_user_input("Masukkan Uniqcode perusahaan [4chara, capital]: ", validate_input, "uniqcode")
        if input_uniq_code is None:
            return  # Kembali ke menu utama

        company = find_company_by_uniqcode(input_uniq_code)
        if company:
            print("  NameCompany        NoReg         Product                   Address              PostCode            Email                 UniqCode")
            print("=" * 135)
            print(f"{company['NameCompany']:20} {company['NoReg']:10} {company['Product']:25} {company['Address']:25} {company['PostCode']:10} {company['Email']:30} {company['UniqCode']:10}") 

            if confirm_action("Apakah Anda ingin melanjutan pengkinian data? 1.Ya / 2. Tidak: "):
                for key in company.keys():
                    new_value = input(f"Masukkan {key} baru (tekan Enter untuk tetap): ")
                    if new_value:
                        company[key] = new_value
                print("Data berhasil diupdate.")
            else:
                print("Pengkinian dibatalkan.")
        else:
            print("Data tidak ditemukan.")  

def delete_company():
    print("""                       ******************** 1. Delete Company Menu *************************
                        ----------------- Nomor Option ------------------------
                        1 = Delete Data 
                        2 = Back to Main Menu  
                      **********************************************************""")

    input_user_delete_company = input("Masukkan nomor Option yang ingin anda jalankan: ")

    if input_user_delete_company == "1":
        input_uniq_code = get_user_input("Masukkan Uniqcode perusahaan [4chara, capital]: ", validate_input, "uniqcode")
        if input_uniq_code is None:
            return  # Kembali ke menu utama

        company = find_company_by_uniqcode(input_uniq_code)
        if company:
            print("  NameCompany        NoReg         Product                   Address              PostCode            Email                 UniqCode")
            print("=" * 135)
            print(f"{company['NameCompany']:20} {company['NoReg']:10} {company['Product']:25} {company['Address']:25} {company['PostCode']:10} {company['Email']:30} {company['UniqCode']:10}")

            if confirm_action("Apakah Anda ingin menghapus data? 1.Ya / 2. Tidak: "):
                directory_large_company.remove(company)
                print("Data berhasil dihapus.")
            else:
                print("Data batal dihapus.")
        else:
            print("Data tidak ditemukan dengan kode unik tersebut.")

# Main program loop
header()
while True:
    main_menu()
    input_user_main_menu = input("Masukkan nomor Option yang ingin anda jalankan: ")
    
    if input_user_main_menu == "1":
        display_company()
    elif input_user_main_menu == "2":
        add_company()
    elif input_user_main_menu == "3":
        update_company()
    elif input_user_main_menu == "4":
        delete_company()
    elif input_user_main_menu == "5":
        print("Anda keluar dari program.")
        break