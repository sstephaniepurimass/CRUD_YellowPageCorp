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

def get_valid_uniqcode():
    return get_user_input("Masukkan Uniqcode perusahaan [4chara, capital]: ", validate_uniqcode)

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
            display_company_details()
        else:
            print("Data tidak tersedia")
            
    elif option == "2":
        print("  Product\n" + "=" * 25)
        for i in directory_large_company:
            print(f"{i['Product']:25}")

        confirm_action_response = input("Apakah nama perusahaan yang Anda cari telah tersedia? 1. Sudah 2. Belum: ")
        if confirm_action_response == "1":
            code = get_valid_uniqcode()
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




#####################
def add_company(action):
    print("""                       ******************** 1. Add Company Menu *************************
                        ----------------- Nomor Option ------------------------
                        1 = Input to add new data  
                        2 = Back to Main Menu  
                      **********************************************************""")
    
    option = get_user_input("Masukkan nomor Option yang ingin anda jalankan: ", validate_display_option)
    
    if option == "1":
        code = get_valid_uniqcode()
        if code is None:
            return
        
        company = find_company_by_uniqcode(code)

        if action == "add" and company:
            print("Perusahaan sudah ada.")
            return

        data = {}
        fields = {
            "NameCompany": validate_name,
            "NoReg": validate_no_reg,
            "Product": validate_product,
            "Address": validate_address,
            "PostCode": validate_postcode,
            "Email": validate_email
        }

        for key, validation_func in fields.items():
            prompt = f"Masukkan {key} (max {len(key)} karakter): "
            value = get_user_input(prompt, validation_func)
            if value is None:
                return
            data[key] = value
        
        data["UniqCode"] = code

        if action == "add":
            directory_large_company.append(data)
        elif action == "update" and company:
            company.update(data)

        if confirm_action("Simpan data? 1. Ya 2. Tidak: "):
            print("Data berhasil disimpan.")
        else:
            print("Data tidak tersimpan.")
    
    elif option == "2":
        main_menu()  # Call the main menu function to go back







# def modify_or_delete_company(action):
#     code = get_valid_uniqcode()
#     if code is None:
#         return
#     company = find_company_by_uniqcode(code)

#     if action == "add" and company:
#         print("Perusahaan sudah ada.")
#         return

#     data = {}
#     fields = {
#         "NameCompany": validate_name,
#         "NoReg": validate_no_reg,
#         "Product": validate_product,
#         "Address": validate_address,
#         "PostCode": validate_postcode,
#         "Email": validate_email
#     }

#     for key, validation_func in fields.items():
#         prompt = f"Masukkan {key} (max {len(key)} karakter): "
#         value = get_user_input(prompt, validation_func)
#         if value is None:
#             return
#         data[key] = value
    
#     data["UniqCode"] = code

#     if action == "add":
#         directory_large_company.append(data)
#     elif action == "update" and company:
#         company.update(data)

#     if confirm_action("Simpan data? 1. Ya 2. Tidak: "):
#         print("Data berhasil disimpan.")
#     else:
#         print("Data tidak tersimpan.")

#     if action == "delete" and company:
#         display_company_details([company])
#         if confirm_action("Hapus data? 1. Ya 2. Tidak: "):
#             directory_large_company.remove(company)
#             print("Data berhasil dihapus.")

# Main program loop
header()
while True:
    main_menu()
    choice = get_user_input("Masukkan nomor Option yang ingin anda jalankan: ", validate_main_menu_option)
    if choice is None:
        continue

    if choice == "1":
        display_company()
    elif choice == "2":
        add_company()
    elif choice == "3":
        modify_or_delete_company("update")
    elif choice == "4":
        modify_or_delete_company("delete")
    elif choice == "5":
        print("Anda keluar dari program.")
        break












# from data_company import directory_large_company

# def header():
#     print("==========================================================================================================================================")
#     print("============================= Direktori Pencarian Perusahaan Industri di Kota Surabaya ==================================")
#     print("==========================================================================================================================================")

# def main_menu():
#     print("""                       ******************** Main Menu *************************
#                         ----------------- Nomor Option ------------------------
#                         1 = display company-----(Melihat semua data yang sudah tersedia)
#                         2 = add company --------(Membuat data baru yang belum tersedia)
#                         3 = update company------(Memperbarui data yang sudah tersedia)
#                         4 = delete company------(Menghapus data yang sudah tersedia)
#                         5 = exit ---------------(Meninggalkan Program)
#                       **********************************************************""")

# def find_company_by_uniqcode(code):
#     return next((item for item in directory_large_company if item['UniqCode'] == code), None)

# def display_company_details(companies=None):
#     print("  NameCompany        NoReg         Product                   Address              PostCode            Email                 UniqCode")
#     print("=" * 135)
#     for item in (companies or directory_large_company):
#         print(f"{item['NameCompany']:20} {item['NoReg']:10} {item['Product']:25} {item['Address']:25} {item['PostCode']:10} {item['Email']:30} {item['UniqCode']:10}")

# def confirm_action(prompt):
#     return input(prompt) == "1"

# def get_user_input(prompt, validation_func=None, max_attempts=3):
#     for _ in range(max_attempts):
#         value = input(prompt)
#         if validation_func is None or validation_func(value):
#             return value
#         print("Input tidak valid. Silakan coba lagi.")
#     print("Terlalu banyak percobaan tidak valid. Kembali ke menu utama.")
#     return None

# def validate_uniqcode(code):
#     return len(code) == 4 and find_company_by_uniqcode(code) is not None

# def validate_postcode(postcode):
#     return postcode.isdigit() and len(postcode) == 6

# def validate_length(value, max_length):
#     return len(value) <= max_length

# def modify_or_delete_company(action):
#     code = get_user_input("Masukkan Uniqcode perusahaan [4chara (xxxx), CAPITAL]: ", validate_uniqcode)
#     if code is None:
#         return

#     company = find_company_by_uniqcode(code)
    
#     if action == "add" and company:
#         print("Perusahaan sudah ada.")
#         return

#     if action in ["add", "update"]:
#         max_lengths = {
#             "NameCompany": 20,
#             "NoReg": 10,
#             "Product": 25,
#             "Address": 25,
#             "PostCode": 6,
#             "Email": 30
#         }
        
#         data = {}
#         for key, max_length in max_lengths.items():
#             prompt = f"Masukkan {key} (max {max_length} karakter): "
#             validation_func = validate_length if key != "PostCode" else validate_postcode
#             value = get_user_input(prompt, validation_func)
#             if value is None:
#                 return
#             data[key] = value
        
#         data["UniqCode"] = code

#         if action == "add":
#             directory_large_company.append(data)
#         elif action == "update" and company:
#             company.update(data)

#         if confirm_action("Simpan data? 1. Ya 2. Tidak: "):
#             print("Data berhasil disimpan.")
#         else:
#             print("Data tidak tersimpan.")

#     elif action == "delete":
#         if company:
#             display_company_details([company])
#             if confirm_action("Hapus data? 1. Ya 2. Tidak: "):
#                 directory_large_company.remove(company)
#                 print("Data berhasil dihapus.")
#             else:
#                 print("Penghapusan dibatalkan.")

#     display_company_details()

# # Main program loop
# header()
# while True:
#     main_menu()
#     action = get_user_input("Masukkan nomor Option yang ingin anda jalankan: ", lambda x: x in ["1", "2", "3", "4", "5"])
#     if action is None:
#         continue
    
#     if action == "1":
#         display_company_details()
#     elif action == "2":
#         modify_or_delete_company("add")
#     elif action == "3":
#         modify_or_delete_company("update")
#     elif action == "4":
#         modify_or_delete_company("delete")
#     elif action == "5":
#         print("Anda keluar dari program.")
#         break



# # # Main program loop
# # header()
# # while True:
# #     main_menu()
# #     action = input("Masukkan nomor Option yang ingin anda jalankan: ")
# #     if action == "1":
# #         show_all("NameCompany")
# #     elif action == "2":
# #         add_or_update_company("add")
# #     elif action == "3":
# #         add_or_update_company("update")
# #     elif action == "4":
# #         delete_company()
# #     elif action == "5":
# #         print("Anda keluar dari program.")
# #         break
# #     else:
# #         print("Pilihan tidak valid.")



# # from data_company import directory_large_company

# # def header():
# #     print("==========================================================================================================================================\n")
# #     print("============================= Direktori Pencarian Perusahaan Industri di Kota Surabaya ==================================\n")
# #     print("==========================================================================================================================================\n")

# # def main_menu():
# #     print("""                       ******************** Main Menu *************************
# #                         ----------------- Nomor Option ------------------------
# #                         1 = display company-----(Melihat semua data yang sudah tersedia)
# #                         2 = add company --------(Membuat data baru yang belum tersedia)
# #                         3 = update company------(Memperbarui data yang sudah tersedia)
# #                         4 = delete company------(Menghapus data yang sudah tersedia)
# #                         5 = exit ---------------(Meninggalkan Program)
# #                       **********************************************************
# #             """)

# # def find_company_by_uniqcode(code):
# #     return next((item for item in directory_large_company if item['UniqCode'] == code), None)

# # def display_company_details(companies=None):
# #     print("  NameCompany        NoReg         Product                   Address              PostCode            Email                 UniqCode")
# #     print("=" * 135)
# #     for item in (companies or directory_large_company):
# #         print(f"{item['NameCompany']:20} {item['NoReg']:10} {item['Product']:25} {item['Address']:25} {item['PostCode']:10} {item['Email']:30} {item['UniqCode']:10}")

# # def confirm_action(prompt):
# #     return input(prompt) == "1"

# # def show_all(field):
# #     print(f"  {field}")
# #     print("=" * 25)
# #     for item in directory_large_company:
# #         print(f"{item[field]:25}")
# #     if confirm_action(f"Apakah {field.lower()} yang Anda cari sudah tersedia? 1. Ya 2. Tidak: "):
# #         if field == "NameCompany":
# #             display_company_details()
# #         else:
# #             code = input("Masukkan Uniqcode perusahaan [4chara, capital]: ")
# #             company = find_company_by_uniqcode(code)
# #             if company:
# #                 display_company_details([company])
# #             else:
# #                 print("Data tidak ditemukan.")
# #     else:
# #         print("Data tidak ditemukan.")

# # def add_or_update_company(action):
# #     code = input("Masukkan Uniqcode perusahaan [4chara, capital]: ")
# #     if action == "add" and find_company_by_uniqcode(code):
# #         print("Perusahaan sudah ada.")
# #         return
# #     data = {key: input(f"Masukkan {key}: ") for key in ["NameCompany", "NoReg", "Product", "Address", "PostCode", "Email"]}
# #     data["UniqCode"] = code

# #     if action == "add":
# #         directory_large_company.append(data)
# #     else:
# #         company = find_company_by_uniqcode(code)
# #         if company:
# #             company.update(data)

# #     if confirm_action("Simpan data? 1. Ya 2. Tidak: "):
# #         print("Data berhasil disimpan.")
# #     else:
# #         print("Data tidak tersimpan.")

# # def delete_company():
# #     code = input("Masukkan Uniqcode perusahaan [4chara, capital]: ")
# #     company = find_company_by_uniqcode(code)
# #     if company:
# #         display_company_details([company])
# #         if confirm_action("Hapus data? 1. Ya 2. Tidak: "):
# #             directory_large_company.remove(company)
# #             print("Data berhasil dihapus.")
# #     else:
# #         print("Data tidak ditemukan.")

# # # Main program loop
# # header()
# # while True:
# #     main_menu()
# #     action = input("Masukkan nomor Option yang ingin anda jalankan: ")
# #     if action == "1":
# #         show_all("NameCompany")
# #     elif action == "2":
# #         add_or_update_company("add")
# #     elif action == "3":
# #         add_or_update_company("update")
# #     elif action == "4":
# #         delete_company()
# #     elif action == "5":
# #         print("Anda keluar dari program.")
# #         break
# #     else:
# #         print("Pilihan tidak valid.")