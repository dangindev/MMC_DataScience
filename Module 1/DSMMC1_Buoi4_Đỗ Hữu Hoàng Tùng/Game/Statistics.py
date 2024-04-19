from .File import *
from .Path import *

def thong_ke_user(username):
    try:
        du_lieu_choi_lo = doc_file(PATH_DATA_CHOI_LO, "r")
        so_lan_choi = 0
        tong_tien_thang = 0
        tong_tien_thua = 0
        so_lan_thang = 0
        so_lan_thua = 0

        for choi_lo in du_lieu_choi_lo:
            if choi_lo[1] == username:
                so_lan_choi += 1
                tong_tien_thang += int(choi_lo[-2])
                tong_tien_thua += int(choi_lo[-1])
                if int(choi_lo[-2]) >  0:
                    so_lan_thang += 1
                else:
                    so_lan_thua += 1
        ti_le_thang = round(so_lan_thang / so_lan_thua, 2) if so_lan_thua > 0 else 0

        # In kết quả
        print("===THỐNG KÊ CHƠI LÔ USER: "+ username+"===")
        print("Số lần chơi lô:", so_lan_choi)
        print("Tổng tiền chơi lô thắng:", tong_tien_thang)
        print("Tổng tiền chơi lô thua:", tong_tien_thua)
        print("Tỉ lệ chơi lô thắng:", ti_le_thang)

    except Exception as e:
        print(f"Có lỗi xảy ra khi thực hiện thống kê: {e}")


def thong_ke_admin():
    try:
        # Đọc dữ liệu từ file choilo.txt
        du_lieu_choi_lo = doc_file(PATH_DATA_CHOI_LO, "r")
        so_luong_tai_khoan = len(doc_file(PATH_DATA_TAI_KHOAN, "r"))
        tong_so_lan_choi_lo = len(du_lieu_choi_lo)
        tong_tien_thang = sum(int(choi_lo[-2]) for choi_lo in du_lieu_choi_lo)
        tong_tien_thua = sum(int(choi_lo[-1]) for choi_lo in du_lieu_choi_lo)
        so_lan_thang = sum(1 for choi_lo in du_lieu_choi_lo if int(choi_lo[-2]) > 0)
        so_lan_thua = tong_so_lan_choi_lo - so_lan_thang

        # Tính tỷ lệ thắng/thua
        ti_le_thang_thua = round(so_lan_thang / so_lan_thua, 2) if so_lan_thua > 0 else 0

        # In kết quả thống kê
        print("===THỐNG KÊ TỔNG HỢP===")
        print("Số lượng tài khoản:", so_luong_tai_khoan)
        print("Tổng số lượt chơi lô:", tong_so_lan_choi_lo)
        print("Tổng tiền chơi lô thắng:", tong_tien_thang)
        print("Tổng tiền chơi lô thua:", tong_tien_thua)
        print("Tỉ lệ thắng/thua:", ti_le_thang_thua)

    except Exception as e:
        print(f"Có lỗi xảy ra khi thực hiện thống kê tổng hợp: {e}")