from datetime import datetime
import re

class Sach:
    def __init__(self, ma_sach, tieu_de, tac_gia, the_loai, so_ban_sao, ngay_xuat_ban=None):
        self.ma_sach = ma_sach
        self.tieu_de = tieu_de
        self.tac_gia = tac_gia
        self.the_loai = the_loai
        self.so_ban_sao = so_ban_sao
        if ngay_xuat_ban is None:
            self.ngay_xuat_ban = datetime.now()
        else:
            self.ngay_xuat_ban = ngay_xuat_ban

    def hien_thi_thong_tin(self):
        print(f"Mã sách: {self.ma_sach}")
        print(f"Tiêu đề: {self.tieu_de}")
        print(f"Tác giả: {self.tac_gia}")
        print(f"Thể loại: {self.the_loai}")
        print(f"Số bản sao: {self.so_ban_sao}")
        print(f"Ngày xuất bản: {self.ngay_xuat_ban.strftime('%Y-%m-%d')}")


class QuanLySach:
    def __init__(self):
        self.ds_sach = []

    def them_sach(self, sach):
        if self.kiem_tra_trung_lap(sach.ma_sach):
            print("Mã sách đã tồn tại! Vui lòng nhập mã khác.")
            return
        self.ds_sach.append(sach)
        self.luu_du_lieu_vao_file()
        print(f"Đã thêm sách: {sach.tieu_de}")

    def tim_kiem_sach(self, ma_sach=None, tieu_de=None):
        ket_qua = []
        for sach in self.ds_sach:
            if (ma_sach and sach.ma_sach == ma_sach) or (tieu_de and sach.tieu_de.lower() == tieu_de.lower()):
                ket_qua.append(sach)
        return ket_qua

    def hien_thi_danh_sach_sach(self):
        if not self.ds_sach:
            print("Danh sách sách trống.")
        else:
            for sach in self.ds_sach:
                sach.hien_thi_thong_tin()

    def cap_nhat_sach(self, ma_sach, tieu_de=None, tac_gia=None, the_loai=None, so_ban_sao=None):
        sach = self.tim_kiem_sach(ma_sach=ma_sach)
        if not sach:
            print("Không tìm thấy sách với mã:", ma_sach)
            return
        sach = sach[0]
        if tieu_de:
            sach.tieu_de = tieu_de
        if tac_gia:
            sach.tac_gia = tac_gia
        if the_loai:
            sach.the_loai = the_loai
        if so_ban_sao is not None:
            sach.so_ban_sao = so_ban_sao
        self.luu_du_lieu_vao_file()
        print(f"Đã cập nhật thông tin sách: {sach.tieu_de}")

    def xoa_sach(self, ma_sach):
        sach = self.tim_kiem_sach(ma_sach=ma_sach)
        if sach:
            self.ds_sach.remove(sach[0])
            self.luu_du_lieu_vao_file()
            print(f"Đã xóa sách có mã: {ma_sach}")
        else:
            print(f"Không tìm thấy sách với mã: {ma_sach}")

    def luu_du_lieu_vao_file(self, ten_file='sach.txt'):
        with open(ten_file, 'w', encoding='utf-8') as f:
            for sach in self.ds_sach:
                f.write(f"{sach.ma_sach},{sach.tieu_de},{sach.tac_gia},{sach.the_loai},{sach.so_ban_sao},{sach.ngay_xuat_ban.strftime('%Y-%m-%d')}\n")
        print(f"Dữ liệu đã được lưu vào file {ten_file}")

    def tai_lai_du_lieu(self, ten_file='sach.txt'):
        try:
            with open(ten_file, 'r', encoding='utf-8') as f:
                self.ds_sach.clear()
                for line in f:
                    ma_sach, tieu_de, tac_gia, the_loai, so_ban_sao, ngay_xuat_ban = line.strip().split(',')
                    ngay_xuat_ban = datetime.strptime(ngay_xuat_ban, '%Y-%m-%d')
                    sach = Sach(ma_sach, tieu_de, tac_gia, the_loai, int(so_ban_sao), ngay_xuat_ban)
                    self.ds_sach.append(sach)
            print("Dữ liệu đã được tải lại từ file.")
        except FileNotFoundError:
            print("Không tìm thấy file để tải dữ liệu.")

    def tong_so_sach(self):
        print(f"Tổng số sách hiện có: {len(self.ds_sach)}")

    def tim_kiem_theo_regex(self, pattern):
        regex = re.compile(pattern)
        ket_qua = [sach for sach in self.ds_sach if regex.search(sach.tieu_de) or regex.search(sach.tac_gia)]
        if ket_qua:
            for sach in ket_qua:
                sach.hien_thi_thong_tin()
        else:
            print("Không tìm thấy kết quả phù hợp.")

    def kiem_tra_trung_lap(self, ma_sach):
        return any(sach.ma_sach == ma_sach for sach in self.ds_sach)

    
    def thong_ke_theo_the_loai(self):
        thong_ke = {}
        for sach in self.ds_sach:
            thong_ke[sach.the_loai] = thong_ke.get(sach.the_loai, 0) + 1
        print("Thống kê theo thể loại:")
        for the_loai, so_luong in thong_ke.items():
            print(f"{the_loai}: {so_luong} sách")

    def sap_xep_theo_ngay_xuat_ban(self):
        sorted_books = sorted(self.ds_sach, key=lambda x: x.ngay_xuat_ban)
        print("Sách theo thứ tự ngày xuất bản:")
        for sach in sorted_books:
            sach.hien_thi_thong_tin()

    def dem_sach_theo_tac_gia(self):
        tac_gia_count = {}
        for sach in self.ds_sach:
            tac_gia_count[sach.tac_gia] = tac_gia_count.get(sach.tac_gia, 0) + 1
        print("Số lượng sách theo tác giả:")
        for tac_gia, so_luong in tac_gia_count.items():
            print(f"{tac_gia}: {so_luong} sách")

    def hien_thi_sach_moi_nhat(self):
        if not self.ds_sach:
            print("Không có sách trong hệ thống.")
            return
        sach_moi_nhat = max(self.ds_sach, key=lambda x: x.ngay_xuat_ban)
        print("Sách mới nhất:")
        sach_moi_nhat.hien_thi_thong_tin()

    def tim_sach_theo_nam_xuat_ban(self, nam):
        print(f"Sách xuất bản trong năm {nam}:")
        sach_nam = [sach for sach in self.ds_sach if sach.ngay_xuat_ban.year == nam]
        if sach_nam:
            for sach in sach_nam:
                sach.hien_thi_thong_tin()
        else:
            print("Không tìm thấy sách nào trong năm này.")

   
    def chon_chuc_nang(self):
        menu = {
            1: 'Hiển thị danh sách sách',
            2: 'Thêm sách mới',
            3: 'Tìm kiếm sách',
            4: 'Cập nhật thông tin sách',
            5: 'Xóa sách',
            6: 'Tính tổng số sách',
            7: 'Tìm kiếm bằng regex',
            8: 'Thống kê theo thể loại',
            9: 'Sắp xếp theo ngày xuất bản',
            10: 'Hiển thị sách mới nhất',
            11: 'Tìm sách theo năm xuất bản',
            12: 'Đếm sách theo tác giả',
            13: 'Thoát'
        }

        while True:
            print("\nChọn một chức năng:")
            for key, value in menu.items():
                print(f"{key}. {value}")

            try:
                lua_chon = int(input("Nhập lựa chọn của bạn: "))

                if lua_chon == 1:
                    self.hien_thi_danh_sach_sach()
                elif lua_chon == 2:
                    ma_sach = input("Nhập mã sách: ")
                    tieu_de = input("Nhập tiêu đề sách: ")
                    tac_gia = input("Nhập tác giả: ")
                    the_loai = input("Nhập thể loại: ")
                    so_ban_sao = int(input("Nhập số bản sao: "))
                    sach_moi = Sach(ma_sach, tieu_de, tac_gia, the_loai, so_ban_sao)
                    self.them_sach(sach_moi)
                elif lua_chon == 3:
                    ma_sach = input("Nhập mã sách cần tìm (hoặc để trống để tìm theo tiêu đề): ")
                    tieu_de = None
                    if ma_sach == "":
                        tieu_de = input("Nhập tiêu đề sách cần tìm: ")
                    ket_qua = self.tim_kiem_sach(ma_sach, tieu_de)
                    for sach in ket_qua:
                        sach.hien_thi_thong_tin()
                elif lua_chon == 4:
                    ma_sach = input("Nhập mã sách cần cập nhật: ")
                    tieu_de = input("Nhập tiêu đề mới (để trống nếu không thay đổi): ")
                    tac_gia = input("Nhập tác giả mới (để trống nếu không thay đổi): ")
                    the_loai = input("Nhập thể loại mới (để trống nếu không thay đổi): ")
                    so_ban_sao = input("Nhập số bản sao mới (để trống nếu không thay đổi): ")
                    so_ban_sao = int(so_ban_sao) if so_ban_sao else None
                    self.cap_nhat_sach(ma_sach, tieu_de or None, tac_gia or None, the_loai or None, so_ban_sao)
                elif lua_chon == 5:
                    ma_sach = input("Nhập mã sách cần xóa: ")
                    self.xoa_sach(ma_sach)
                elif lua_chon == 6:
                    self.tong_so_sach()
                elif lua_chon == 7:
                    pattern = input("Nhập mẫu regex để tìm kiếm: ")
                    self.tim_kiem_theo_regex(pattern)
                elif lua_chon == 8:
                    self.thong_ke_theo_the_loai()
                elif lua_chon == 9:
                    self.sap_xep_theo_ngay_xuat_ban()
                elif lua_chon == 10:
                    self.hien_thi_sach_moi_nhat()
                elif lua_chon == 11:
                    nam = int(input("Nhập năm: "))
                    self.tim_sach_theo_nam_xuat_ban(nam)
                elif lua_chon == 12:
                    self.dem_sach_theo_tac_gia()
                elif lua_chon == 13:
                    print("Cảm ơn bạn đã sử dụng chương trình!")
                    break
                else:
                    print("Lựa chọn không hợp lệ, vui lòng thử lại.")

            except ValueError:
                print("Vui lòng nhập một số nguyên.")

if __name__ == '__main__':
    ql_sach = QuanLySach()
    ql_sach.tai_lai_du_lieu()
    ql_sach.chon_chuc_nang()
