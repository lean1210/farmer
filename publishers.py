import csv
import os
import re

class Publishers:
    Publishers = []
    file = 'publishers.csv'

    @classmethod
    def doc_file(cls):
        """Đọc dữ liệu từ publishers.csv"""
        if os.path.exists(cls.file):  # Kiểm tra file có tồn tại không
            with open(cls.file, mode='r', newline='', encoding="utf-8") as sam:
                reader = csv.DictReader(sam)
                cls.Publishers = list(reader)
            print(f"Đã tải {len(cls.Publishers)} nhà xuất bản từ file.")
        else:
            print(f"Không tìm thấy file {cls.file}. Tạo danh sách mới.")

    @classmethod
    def ghi_file(cls):
        """Ghi dữ liệu khi có sự thay đổi vào publishers.csv"""
        with open(cls.file, mode='w', newline='', encoding='utf-8') as sam:  # Mở file với mode 'w' để ghi đè dữ liệu mới
            fieldnames = ['ma', 'ten', 'dia_chi', 'email', 'sdt']
            writer = csv.DictWriter(sam, fieldnames=fieldnames)
            writer.writeheader()  # Ghi header vào file
            writer.writerows(cls.Publishers)  # Ghi danh sách nhà xuất bản
        print("Dữ liệu đã được ghi vào file thành công.")

    @classmethod
    def hien_thi_danh_sach(cls):
        if len(cls.Publishers) == 0:
            print("Danh sách nhà xuất bản trống.")
        else:
            print(f"{'Mã':<5}{'Tên':<20}{'Địa chỉ':<30}{'Email':<30}{'SDT':<10}")
            print("-" * 95)
            for nxb in cls.Publishers:
                print(f"{nxb['ma']:<5}{nxb['ten']:<20}{nxb['dia_chi']:<30}{nxb['email']:<30}{nxb['sdt']:<10}")

    @classmethod
    def tim_kiem_theo_ma(cls):
        ma = input("Mời bạn nhập mã nhà xuất bản để tìm: ").lower()
        ket_qua = [nxb for nxb in cls.Publishers if ma in nxb['ma'].lower()]
        if len(ket_qua) == 0:
            print("Không tìm thấy nhà xuất bản nào với mã này.")
        else:
            print(f"{'Mã':<5}{'Tên':<20}{'Địa chỉ':<30}{'Email':<30}{'SĐT':<10}")
            print("-" * 95)
            for nxb in ket_qua:
                print(f"{nxb['ma']:<5}{nxb['ten']:<20}{nxb['dia_chi']:<30}{nxb['email']:<30}{nxb['sdt']:<10}")

    @classmethod
    def tim_kiem_theo_ten(cls):
        ten = input("Mời bạn nhập tên nhà xuất bản để tìm: ").lower()
        ket_qua = [nxb for nxb in cls.Publishers if ten in nxb['ten'].lower()]
        if len(ket_qua) == 0:
            print("Không tìm thấy nhà xuất bản nào với tên này.")
        else:
            print(f"{'Mã':<5}{'Tên':<20}{'Địa chỉ':<30}{'Email':<30}{'SĐT':<10}")
            print("-" * 95)
            for nxb in ket_qua:
                print(f"{nxb['ma']:<5}{nxb['ten']:<20}{nxb['dia_chi']:<30}{nxb['email']:<30}{nxb['sdt']:<10}")

    @classmethod
    def them_moi(cls):
        ma = cls.nhap_ma()
        ten = cls.nhap_ten()
        dia_chi = cls.nhap_dia_chi()
        email = cls.nhap_email()
        sdt = cls.nhap_sdt()
        # Thêm thông tin mới vào danh sách Publishers
        cls.Publishers.append({'ma': ma, 'ten': ten, 'dia_chi': dia_chi, 'email': email, 'sdt': sdt})
        print("Cập nhật thông tin Nhà Xuất Bản thành công.")
        cls.ghi_file()  # Ghi dữ liệu vào file ngay sau khi thêm mới

    @classmethod
    def xoa(cls):
        ma = input("Nhập mã nhà xuất bản cần xóa: ")
        for nxb in cls.Publishers:
            if nxb['ma'] == ma:
                cls.Publishers.remove(nxb)
                print("Xóa nhà xuất bản thành công.")
                cls.ghi_file()  # Ghi dữ liệu vào file sau khi xóa
                return
        print("Không tìm thấy nhà xuất bản có mã này!")

    @classmethod
    def sap_xep_theo_ten(cls):
        cls.Publishers.sort(key=lambda x: x['ten'])
        print("Danh sách đã được sắp xếp theo tên Nhà Xuất Bản (A-Z).")
        cls.hien_thi_danh_sach()
        cls.ghi_file()  # Ghi dữ liệu vào file sau khi sắp xếp

    @classmethod
    def dem_so_luong(cls):
        print(f"Tổng số Nhà Xuất Bản hiện có: {len(cls.Publishers)}")

    @classmethod
    def cap_nhat(cls):
        ma = input("Nhập mã nhà xuất bản cần cập nhật: ")
        for nxb in cls.Publishers:
            if nxb['ma'] == ma:
                print(f"Đang cập nhật thông tin cho Nhà Xuất Bản {nxb['ten']}")
                nxb['ten'] = cls.nhap_ten() or nxb['ten']
                nxb['dia_chi'] = cls.nhap_dia_chi() or nxb['dia_chi']
                nxb['email'] = cls.nhap_email() or nxb['email']
                nxb['sdt'] = cls.nhap_sdt() or nxb['sdt']
                print("Cập nhật thông tin Nhà Xuất Bản thành công.")
                cls.ghi_file()  # Ghi dữ liệu vào file sau khi cập nhật
                return
        print("Không tìm thấy nhà xuất bản có mã này!")

    @classmethod
    def dao_nguoc_danh_sach(cls):
        if len(cls.Publishers) == 0:
            print("Danh sách nhà xuất bản trống, không đảo ngược.")
        else:
            cls.Publishers.reverse()
            print("Danh sách nhà xuất bản đã được đảo ngược.")
            cls.hien_thi_danh_sach()
            cls.ghi_file()  # Ghi dữ liệu vào file sau khi đảo ngược

    @classmethod
    def loc_theo_ma(cls):
        ma = input("Nhập mã nhà xuất bản để lọc: ").lower()
        ket_qua = [nxb for nxb in cls.Publishers if ma in nxb['ma'].lower()]
        if len(ket_qua) == 0:
            print("Không có nhà xuất bản với phần mã đã nhập.")
        else:
            print(f"{'Mã':<5}{'Tên':<20}{'Địa chỉ':<30}{'Email':<30}{'SĐT':<10}")
            print("-" * 95)
            for nxb in ket_qua:
                print(f"{nxb['ma']:<5}{nxb['ten']:<20}{nxb['dia_chi']:<30}{nxb['email']:<30}{nxb['sdt']:<10}")

    # các phương thức kiểm tra dữ liệu người dùng
    @classmethod
    def nhap_ma(cls):
        while True:
            ma = input("Nhập mã nhà xuất bản (không để trống): ").strip()
            if ma:
                return ma
            print("Mã nhà xuất bản không được để trống. Vui lòng nhập lại.")

    @classmethod
    def nhap_ten(cls):
        while True:
            ten = input("Nhập tên nhà xuất bản (không để trống): ").strip()
            if ten:
                return ten
            print("Tên nhà xuất bản không được để trống. Vui lòng nhập lại.")

    @classmethod
    def nhap_dia_chi(cls):
        while True:
            dia_chi = input("Nhập địa chỉ nhà xuất bản: ").strip()
            if dia_chi:
                return dia_chi
            print("Địa chỉ không được để trống. Vui lòng nhập lại.")

    @classmethod
    def nhap_email(cls):
        while True:
            email = input("Nhập email nhà xuất bản: ").strip()
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                return email
            print("Email không hợp lệ. Vui lòng nhập lại.")

    @classmethod
    def nhap_sdt(cls):
        while True:
            sdt = input("Nhập số điện thoại nhà xuất bản (10 chữ số): ").strip()
            if re.match(r"^\d{10}$", sdt):
                return sdt
            print("Số điện thoại không hợp lệ. Vui lòng nhập lại.")

    @staticmethod
    def confirm_action(prompt):
        while True:
            xac_nhan = input(f"{prompt} (y/n): ").lower()
            if xac_nhan in ['y', 'n']:
                return xac_nhan == 'y'
            print("Lựa chọn không hợp lệ. Vui lòng nhập 'y'  hoặc 'n' .")

    @classmethod
    def menu(cls):
        while True:
            print("Quản lý nhà xuất bản:")
            print("1. Hiển thị danh sách")
            print("2. Tìm kiếm theo mã")
            print("3. Tìm kiếm theo tên")
            print("4. Thêm mới")
            print("5. Xóa")
            print("6. Sắp xếp theo tên")
            print("7. Đếm số lượng NXB")
            print("8. Đảo ngược danh sach NXB")
            print("9. Cập nhật")
            print("10. Lọc theo mã" )
            print("11. Thoát")
            lua_chon = input("Chọn chức năng từ 1-11: ")
            match lua_chon:
                case '1':
                    cls.hien_thi_danh_sach()
                case '2':
                    cls.tim_kiem_theo_ma()
                case '3':
                    cls.tim_kiem_theo_ten()
                case '4':
                    cls.them_moi()
                case '5':
                    cls.xoa()
                case '6':
                    cls.sap_xep_theo_ten()
                case '7':
                    cls.dem_so_luong()
                case'8':
                    cls.dao_nguoc_danh_sach()
                case'9':
                    cls.cap_nhat()
                case'10':
                    cls.loc_theo_ma()
                case '11':
                    if cls.confirm_action("Bạn có chắc chắn muốn thoát không"):
                        print("Thoát menu.")
                    break
                case _:
                    print("Lựa chọn không hợp lệ, mời bạn chọn lại.")


