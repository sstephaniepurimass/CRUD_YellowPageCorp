from data_company import directory_large_company

def header():
    print("==========================================================================================================================================\n"
          "============================= Direktori Pencarian Perusahaan Industri di Kota Surabaya ==================================\n"
          "==========================================================================================================================================\n")
# Menampilkan header untuk antarmuka pengguna.


def user_input()

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
        return 