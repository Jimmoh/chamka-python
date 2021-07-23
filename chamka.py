def calculate_tax(gross_pay):
    if gross_pay > 50000:
        return gross_pay * 15 / 100
    else:
        return 0


def main():
    print("Enter Employee's Name")
    e_name = input()
    print("PayRoll Number")
    p_no = input()
    print("Employee's grade (x or y)")
    grade = input()
    print("Hours worked")
    hours = float(input())
    print("Distance in Km")
    distance = float(input())
    if grade == "x":
        wage = hours * 1300
        mileage = distance * 75
        if mileage > 30000:
            mileage = 30000
        h_allowance = 0
    if grade == "y":
        wage = hours * 1600
        mileage = distance * 117
        if mileage > 30000:
            mileage = 30000
        h_allowance = 20000
    gross_pay = wage + mileage + h_allowance
    tax = calculate_tax(gross_pay)
    net_pay = gross_pay - tax
    print(f"Name: {e_name}")
    print(f"Payroll number: {p_no}")
    print(f"Basic Pay: {wage}")
    print(f"Allowance: {h_allowance}")
    print(f"Gross Pay: {gross_pay}")
    print(f"Tax: {tax}")
    print(f"Net Pay: {net_pay}")


if __name__ == "__main__":
    main()
