# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，
# 高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，
# 高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

def getPayment(totalProfit):
    if totalProfit <= 10:
        return totalProfit * 0.1
    elif (totalProfit > 10) and (totalProfit < 20):
        return 10 * 0.1 + (totalProfit - 10) * 0.075
    elif (totalProfit >= 20) and (totalProfit < 40):
        return 10 * 0.1 + 10 * 0.075 + (totalProfit - 20) * 0.05
    return 'out of range'


print("input profit")
total = int(input("total="))
print(getPayment(total))


