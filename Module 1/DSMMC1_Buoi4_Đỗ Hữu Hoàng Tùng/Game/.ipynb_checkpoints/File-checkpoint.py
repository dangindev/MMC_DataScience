def ghi_file(data, ten_file, mode):
    try:
        with open(ten_file, mode) as file:
            for line in data:
                file.write(line)
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")


def doc_file(duong_dan, mode):
    try:
        with open(duong_dan, mode) as file:
            du_lieu = [line.strip().split(',') for line in file.readlines()]
        return du_lieu
    except Exception as e:
        print(f"Có lỗi xảy ra khi đọc file: {e}")
        return None
