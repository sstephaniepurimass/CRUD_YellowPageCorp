# ===================================
# [Direktori Pencarian Perusahaan Industri Besar dan Sedang di Kota Surabaya]
# ===================================
# Developed by. Stephanie Purimas
# JCDS - 0412


# /************************************/  

# Welcoming Program
def create():
    """To add new data"""
    print("""                       ******************** 1. Create Data Menu *************************\n
                        ----------------- Nomor Option ------------------------\n
                        1 = Input to add new data  
                        2 = Back to Main Menu  
        
                      **********************************************************\n
            """)

    input_user = input("Masukkan nomor option yang ingin anda jalankan:  ") 

    if input_user == "1":
        # Assume the unique code is pre-defined or fetched from existing data
        uniq_code = input("Masukkan kode unik perusahaan (tidak bisa dirubah): ").strip().lower()

        print("Silakan masukkan detail perusahaan yang ingin ditambahkan:")
        name_company = input("Masukkan nama perusahaan: ")
        no_reg = input("Masukkan nomor registrasi: ")
        product = input("Masukkan produk: ")
        address = input("Masukkan alamat: ")
        post_code = input("Masukkan kode pos: ")
        email = input("Masukkan email: ")

        # Create a new company data dictionary
        new_company = {
            "NameCompany": name_company,
            "NoReg": no_reg,
            "Product": product,
            "Address": address,
            "PostCode": post_code,
            "Email": email,
            "UniqCode": uniq_code  # UniqCode is not changed
        }

        # Here you would typically add this new_company to your data structure
        # For example, appending it to directory_large_company:
        directory_large_company.append(new_company)
        print("Data berhasil ditambahkan.")

        input("Tekan Enter untuk kembali ke Menu Create")  # kembali ke create menu
        create()  # tampilan menu create

    elif input_user == "2":
        return  # kembali ke Main Menu
    else:
        print("Nomor option yang anda masukkan tidak tersedia! Silahkan input 1/2")
