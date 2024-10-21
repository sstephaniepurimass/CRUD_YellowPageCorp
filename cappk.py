from data_company import directory_large_company

company_counter = len(directory_large_company)

def header():
    print("=" * 135)
    print("============================= Direktori Pencarian Perusahaan Industri di Kota Surabaya ==============================")
    print("=" * 135)

def main_menu():
    print(f"Jumlah Perusahaan Terdaftar: {company_counter}")
    print("""\
                       ******************** Main Menu *************************
                        1 = Display company
                        2 = Add company
                        3 = Update company
                        4 = Delete company
                        5 = Exit
                      **********************************************************
            """)

def display_companies(companies):
    print("  NameCompany        NoReg         Product                   Address              PostCode            Email                 UniqCode")
    print("=" * 135)
    for company in companies:
        print(f"{company['NameCompany']:20} {company['NoReg']:10} {company['Product']:25} {company['Address']:25} {company['PostCode']:10} {company['Email']:30} {company['UniqCode']:10}")

def display_company(option):
    if option == "A":
        print("  NameCompany\n" + "=" * 20)
        for company in directory_large_company:
            print(f"{company['NameCompany']:20}")
        if input("Apakah nama perusahaan yang Anda cari telah tersedia? A. Sudah B. Belum: ").upper() == "A":
            display_companies(directory_large_company)

    elif option == "B":
        print("  Product\n" + "=" * 25)
        for company in directory_large_company:
            print(f"{company['Product']:25}")
        if input("Apakah produk yang Anda cari telah tersedia: A. Sudah B. Belum? ").upper() == "A":
            input_uniq_code = input("Masukkan Uniqcode perusahaan [4chara, capital]: ")
            company = next((item for item in directory_large_company if item['UniqCode'] == input_uniq_code), None)
            if company:
                display_companies([company])

def validate_uniqcode(code):
    return len(code) == 4 and all(item['UniqCode'] != code for item in directory_large_company)

def get_company_input(existing_data=None):
    print("Update Data" if existing_data else "Add Data")
    return {key: input(f"Masukkan {key}: ") for key in ["UniqCode", "NameCompany", "NoReg", "Product", "Address", "PostCode", "Email"]}

def manage_company(action):
    input_user = input(f"""                       ******************** 1. {action} Company Menu *************************
                            ----------------- Nomor Option ------------------------
                            1 = {'Input to add new data' if action == 'Add' else 'Update Data' if action == 'Update' else 'Delete Data'} 
                            2 = Back to Main Menu  
                          **********************************************************
            Masukkan nomor Option: """)

    if input_user == "1":
        input_uniq_code = input("Masukkan Uniqcode perusahaan [4chara, capital]: ")
        directory_dict = {item['UniqCode']: item for item in directory_large_company}

        if action == "Add":
            if not validate_uniqcode(input_uniq_code):
                print("Uniqcode tidak valid atau perusahaan sudah ada.")
                return
            directory_large_company.append(get_company_input())
            global company_counter
            company_counter += 1
            print("Data berhasil disimpan.")

        elif action == "Update":
            if input_uniq_code in directory_dict:
                display_companies([directory_dict[input_uniq_code]])
                new_data = get_company_input(existing_data=directory_dict[input_uniq_code])
                for key, value in new_data.items():
                    if value: directory_dict[input_uniq_code][key] = value
                print("Data berhasil diupdate.")
            else:
                print("Data tidak ditemukan.")

        elif action == "Delete":
            if input_uniq_code in directory_dict:
                directory_large_company.remove(directory_dict[input_uniq_code])
                global company_counter
                company_counter -= 1
                print("Data berhasil dihapus.")
            else:
                print("Data tidak ditemukan.")

# Main program loop
header()
while True:
    main_menu()
    option = input("Masukkan nomor Option yang ingin anda jalankan: ")
    
    if option == "1":
        display_company(input("Masukkan nomor Option untuk Display (A/B): ").upper())
    elif option in ["2", "3", "4"]:
        manage_company(["Add", "Update", "Delete"][int(option) - 2])
    elif option == "5":
        print("Anda keluar dari program.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
