from .File import *
from .Path import *
from IPython.display import clear_output



def tao_tai_khoan(username, password, tong_tien):
    user_info = f"{username},{password},{tong_tien}\n"
    ghi_file([user_info], PATH_DATA_TAI_KHOAN, "a")
    print(f"Tạo tài khoản {username} thành công")

def xoa_tai_khoan(username):
    lst_taikhoan = doc_file(PATH_DATA_TAI_KHOAN, "r")
    for tai_khoan_info in lst_taikhoan:
        if tai_khoan_info[0] == username:
            lst_taikhoan.remove(tai_khoan_info)
            ghi_file([','.join(tai_khoan) + '\n' for tai_khoan in lst_taikhoan], PATH_DATA_TAI_KHOAN, "w")
            print ("Xóa tài khoản thành công")


def kiem_tra_admin(username):
    if username == "admin":
        return 1
    else:
        return 0

def kiem_tra_tai_khoan(username, password):
    global dang_nhap_status, user
    # Đọc dữ liệu từ file tài khoản
    lst_taikhoan = doc_file(PATH_DATA_TAI_KHOAN, "r")
    if lst_taikhoan is None:
        return

    for tai_khoan in lst_taikhoan:
        if tai_khoan[0] == username and tai_khoan[1] == password:
            return kiem_tra_admin(username)

def kiem_tra_ton_tai_tai_khoan(username):
    # Đọc dữ liệu từ file tài khoản
    lst_taikhoan = doc_file(PATH_DATA_TAI_KHOAN, "r")
    if lst_taikhoan is None:
        return False

    # Kiểm tra xem tài khoản đã tồn tại chưa
    for tai_khoan in lst_taikhoan:
        if tai_khoan[0] == username:
            return True

    return False

def lay_thong_tin_tai_khoan(username):
    try:
        du_lieu_tai_khoan = doc_file(PATH_DATA_TAI_KHOAN, "r")
        if du_lieu_tai_khoan:
            for tai_khoan in du_lieu_tai_khoan:
                if tai_khoan[0] == username:
                    return tai_khoan
        else:
            return None
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
        return None


def check_dang_nhap(username, password):
    if kiem_tra_tai_khoan(username, password) in (0,1):
        return True
    else:
        return False

def doi_mat_khau(username, password_cu, password_moi):
    lst_taikhoan = doc_file(PATH_DATA_TAI_KHOAN, "r")

    for tai_khoan_info in lst_taikhoan:
        if tai_khoan_info[0] == username and tai_khoan_info[1] == password_cu:
            tai_khoan_info[1] = password_moi
            ghi_file([','.join(tai_khoan) + '\n' for tai_khoan in lst_taikhoan], PATH_DATA_TAI_KHOAN, "w")
            print("Đổi mật khẩu thành công.")
            return

    print("Không tìm thấy tài khoản hoặc mật khẩu cũ không đúng.")
    return

def nap_tien(username, so_tien_nap):
  
    lst_taikhoan = doc_file(PATH_DATA_TAI_KHOAN, "r")

  
    for tai_khoan_info in lst_taikhoan:
        if tai_khoan_info[0] == username:
        
            tai_khoan_info[2] = str(int(tai_khoan_info[2]) + so_tien_nap)
        
            ghi_file([','.join(tai_khoan) + '\n' for tai_khoan in lst_taikhoan], PATH_DATA_TAI_KHOAN, "w")
            print(f"Đã nạp {so_tien_nap} vào tài khoản {username}.")
            return

    print("Không tìm thấy tài khoản.")
    return