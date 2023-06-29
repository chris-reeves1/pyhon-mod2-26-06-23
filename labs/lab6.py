def getIncomeTax(salary):
    if salary < 11850:
        return 0
    elif 11850 <= salary <= 34500:
        return (salary - 11850) * 0.2
    elif 34501 <= salary <= 150000:
        return 4530 + ((salary - 34500) * 0.4)
    else:
        return 50730 + ((salary - 150000)) * 0.45 

salary = 200000
tax_amount = getIncomeTax(salary)
print("Tax anmount for salary £{} is £{}".format(salary, tax_amount))