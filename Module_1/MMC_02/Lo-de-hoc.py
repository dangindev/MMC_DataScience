import random

def quay_so(): 
    danh_sach_giai = [random.randint(10, 99) for _ in range(7)]
    return danh_sach_giai

def in_danh_sach_giai(danh_sach_giai): 
    for i, giai in enumerate(danh_sach_giai, start=1):
        print(f'Giải {i} là {giai}')

def nhap_so_lo(): 
    while True: 
        try: 
            numb = int(input('Nhập số lô: '))
            if 10 < numb < 99:
                print('Xác nhận số lô thành công!') 
                return numb 
            else: 
                print('Vui lòng nhập số trong khoảng giá trị!')
        except: 
            print('Vui lòng chỉ nhập số!')

def nhap_tien_cuoc(tong_tien): 
    while True: 
        try: 
            numb = int(input('Nhập tiền cược: '))
            if numb < tong_tien: 
                print('Xác nhận cược thành công!')
                return numb 
            else: 
                print('Vui lòng cược ít hơn số tiền đang có!')
        except: 
            print('Vui lòng chỉ nhập số!')
            

def hien_thi(tong_tien): 
    print('Chào mừng bạn tới với game Lô Đề học')
    print(f'Tài khoản của bạn hiện có: {tong_tien}')
    print('Hãy lựa chọn:')
    print('1. Chơi game')
    print('2. Nạp tiền')
    print('3. Thoát')

def lua_chon(): 
    while True: 
        try: 
            numb = int(input('Nhập lựa chọn của bạn: '))
            if numb in [1,2,3]: 
                return numb 
            else: 
                print('Vui lòng nhập đúng các lựa chọn')
        except: 
            print('Vui lòng chỉ nhập số!')

def trung_giai(so_lo, danh_sach_giai): 
    return danh_sach_giai.count(so_lo)

def cap_nhat_tien(tong_tien, so_lan_trung, tien_cuoc): 
    return tong_tien - tien_cuoc + so_lan_trung * tien_cuoc * 70
    

def nap_tien(tong_tien):
    while True: 
        try: 
            numb = int(input('Nhập tiền muốn nạp: '))
            tong_tien += numb 
            return tong_tien
        except: 
            print('Vui lòng chỉ nhập số nguyên!')

def thong_bao(so_lan_trung): 
    if so_lan_trung == 0: 
        print('Rất tiếc, bạn không trúng giải nào cả!')
    else: 
        print(f'Xin chúc mừng, bạn đã trúng {so_lan_trung} giải!')

def main(): 
    tong_tien = 100
    hien_thi(tong_tien)
    while True:
        gia_tri_lua_chon = lua_chon()
        if gia_tri_lua_chon == 1: 
            so_lo = nhap_so_lo()
            tien_cuoc = nhap_tien_cuoc(tong_tien)
            danh_sach_giai = quay_so()
            in_danh_sach_giai(danh_sach_giai)
            so_lan_trung = trung_giai(so_lo, danh_sach_giai)
            tong_tien = cap_nhat_tien(tong_tien, so_lan_trung, tien_cuoc)
            thong_bao(so_lan_trung)
            hien_thi(tong_tien)
        elif gia_tri_lua_chon == 2: 
            tong_tien = nap_tien(tong_tien)
            hien_thi(tong_tien)
        elif gia_tri_lua_chon == 3:
            print('Hẹn gặp lại bạn lần sau!')
            break

main()