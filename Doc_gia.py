import re
from datetime import datetime

class DocGia:
    def __init__(self, ma, ten, email, sdt, ngay_dang_ki=None):
        self.ma = ma 
        self.ten = ten 
        self.email = email 
        self.sdt = sdt 
        if ngay_dang_ki is None:
            self.ngay_dang_ki = datetime.now()
        else:
            self.ngay_dang_ki = ngay_dang_ki

    def hien_thi_thong_tin(self):
        print(f"Mã độc giả: {self.ma}")
        print(f"Tên độc giả: {self.ten}")
        print(f"Email: {self.email}")
        print(f"Số điện thoại: {self.sdt}")
        print(f"Ngày đăng ký: {self.ngay_dang_ki.strftime('%Y-%m-%d')}")

class QuanLyDocGia:
    def __init__(self):
        self.ds_doc_gia = []

    def kiem_tra_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email)

    def kiem_tra_sdt(self, sdt):
        pattern = r'^[0-9]{10}$'
        return re.match(pattern, sdt)

    def them_doc_gia(self, ds_doc_gia, doc_gia):
        if not self.kiem_tra_email(doc_gia.email):
            print("Email không hợp lệ! Vui lòng nhập lại.")
            return
        if not self.kiem_tra_sdt(doc_gia.sdt):
            print("Số điện thoại không hợp lệ! Vui lòng nhập lại.")
            return
        ds_doc_gia.append(doc_gia)
        self.luu_du_lieu_vao_file(ds_doc_gia)
        print(f"Đã thêm độc giả: {doc_gia.ten}")

    def tim_kiem_doc_gia(self, ds_doc_gia, ma=None, ten=None):
        ket_qua = []
        for doc_gia in ds_doc_gia: 
            if (ma and doc_gia.ma == ma) or (ten and doc_gia.ten.lower() == ten.lower()):
                ket_qua.append(doc_gia)
        return ket_qua 

    def hien_thi_danh_sach_doc_gia(self, ds_doc_gia):
        for doc_gia in ds_doc_gia:
            doc_gia.hien_thi_thong_tin()

    def cap_nhat_doc_gia(self,ds_doc_gia, doc_gia, ten=None, email=None, ma=None):
        if ten:
            doc_gia.ten = ten 
        if email:
            doc_gia.email = email 
        if ma:
            doc_gia.ma = ma 
        self.luu_du_lieu_vao_file(ds_doc_gia)
        print(f"Đã cập nhật thông tin độc giả: {doc_gia.ten}")

    def xoa_doc_gia(self, ds_doc_gia, ma):
        doc_gia = self.tim_kiem_doc_gia(ds_doc_gia, ma=ma)
        if doc_gia:
            ds_doc_gia.remove(doc_gia[0])
            self.luu_du_lieu_vao_file(ds_doc_gia)
            print(f"Đã xóa độc giả có mã: {ma}")
        else:
            print(f"Không tìm thấy độc giả với mã: {ma}")

    def luu_du_lieu_vao_file(self, ds_doc_gia, ten_file='doc_gia.txt'):
        with open(ten_file, 'w', encoding='utf-8') as f:
            for doc_gia in ds_doc_gia:
                f.write(f"{doc_gia.ma},{doc_gia.ten},{doc_gia.email},{doc_gia.sdt},{doc_gia.ngay_dang_ki.strftime('%Y-%m-%d')}\n")
        print(f"Dữ liệu đã được lưu vào file {ten_file}")

    def tai_lai_du_lieu(self, ds_doc_gia, ten_file='doc_gia.txt'):
        try:
            with open(ten_file, 'r', encoding='utf-8') as f:
                ds_doc_gia.clear()
                for line in f:
                    ma, ten, email, sdt, ngay_dang_ki = line.strip().split(',')
                    ngay_dang_ki = datetime.strptime(ngay_dang_ki, '%Y-%m-%d')
                    doc_gia = DocGia(ma, ten, email, sdt, ngay_dang_ki)
                    ds_doc_gia.append(doc_gia)
            print("Dữ liệu đã được tải lại từ file.")
        except FileNotFoundError:
            print("Không tìm thấy file để tải dữ liệu.")

    def tong_so_doc_gia(self, ds_doc_gia):
        print(f"Tổng số độc giả hiện có: {len(ds_doc_gia)}")

    def tim_kiem_theo_regex(self, ds_doc_gia, pattern):
        regex = re.compile(pattern)
        ket_qua = [doc_gia for doc_gia in ds_doc_gia if regex.search(doc_gia.email) or regex.search(doc_gia.sdt)]
        if ket_qua:
            for doc_gia in ket_qua:
                doc_gia.hien_thi_thong_tin()
        else:
            print("Không tìm thấy kết quả phù hợp.")

    def kiem_tra_trung_lap(self, ds_doc_gia, ma=None, email=None):
        for doc_gia in ds_doc_gia:
            if (ma and doc_gia.ma == ma) or (email and doc_gia.email.lower() == email.lower()):
                print("Độc giả đã tồn tại với thông tin trùng lặp.")
                return True
        print("Không tìm thấy thông tin trùng lặp.")
        return False

    def chon_chuc_nang(self, ds_doc_gia):
        menu = {
            1: 'Hiển thị danh sách độc giả',
            2: 'Thêm độc giả',
            3: 'Tìm kiếm độc giả',
            4: 'Cập nhật thông tin độc giả',
            5: 'Xóa độc giả',
            6: 'Tính tổng số độc giả',
            7: 'Tìm kiếm bằng regex',
            8: 'Kiểm tra trùng lặp',
            9: 'Lưu dữ liệu vào file',
            10: 'Tải lại dữ liệu từ file',
            11: 'Thoát'
        }

        while True:
            print("\nChọn một chức năng:")
            for key, value in menu.items():
                print(f"{key}. {value}")

            try:
                lua_chon = int(input("Nhập lựa chọn của bạn: "))

                if lua_chon == 1:
                    self.hien_thi_danh_sach_doc_gia(ds_doc_gia)
                elif lua_chon == 2:
                    ma = input("Nhập mã độc giả: ")
                    ten = input("Nhập tên độc giả: ")
                    email = input("Nhập email: ")
                    sdt = input("Nhập số điện thoại: ")
                    doc_gia_moi = DocGia(ma, ten, email, sdt)
                    self.them_doc_gia(ds_doc_gia, doc_gia_moi)
                elif lua_chon == 3:
                    ma = input("Nhập mã độc giả (hoặc để trống để tìm theo tên): ")
                    ten = input("Nhập tên độc giả (hoặc để trống để tìm theo mã): ")
                    ket_qua = self.tim_kiem_doc_gia(ds_doc_gia, ma=ma, ten=ten)
                    for doc_gia in ket_qua:
                        doc_gia.hien_thi_thong_tin()
                elif lua_chon == 4:
                    ma = input("Nhập mã độc giả cần cập nhật: ")
                    doc_gia = self.tim_kiem_doc_gia(ds_doc_gia, ma=ma)
                    if doc_gia:
                        doc_gia = doc_gia[0]
                        ten = input("Nhập tên mới (để trống nếu không muốn thay đổi): ").strip()
                        email = input("Nhập email mới (để trống nếu không muốn thay đổi): ").strip()
                        self.cap_nhat_doc_gia(ds_doc_gia=ds_doc_gia,doc_gia=doc_gia, ten=ten if ten else None, email=email if email else None)
                    else:
                        print("Không tìm thấy độc giả.")
                elif lua_chon == 5:
                    ma = input("Nhập mã độc giả cần xóa: ")
                    self.xoa_doc_gia(ds_doc_gia, ma)
                elif lua_chon == 6:
                    self.tong_so_doc_gia(ds_doc_gia)
                elif lua_chon == 7:
                    pattern = input("Nhập mẫu tìm kiếm (regex): ")
                    self.tim_kiem_theo_regex(ds_doc_gia, pattern)
                elif lua_chon == 8:
                    ma = input("Nhập mã độc giả cần kiểm tra (để trống nếu không kiểm tra theo mã): ")
                    email = input("Nhập email cần kiểm tra (để trống nếu không kiểm tra theo email): ")
                    self.kiem_tra_trung_lap(ds_doc_gia, ma=ma, email=email)
                elif lua_chon == 9:
                    self.luu_du_lieu_vao_file(ds_doc_gia)
                elif lua_chon == 10:
                    self.tai_lai_du_lieu(ds_doc_gia)
                elif lua_chon == 11:
                    print("Đã thoát chương trình.")
                    break
                else:
                    print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
            except ValueError:
                print("Lỗi: Vui lòng nhập số hợp lệ.")

if __name__ == "__main__":
    ds_doc_gia = []  # Khởi tạo danh sách độc giả

    # Tạo đối tượng quản lý độc giả từ lớp QuanLyDocGia, không phải DocGia
    quan_ly_doc_gia = QuanLyDocGia()

    # Thêm một độc giả ví dụ vào danh sách
    doc_gia = DocGia(ma='001', ten='John Doe', email='john@example.com', sdt='1234567890')
    ds_doc_gia.append(doc_gia)  # Thêm độc giả vào danh sách

    # Gọi phương thức chọn chức năng từ đối tượng QuanLyDocGia
    quan_ly_doc_gia.chon_chuc_nang(ds_doc_gia)




