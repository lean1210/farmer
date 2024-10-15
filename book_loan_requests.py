import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import re


class Request_manager:
    file_path = 'book_loan_requests.xlsx'
    @classmethod
    def check_ID(cls, id):
        reid = r'[a-zA-Z]{3}\d{4}\b'
        if re.match(reid,id): return True
        else: return False

    @classmethod
    def load_request(cls):
        try:
            return pd.read_excel(cls.file_path)
        except FileNotFoundError:
            return pd.DataFrame(columns=['Request_ID','Customer_ID','Loan_start_date','Loan_end_date','Return_Date','Book_ID','Quantity'])
    
    @classmethod
    def save_request(cls, df):
        df.to_excel(cls.file_path, index = False)

    @classmethod    
    def add_new_requests(cls):
        new_request_data = cls.get_infor()
        df = cls.load_request()
        df = pd.concat([df,pd.DataFrame([new_request_data])], ignore_index=True)
        cls.confirm_change(cls, df)

    @classmethod
    def update_requests(cls):
        date_format = "%m/%d/%Y"
        print('Câp nhật')
        df = cls.load_request()
        while True:
            while True:
                request_id_ud = input('Nhập mã sách muốn cập nhật vd ABC1234 (exit để trở lại): ').upper()
                if request_id_ud == 'EXIT': cls.choose_action() 
                if cls.check_ID(request_id_ud): break
                else: print('Sai định dạng mã. Mã nhập theo mẫu vd: ABC1234.')
            if request_id_ud in list(df['Request_ID']):
                break
            else:
                print('Mã mượn sách không tồn tại.')
        print(f'Nhập thông tin cho mã mượn {request_id_ud}')
        while True:
            customer_id_ud = input('Nhâp mã khách hàng vd: ABC1234 (exit để trở lại): ').upper()
            if customer_id_ud == 'EXIT': cls.choose_action() 
            if cls.check_ID(customer_id_ud): break
            else: print('Sai định dạng mã. Mã nhập theo mẫu vd: ABC1234.')
        while True:
            book_id_ud = input('Nhập mã sách vd: ABC1234 (exit để trở lại): ').upper()
            if book_id_ud == 'EXIT': cls.choose_action() 
            if cls.check_ID(book_id_ud): break
            else: print('Sai định dạng mã. Mã nhập theo mẫu vd: ABC1234. ')        
        while True:
            while True:
                loan_start_date_ud = input('Nhập ngày mượn sách định dang (mm/dd/yyyy) (exit để trở lại): ')
                if loan_start_date_ud == 'EXIT': cls.choose_action() 
                try:
                    datetime.strptime(loan_start_date_ud, date_format)
                    break
                except ValueError:
                    print('Nhập sai định dạng nhập lại')

            while True:  
                loan_end_date_ud = input('Nhập ngày hẹn trả sách định dang (mm/dd/yyyy) (exit để trở lại): ')
                if loan_end_date_ud == 'EXIT': cls.choose_action() 
                try:
                    datetime.strptime(loan_end_date_ud, date_format)
                    break
                except ValueError:
                    print('Sai định dạng mời nhập lại.')
            if datetime.strptime(loan_end_date_ud, date_format) >= datetime.strptime(loan_start_date_ud, date_format): 
                break
            else: print('Ngày trả phải sau ngày mượn, nhập lại.')

        while True:
            quantity_ud = input('Nhập số lượng sách mượn (exit để trở lại): ')
            if quantity_ud == 'EXIT': cls.choose_action() 
            try:
                quantity_ud = int(quantity_ud)
                if quantity_ud < 0: print('Số lượng phải lớn hơn 0.')
                else: break
            except ValueError:
                print('Số lượng phải là số nguyên: ')

        df.loc[df['Request_ID'] == request_id_ud, ['Customer_ID', 'Loan_start_date', 'Loan_end_date', 'Book_ID', 'Quantity']] = [customer_id_ud, loan_start_date_ud, loan_end_date_ud, book_id_ud, quantity_ud]
        cls.confirm_change(cls, df)

    @classmethod
    def show_requests(cls):
        df = cls.load_request()
        df50  = df.tail(50)
        print(df50)

    @classmethod    
    def search_requests(cls):#################################################################################
        print('Tìm kiếm')
        info_search = input('Nhập mã đơn hoặc mã khách hàng: ')
        df = cls.load_request()
        dfrq = df[df['Request_ID'] == info_search]
        dfc = df[df['Customer_ID'] == info_search]
        df = pd.concat([dfrq, dfc], axis=0)
        return df

    @classmethod    
    def search_requests2(cls): 
        df = cls.load_request()
        while True:
            info_search = input('Tìm kiếm bằng mã 7 kí tự vd: (ABC   7) (exit để trở lại): ').upper()
            if info_search == 'EXIT': cls.choose_action() 
            if len(info_search) == 7: break 
            else: print('Mã phải gồm 7 kí tự vd: (ABC   7).')
        a,b,c,d,e,g,h = map(str, info_search)
        ws = [a,b,c,d,e,g,h]
        for i in range(7):
            if ws[i] == ' ':
                ws[i] = 'a-zA-Z0-9'

        re_search = f"[{ws[0]}][{ws[1]}][{ws[2]}][{ws[3]}][{ws[4]}][{ws[5]}][{ws[6]}]"
        list_customer = re.findall(re_search, df['Customer_ID'].to_string())
        list_book = re.findall(re_search, df['Book_ID'].to_string())
        list_rq = re.findall(re_search, df['Request_ID'].to_string())

        dfcustomer = df[df['Customer_ID'].isin(list_customer)]
        dfbook = df[df['Book_ID'].isin(list_book)]
        dfrq = df[df['Request_ID'].isin(list_rq)]
        return_df = pd.concat([dfrq, dfcustomer, dfbook], axis=0,  ignore_index=True)
        return return_df

    @classmethod
    def del_requests(cls):
        print('Xoá phiếu mượn sách')
        df = cls.load_request()
        while True:    
            ID_del_request = input('Nhập mã mượn sách vd: ABC1234 (exit để trở lại): ').upper()
            if ID_del_request == 'EXIT': cls.choose_action()
            if cls.check_ID(ID_del_request): break
            else: print('Sai định dạng mã. Mã nhập theo mẫu vd: ABC1234.')
            if ID_del_request in df['Request_ID'].values:
                df = df[df['Request_ID'] != ID_del_request]
                cls.confirm_change(df)
                break
            else:
                print('Mã phiếu mượn không tồn tại.')
            
    @classmethod
    def check_loans(cls):
        today = datetime.now()
        df = cls.load_request()
        df['Loan_end_date'] = pd.to_datetime(df['Loan_end_date'], errors = 'coerce')

        late_loans = df[(df['Loan_end_date'] < today) & (df['Return_date'].isna())]
        return late_loans
    
    @classmethod
    def notifications_late_loans(cls, late_loans):   # thông báo phiếu quá bạn
        if not late_loans.empty:
            print('Có đơn sách quá hạn.')
        else:
            print('Have a nice day.')

    @classmethod
    def show_late_loans(cls):                 # hiển thị phiếu quá hạn
        print('Các đơn sách bị quá hạn:')
        print(cls.check_loans())

    @classmethod
    def update_returned(cls):                          # cập nhật phiếu đã trả
        print('Trả sách')
        date = datetime.today().strftime("%m/%d/%Y")
        date = str(date)
        df = cls.load_request()
        while True:
            lr_ID = input('Nhập mã phiếu trả vd: ABC1234 (exit để trở lại): ').upper()
            if lr_ID == 'EXIT': cls.choose_action()
            if cls.check_ID(lr_ID): 
                if lr_ID in list(df['Request_ID']):
                    if pd.isna(df.loc[df['Request_ID'] == lr_ID, 'Return_date'].values[0]):
                        break
                    else: print('Phiếu mượn đã trả.')
                else: print('Mã mượn không tồn tại.')
            else: print('Sai định dạng mã. Mã nhập theo mẫu vd: ABC1234.')
        df.loc[df['Request_ID'] == lr_ID, 'Return_date'] =  date
        cls.confirm_change(cls, df)
    # df.loc[df['Request_ID'] == request_id_ud, ['Customer_ID', 'Loan_start_date', 'Loan_end_date', 'Book_ID', 'Quantity']]
    @classmethod                  #"%m/%d/%Y"                
    def statistic(cls):
        print('Chức năng thống kê.')                  
        df = cls.load_request()

        df['Loan_start_date'] = pd.to_datetime(df['Loan_start_date'], format="%m/%d/%Y", errors='coerce')

        total_request = df['Request_ID'].count()
        print(f'Tổng số đơn mượn sách: {total_request}')
        total_book = df['Quantity'].sum()
        print(f'Tổng số sách được mượn: {total_book}')
        
        df_group = df.groupby('Loan_start_date').size()

        plt.figure(figsize=(10, 6))
        plt.plot(df_group.index, df_group, marker='o', linestyle='-', color='b')

        plt.title('Số đơn mượn sách', fontsize=16)
        plt.xlabel('Ngày', fontsize=12)
        plt.ylabel('Số lượng', fontsize=12)
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()

    @classmethod
    def backup(cls):    #ok
        file_path_backup = "book_loan_requests_backup.xlsx"
        df = cls.load_request()
        while True:
            confirm = input('Xác nhận (y/n): ').lower()
            if confirm == 'y':
                df.to_excel(file_path_backup, index = False)
                print('Thao tác thành công.')
                break
            elif confirm == 'n':
                print('Đã huỷ thao tác.')
                break
            else: print('Lựa chọn không hợp lệ. Chọn lại.')                          

    def confirm_change(cls, df):  #ok
        while True:
            confirm = input('Xác nhận (y/n): ').lower()
            if confirm == 'y':
                cls.save_request(df), print('Thao tác thành công.')
                break
            elif confirm == 'n':
                print('Đã huỷ thao tác.')
                break
            else: print('Lựa chọn không hợp lệ. Chọn lại.')  

    @classmethod
    def get_infor(cls): #ok
        date_format = "%m/%d/%Y"
        print('Nhập thông tin:')
        df = cls.load_request()
        while True:
            request_ID = input('Nhập mã mượn sách vd: ABC1234 (exit để trở lại): ').upper()
            if request_ID == 'EXIT': cls.choose_action()     
            if cls.check_ID(request_ID): break
            else: print('Sai định dạng mã. Mã nhập theo mẫu vd: ABC1234.')
            if request_ID in df['Request_ID'].to_list(): print('Mã đơn sách đã tồn tại.')
            else: break

        while True:
            customer_ID = input('Nhập mã khách hàng vd: ABC1234 (exit để trở lại): ').upper()
            if customer_ID == 'EXIT': cls.choose_action() 
            if cls.check_ID(customer_ID): break
            else: print('Sai định dạng mã. Mã nhập theo mẫu vd: ABC1234.')   
        while True:
            book_ID = input('Nhập mã sách vd ABC1234 (exit để trở lại): ').upper()
            if book_ID == 'EXIT': cls.choose_action() 
            if cls.check_ID(book_ID): break
            else: print('Sai định dạng mã. Mã nhập theo mẫu vd: ABC1234.')

        while True:
            while True:
                loan_start_date = input('Nhập ngày mượn sách định dang (mm/dd/yyyy) (exit để trở lại): ')
                if loan_start_date == 'EXIT': cls.choose_action() 
                try:
                    datetime.strptime(loan_start_date, date_format)
                    break
                except ValueError:
                    print('Nhập sai định dạng nhập lại')

            while True:  
                loan_end_date = input('Nhập ngày hẹn trả sách định dang (mm/dd/yyyy) (exit để trở lại): ')
                if loan_end_date == 'EXIT': cls.choose_action() 
                try:
                    datetime.strptime(loan_end_date, date_format)
                    break
                except ValueError:
                    print('Sai định dạng mời nhập lại.')
            if datetime.strptime(loan_end_date, date_format) >= datetime.strptime(loan_start_date, date_format): break
            else: print('Ngày trả phải sau ngày mượn, nhập lại.')

        return_date = ''
        while True:
            quantity = input('Nhập số lượng sách mượn (exit để trở lại): ')
            if quantity == 'EXIT': cls.choose_action() 
            try:
                quantity = int(quantity)
                if quantity < 0:
                    print('Số lượng phải lớn hơn 0.')
                else:
                    break
            except ValueError:
                print('Số lượng phải là số nguyên: ')

        new_request_data = {
        'Request_ID' : request_ID,
        'Customer_ID': customer_ID,
        'Loan_start_date': loan_start_date,
        'Loan_end_date': loan_end_date,
        'Book_ID' : book_ID,
        'Quantity' : quantity,
        'Return_date' : return_date
        }
        return new_request_data
################################
    @classmethod
    def choose_action(cls):
        while True:
            print(''' 
        Chọn thao tác:
                1: Tạo phiếu mượn       6: Trả sách
                2: Tìm kiếm             7: Thống kê
                3: Cập nhật             8: Phiếu quá hạn
                4: Hiển thị             9: Sao lưu
                5: Xoá phiếu mượn       0: Quay lại
    ''')
            action = input("Thao tác muốn thực hiện (0-9): ")
            if action == '1':
                cls.add_new_requests()
            elif action == '2':    
                print(cls.search_requests2())
            elif action == '3':    
                cls.update_requests()
            elif action == '4':     
                print('Hien thi')
                cls.show_requests()
            elif action == '5':    
                cls.del_requests()
            elif action == '6':    
                cls.update_returned()
            elif action == '7':    
                cls.statistic()
            elif action == '8':    
                cls.show_late_loans()
            elif action == '9':    
                cls.backup()
            elif action == '0':
                break
            else:
                print('Thao tác sai.')
