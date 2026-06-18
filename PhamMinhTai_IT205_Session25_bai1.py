class BankAccount:
    # Class Attributes
    bank_name = "Vietcombank"
    transaction_fee = 2000

    def __init__(self, account_number, account_name):
        self.__account_number = account_number
        self.__balance = 0
        self.account_name = account_name

    @property
    def balance(self):
        return self.__balance

    @property
    def account_name(self):
        return self.__account_name

    @account_name.setter
    def account_name(self, new_name):
        cleaned_name = " ".join(new_name.strip().split())

        if cleaned_name == "":
            print("Tên tài khoản không được để trống")
            return

        self.__account_name = cleaned_name.upper()

    @staticmethod
    def validate_account_number(account_number):
        return account_number.isdigit() and len(account_number) == 10

    @classmethod
    def update_transaction_fee(cls, new_fee):
        cls.transaction_fee = new_fee

    def deposit(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False

        self.__balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False

        total_amount = amount + BankAccount.transaction_fee

        if self.__balance < total_amount:
            print(
                "Giao dịch thất bại. Số dư không đủ để thanh toán số tiền và phí giao dịch"
            )
            return False

        self.__balance -= total_amount
        return True

    def display_info(self):
        print("\n--- THÔNG TIN TÀI KHOẢN ---")
        print(f"Ngân hàng: {BankAccount.bank_name}")
        print(f"Số tài khoản: {self.__account_number}")
        print(f"Tên chủ tài khoản: {self.__account_name}")
        print(f"Số dư hiện tại: {self.__balance:,} VND")
        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")


current_account = None

while True:
    print("\n===== VIETCOMBANK DIGIBANK SIMULATOR =====")
    print("1. Mở tài khoản mới")
    print("2. Xem thông tin tài khoản")
    print("3. Giao dịch Nạp / Rút tiền")
    print("4. Cập nhật Tên chủ tài khoản")
    print("5. Đổi phí giao dịch hệ thống")
    print("6. Thoát chương trình")
    print("==========================================")

    choice = input("Chọn chức năng (1-6): ")

    if choice == "1":
        print("\n--- MỞ TÀI KHOẢN MỚI ---")

        while True:
            account_number = input(
                "Nhập số tài khoản 10 chữ số: "
            )

            if BankAccount.validate_account_number(account_number):
                break

            print("Số tài khoản không hợp lệ!")
            print("Số tài khoản phải gồm đúng 10 chữ số.")

        account_name = input("Nhập tên chủ tài khoản: ")

        current_account = BankAccount(
            account_number,
            account_name
        )

        print("Mở tài khoản thành công!")
        print(f"Số tài khoản: {account_number}")
        print(
            f"Tên chủ tài khoản: {current_account.account_name}"
        )

    elif choice == "2":

        if current_account is None:
            print("Hệ thống chưa có thông tin tài khoản")
            print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
        else:
            current_account.display_info()

    elif choice == "3":

        if current_account is None:
            print("Hệ thống chưa có thông tin tài khoản")
            print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
            continue

        print("\n--- GIAO DỊCH NẠP / RÚT TIỀN ---")
        print("1. Nạp tiền")
        print("2. Rút tiền")

        transaction_type = input(
            "Chọn loại giao dịch (1-2): "
        )

        try:
            amount = int(
                input("Nhập số tiền giao dịch: ")
            )

            if transaction_type == "1":

                if current_account.deposit(amount):
                    print(
                        f"Nạp tiền thành công: +{amount:,} VND"
                    )
                    print(
                        f"Số dư mới: {current_account.balance:,} VND"
                    )

            elif transaction_type == "2":

                if current_account.withdraw(amount):
                    print(
                        f"Rút tiền thành công: -{amount:,} VND"
                    )
                    print(
                        f"Phí giao dịch: {BankAccount.transaction_fee:,} VND"
                    )
                    print(
                        f"Số dư mới: {current_account.balance:,} VND"
                    )
                else:
                    print(
                        f"Số dư mới: {current_account.balance:,} VND"
                    )

            else:
                print("Lựa chọn không hợp lệ")

        except ValueError:
            print("Vui lòng nhập số tiền hợp lệ")

    elif choice == "4":

        if current_account is None:
            print("Hệ thống chưa có thông tin tài khoản")
            print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
            continue

        print("\n--- CẬP NHẬT TÊN CHỦ TÀI KHOẢN ---")

        old_name = current_account.account_name

        new_name = input("Nhập tên mới: ")

        current_account.account_name = new_name

        if current_account.account_name != old_name:
            print(
                f"Cập nhật thành công. Tên mới: {current_account.account_name}"
            )

    elif choice == "5":

        print("\n--- ĐỔI PHÍ GIAO DỊCH HỆ THỐNG ---")
        print(
            f"Phí giao dịch hiện tại: {BankAccount.transaction_fee:,} VND"
        )

        try:
            new_fee = int(
                input("Nhập phí giao dịch mới: ")
            )

            if new_fee < 0:
                print("Phí giao dịch không được âm")
                print(
                    f"Phí giao dịch hiện tại vẫn là {BankAccount.transaction_fee:,} VND"
                )
            else:
                BankAccount.update_transaction_fee(new_fee)

                print(
                    f"Đã cập nhật phí giao dịch toàn hệ thống thành {new_fee:,} VND"
                )

        except ValueError:
            print("Phí giao dịch không hợp lệ")

    elif choice == "6":
        print("Cảm ơn bạn đã sử dụng Vietcombank Digibank!")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 6.")