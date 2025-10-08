def check_loan(age: int, income: int) -> str:
    res = ""

    if (age < 0 or age > 200) or (income < 0):
        res = "Không hợp lệ"

    elif (18 > age or age > 60) or (income < 3000000):
        res = "Không đủ điều kiện"

    else:
        res = "Đủ điều kiện"

    return res