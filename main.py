from book_loan_requests import Request_manager
from publishers import *
from confirm import confirm_exit

from Doc_gia import *
from son import *
from thanh import *

class_library = {
    "1": 'books',
    "2": 'requests',
    "3": 'categories',
    "4": 'customers',
    "5": 'publishers'
}

if __name__ == "__main__":
    ds_doc_gia = []  
    doc_gia1 = DocGia(ma='001', ten='John Doe', email='john@example.com', sdt='123456789')
    ds_doc_gia.append(doc_gia1)
    quan_ly_doc_gia = QuanLyDocGia()

    while True:
        print('-------------Chương Trình Quản Lý Thư Viện------------')
        Request_manager.notifications_late_loans(Request_manager.check_loans())
        print(''' 
            1: Sách             4: Độc giả
            2: Phiếu mượn       5: Nhà xuất bản
            3: Thể loại  ''')
        user_input = input("Nhập mã đối tượng muốn tương tác ('q' để thoát): ").strip().lower()
        if user_input == 'q':
            confirm_exit()
            
        elif user_input in class_library: 
            if user_input == '1' or user_input == 'books': 
                print('Sách')
                ql_sach = QuanLySach()
                ql_sach.tai_lai_du_lieu()
                ql_sach.chon_chuc_nang()

            elif user_input == '2' or user_input == 'requests':
                print('Phiếu mượn')
                Request_manager.choose_action()
            elif user_input == '3': 
                menu_quan_ly()
            elif user_input == '4':
                quan_ly_doc_gia.chon_chuc_nang(ds_doc_gia)
            elif user_input == '5':
                Publishers.menu()
        else:
            print("Đối tượng không tồn tại. Vui lòng chọn lại.")

