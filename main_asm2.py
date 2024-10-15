from publishers import Publishers

def main():
    Publishers.doc_file()  # Tải dữ liệu từ file CSV khi khởi động
    while True:
        print("Quản lý nhà xuất bản:")
        print("1. Hiển thị danh sách")
        print("2. Tìm kiếm theo mã")
        print("3. Tìm kiếm theo tên")
        print("4. Thêm mới")
        print("5. Xóa")
        print("6. Sắp xếp theo tên")
        print("7. Đếm số lượng NXB")
        print("8. Đảo ngược danh sách NXB")
        print("9. Cập nhật")
        print("10. Lọc theo mã")
        print("11. Thoát")
        lua_chon = input("Chọn chức năng (1-11): ")

        if lua_chon == '1':
            Publishers.hien_thi_danh_sach()
        elif lua_chon == '2':
            Publishers.tim_kiem_theo_ma()
        elif lua_chon == '3':
            Publishers.tim_kiem_theo_ten()
        elif lua_chon == '4':
            Publishers.them_moi()
        elif lua_chon == '5':
            Publishers.xoa()
        elif lua_chon == '6':
            Publishers.sap_xep_theo_ten()
        elif lua_chon == '7':
            Publishers.dem_so_luong()
        elif lua_chon == '8':
            Publishers.dao_nguoc_danh_sach()
        elif lua_chon == '9':
            Publishers.cap_nhat()
        elif lua_chon == '10':
            Publishers.loc_theo_ma()
        elif lua_chon == '11':
            if Publishers.confirm_action("Bạn có chắc chắn muốn thoát không?"):
                print("Chương trình kết thúc.")
                break
        else:
            print("Lựa chọn không hợp lệ, mời bạn chọn lại.")

if __name__ == "__main__":
    main()
