S = 50
def main():
    x1 = [0] * (S + 1)
    x2 = [0] * (S + 1)
    y = [0] * (S + 1)
    sum_Y = 0
    sum_X1 = 0
    sum_X1_sq = 0
    sum_X2 = 0
    sum_X2_sq = 0
    sum_X1Y = 0
    sum_X2Y = 0
    sum_X1X2 = 0
    
    n = int(input("How many data points? "))
    
    print("Enter data: ")
    
    for index in range(1, n + 1):
        y[index] = float(input(f"y[{index}] = "))
        x1[index] = float(input(f"x1[{index}] = "))
        x2[index] = float(input(f"x2[{index}] = "))
        
        
    for index in range(1, n + 1):
        sum_Y += y[index]
        sum_X1 += x1[index]
        sum_X2 += x2[index]
        sum_X1_sq += x1[index] ** 2
        sum_X2_sq += x2[index] * x2[index]
        sum_X1Y += x1[index] * y[index]
        sum_X2Y += x2[index] * y[index]
        sum_X1X2 += x1[index] * x2[index]
        
    X1_sq = sum_X1 ** 2
    X2_sq = sum_X2 ** 2
    
    reg_X1_sq = sum_X1_sq - (X1_sq/n)
    reg_X2_sq = sum_X2_sq - (X2_sq/n)
    reg_X1Y = sum_X1Y - ((sum_X1 * sum_Y)/n)
    reg_X2Y = sum_X2Y - ((sum_X2 * sum_Y)/n)
    reg_X1X2 = sum_X1X2 - ((sum_X1 * sum_X2)/n)
    
    b1 = ((reg_X2_sq * reg_X1Y) - (reg_X1X2 * reg_X2Y)) / ((reg_X1_sq * reg_X2_sq) - (reg_X1X2 ** 2))
    b2 = ((reg_X1_sq * reg_X2Y) - (reg_X1X2 * reg_X1Y)) / ((reg_X1_sq * reg_X2_sq) - (reg_X1X2 ** 2))
    
    mean_Y = sum_Y / n
    mean_X1 = sum_X1 / n
    mean_X2 = sum_X2 / n
    
    a = mean_Y - (b1 * mean_X1) - (b2 * mean_X2)
    round_a = round(a, 4)
    round_b1 = round(b1, 4)
    round_b2 = round(b2, 4)
    print("The regression line is: ")
    print(f"y = ({round_a}) + ({round_b1})x1 + ({round_b2})x2")
if __name__ == "__main__":
    main()
