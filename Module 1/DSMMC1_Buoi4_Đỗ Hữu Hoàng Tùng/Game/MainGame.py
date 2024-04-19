import random
from .Account import *
from datetime import datetime

def quay_so():
    danh_sach_giai = {}

    ten_giai = ["GIẢI NHẤT", "GIẢI NHÌ", "GIẢI BA", "GIẢI TƯ", "GIẢI NĂM", "GIẢI SÁU", "GIẢI BẢY"]

    for giai in ten_giai:
        so = ""
        for i in range(5):
            so += str(random.randint(0, 9)) 
        danh_sach_giai[giai] = so

    return danh_sach_giai

def in_danh_sach_giai(danh_sach_giai):
    print('-' * 20)
    print("---DANH SÁCH GIẢI---")
    for giai, so in danh_sach_giai.items():
        print(f"{giai}: {so}")
    print('-' * 20)

def nhap_so_lo():
    while True:
        so_lo_input = input("Nhập các số lô bạn muốn chơi, cách nhau bằng dấu phẩy: ")
        danh_sach_so_lo = so_lo_input.split(",")

        so_lo_hop_le = True

        for so_lo in danh_sach_so_lo:
            if len(so_lo) != 2 or not so_lo.isdigit():
                print("Số lô nhập không hợp lệ. Vui lòng nhập lại.")
                so_lo_hop_le = False
                break

        if so_lo_hop_le:
            return danh_sach_so_lo
def nhap_tien_cuoc(username,so_lo):
    tong_tien = int(lay_thong_tin_tai_khoan(username)[2])
    while True:
        tien_cuoc = input("Nhập tiền cược mà bạn muốn cược (tiền cược < tổng tiền bạn có): ")
        if tien_cuoc.isdigit() and int(tien_cuoc) * so_lo < tong_tien:
            return int(tien_cuoc)
        else:
            print("Nhập sai định dạng hoặc quá tổng tiền. Nhập lại")


def cap_nhat_tien_choi_lo(username, tong_tien):
    try:
        du_lieu_tai_khoan = doc_file(PATH_DATA_TAI_KHOAN, "r")
        if du_lieu_tai_khoan:
            for i, tai_khoan in enumerate(du_lieu_tai_khoan):
                if tai_khoan[0] == username:
                    du_lieu_tai_khoan[i][2] = str(tong_tien)  # Cập nhật số tiền
                    ghi_file([','.join(tai_khoan) + '\n' for tai_khoan in du_lieu_tai_khoan], PATH_DATA_TAI_KHOAN, "w")
                    return
    except Exception as e:
        print(f"Có lỗi xảy ra khi cập nhật thông tin tài khoản: {e}")


def luu_thong_tin_choi_lo(username, danh_sach_so_lo, tien_cuoc, danh_sach_giai,  tien_thang, tien_thua):
    try:
        thoi_gian_choi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        thong_tin = f"{thoi_gian_choi},{username},{','.join(danh_sach_so_lo)},{tien_cuoc}," \
                    f"{','.join(danh_sach_giai.values())},{tien_thang},{tien_thua}\n"

        ghi_file(thong_tin, PATH_DATA_CHOI_LO, "a")
        print("Thông tin về lần chơi lô đã được lưu.")

        # Cập nhật số tiền thắng/thua vào tài khoản

    except Exception as e:
        print(f"Có lỗi xảy ra khi lưu thông tin: {e}")

def game_quay_so(username, danh_sach_so_lo, tien_cuoc):
    tong_tien = int(lay_thong_tin_tai_khoan(username)[2])

    danh_sach_giai = quay_so()

    in_danh_sach_giai(danh_sach_giai)
    dem_so_lo_trung = 0
    so_lo_trung = []  

    print("Các số lô bạn chơi là:", danh_sach_so_lo)
    for giai, so_giai in danh_sach_giai.items():
        for so_lo in danh_sach_so_lo:
            if so_lo == so_giai[-2:]:
                dem_so_lo_trung += 1
                so_lo_trung.append(so_lo)
    tien_thang = 0  
    tien_thua = 0   

    if dem_so_lo_trung > 0:
        tien_thang = tien_cuoc * dem_so_lo_trung * 70
        tien_thua = tien_cuoc * (len(danh_sach_so_lo) - dem_so_lo_trung)

        tong_tien += tien_thang - tien_thua

        print(f"Bạn đã trúng {dem_so_lo_trung} nháy!")
        print("Các số lô trúng:", ", ".join(so_lo_trung))
        print(f"Số tiền bạn trúng là {tien_thang}")
        print(f"Số tiền bạn thua là {tien_thua}")
        print(f"Tổng tiền bạn có là {tong_tien}")
    else:
        tien_thua = tien_cuoc * len(danh_sach_so_lo)
        tong_tien -= tien_thua

        print("Bạn đã thua lô!")
        print(f"Số tiền bạn thua là {tien_thua}")
        print(f"Tổng tiền bạn còn là {tong_tien}")

    luu_thong_tin_choi_lo(username, danh_sach_so_lo, tien_cuoc, danh_sach_giai, tien_thang, tien_thua)
    cap_nhat_tien_choi_lo(username, tong_tien)