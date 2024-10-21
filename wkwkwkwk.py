from data_company import directory_large_company

# Inisialisasi jumlah total perusahaan
total_count = len(directory_large_company)

def header():
    print("==========================================================================================================================================\n"
          "============================= Direktori Pencarian Perusahaan Industri di Kota Surabaya ==================================\n"
          "==========================================================================================================================================\n")
# Menampilkan header untuk antarmuka pengguna.

def main_menu():
    print(""" 
                       ******************** Main Menu *************************
                        ----------------- Nomor Option ------------------------
                        1 = display company-----(Melihat semua data yang sudah tersedia)
                        2 = add company --------(Membuat data baru yang belum tersedia)
                        3 = update company------(Memperbarui data yang sudah tersedia)
                        4 = delete company------(Menghapus data yang sudah tersedia)
                        5 = exit ---------------(Meninggalkan Program)
                      **********************************************************
            """)
# Menampilkan menu utama dengan opsi yang tersedia.

def user_input(text, valid_options=None, max_length=None, is_unique_code=False):
    attempts = 0
    while attempts < 3:
        input_value = input(text)
        
        # Validasi panjang input
        if max_length and len(input_value) > max_length:
            print(f"Input tidak boleh lebih dari {max_length} karakter.")
            attempts += 1
            continue
        
        # Validasi format kode unik
        if is_unique_code and (len(input_value) != 4 or not input_value.isalnum() or not input_value.isupper()):
            print("Kode unik harus 4 karakter, kombinasi huruf kapital dan angka.")
            attempts += 1
            continue

        # Validasi opsi
        if valid_options and input_value not in valid_options:
            print("Input tidak valid. Silakan masukkan salah satu dari: ", ', '.join(valid_options))
            attempts += 1
            continue

        return input_value
    
    print("Terlalu banyak percobaan yang salah. Kembali ke menu utama.")
    return None  # Menunjukkan kembali ke menu utama
# Mengambil input dari pengguna dengan beberapa validasi, termasuk panjang input dan format kode unik.

def display_data(header=True):
    if header:
        print("  NameCompany        NoReg         Product                   Address              PostCode            Email                 UniqCode")
        print("=" * 135)

    for item in directory_large_company:
        print(f"{item['NameCompany']:20} {item['NoReg']:10} {item['Product']:25} {item['Address']:25} {item['PostCode']:10} {item['Email']:30} {item['UniqCode']:10}")
# Menampilkan data perusahaan dalam format tabel.

def display_company():
    print(""" 
                     ******************** 1. Display Company Menu **********************
                        ----------------- Nomor Option ------------------------
                        1 = Shown All Name Company 
                        2 = Shown All Product Company 
                        3 = Back to Main Menu  
                    ****************************************************************
            """)

    option = user_input("Masukkan nomor option yang ingin anda jalankan: ", ["1", "2", "3"])  
    if option is None:
        return  # Kembali ke menu utama
    if option == "1":
        display_data()
        if user_input("Apakah nama perusahaan yang anda cari tersedia? (1.Ya / 2.Tidak): ", ["1", "2"]) == "1":
            display_data()
    elif option == "2":
        company_name = input("Masukkan nama perusahaan yang ingin dicari: ")
        found = False
        display_data(header=False)
        for item in directory_large_company:
            if company_name.lower() in item['NameCompany'].lower():
                print(f"{item['NameCompany']:20} {item['NoReg']:10} {item['Product']:25} {item['Address']:25} {item['PostCode']:10} {item['Email']:30} {item['UniqCode']:10}")
                found = True
        if not found:
            print("Perusahaan tidak ditemukan.")
# Menampilkan submenu untuk memilih bagaimana ingin melihat perusahaan dan mencari perusahaan berdasarkan nama.

def manage_company(action):
    uniq_code = user_input(f"Masukkan kode unik perusahaan yang ingin {action}: ", max_length=4, is_unique_code=True)
    if uniq_code is None:
        return  # Kembali ke menu utama jika input tidak valid

    company = next((item for item in directory_large_company if item['UniqCode'].lower() == uniq_code), None)

    if action == "create":
        if company:
            print("Kode unik sudah ada. Silakan gunakan kode unik lain.")
            return False

        new_company = {
            "NameCompany": user_input("Masukkan nama perusahaan: ", max_length=20),
            "NoReg": user_input("Masukkan nomor registrasi: ", max_length=10),
            "Product": user_input("Masukkan produk: ", max_length=25),
            "Address": user_input("Masukkan alamat: ", max_length=25),
            "PostCode": user_input("Masukkan kode pos: ", max_length=5),
            "Email": user_input("Masukkan email: ", max_length=30),
            "UniqCode": uniq_code
        }
        directory_large_company.append(new_company)
        print("Data berhasil ditambahkan.")
        return True

    elif action == "update":
        if company:
            print("Data yang tersedia:")
            for key, value in company.items():
                print(f"  {key}: {value}")

            if user_input(f"Apakah anda ingin melanjutkan update data? (1.Ya / 2.Tidak): ", ["1", "2"]) == "1":
                for key in company.keys():
                    new_value = input(f"Masukkan {key} baru (tekan Enter untuk tetap): ")
                    if new_value:
                        if key == "NameCompany" and len(new_value) <= 20:
                            company[key] = new_value
                        elif key == "NoReg" and len(new_value) <= 10:
                            company[key] = new_value
                        elif key == "Product" and len(new_value) <= 25:
                            company[key] = new_value
                        elif key == "Address" and len(new_value) <= 25:
                            company[key] = new_value
                        elif key == "PostCode" and len(new_value) <= 5 and new_value.isdigit():
                            company[key] = new_value
                        elif key == "Email" and len(new_value) <= 30:
                            company[key] = new_value
                        else:
                            print(f"Input untuk {key} tidak valid.")
                print("Data berhasil diupdate.")
                return True
        else:
            print("Data tidak ditemukan dengan kode unik tersebut.")

    elif action == "delete":
        if company:
            print("Data yang akan dihapus:")
            for key, value in company.items():
                print(f"  {key}: {value}")

            if user_input("Apakah anda ingin menghapus data ini? (1.Ya / 2.Tidak): ", ["1", "2"]) == "1":
                directory_large_company.remove(company)
                print("Data berhasil dihapus.")
                return True
        else:
            print("Data tidak ditemukan dengan kode unik tersebut.")
    
    return False
# Mengelola data perusahaan berdasarkan aksi yang dipilih: membuat, memperbarui, atau menghapus data perusahaan.

# Loop utama program
header()
while True:
    main_menu()
    option = user_input("Masukkan nomor option yang ingin anda jalankan: ", ["1", "2", "3", "4", "5"])
    
    if option is None:
        continue  # Kembali ke menu utama jika input tidak valid
    if option == "1":
        display_company()  
    elif option == "2":
        manage_company("create")
        display_data()  # Cetak data setelah penambahan
    elif option == "3":
        manage_company("update")
        display_data()  # Cetak data setelah pembaruan
    elif option == "4":
        manage_company("delete")
        display_data()  # Cetak data setelah penghapusan
    elif option == "5":
        print("Anda akan keluar dari program.")
        break
# Memanggil fungsi header, menampilkan menu utama, dan menjalankan aksi yang dipilih pengguna hingga pengguna memutuskan untuk keluar.

