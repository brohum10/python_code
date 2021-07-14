print("Sales Amount \t Commission")

sales = 10000
f_p = 5000 * (8/100)
#f_p is 400
t_p = 5000 * (10/100)
#t_p is 1000


def computeComission(sales):
    if sales <= 5000:
        comm = sales * (8/100)
        print(sales ,"\t\t %.1f"  %comm)
    elif sales >= 10000.1:
        comm = ((sales-10000) * (12/100)) + f_p + t_p
        print(sales ,"\t\t %.1f"  %comm)
    else:
        comm = ((sales-5000) * (10/100)) + f_p
        print(sales ,"\t\t %.1f"  %comm)


for sales in range(10000, 105000, 5000):
    computeComission(sales)
