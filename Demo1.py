# 输出字面量尝试
"""我是多行注释"""

# print(12.365*23.4);
# money=100;
# money=money-10;
# money-=30;
# mon=str(money)
# print(money,"现在的金额为%.2f和%s" % (money**2,f"内嵌你输入{money+200}"))
# print(f"输出金额为{money-10}")
# type=type(money)
# print("\"现在的金额")
# stock_code="003032";
# stock_price=19.99;
# daily_grow=1.2;
# prin=f"公司:传智播客股票代码:{stock_code},当前股票票价格:{stock_price},每日系数{daily_grow},价格为{stock_price*daily_grow**7}"
# print(prin)
# print("开始输入")
# name=input("就fish覅")
# print("我的名字是%s"%name)
# num=random.randint(1,10)
# print("输入猜想的数字")
# first_guess=int(input("第一次机会"))
# if first_guess==num:
#     print("第一次就猜对了")
# elif first_guess>num:
#     print("数字猜大了")
# else:
#     print("数字猜小了")
#     secend_guess=int(input("第二次机会"))
#     if secend_guess==num:
#         print("第二次猜对了")
#     elif secend_guess>num:
#         print("猜大了")
#     else:
#         print("数字猜小了")
#         third_guess=int(input("最后一次机会"))
#         if third_guess==num:
#             print("终于猜对了")
#         else:
#             print("机会用完最后的数字是%d"%num)
# result=0;
# sum=0;
# while result<100:
#     result=result+1
#     sum=sum+result
#
# print(f"一到一百的值为{sum}")
# num = random.randint(1, 100)
# guess = 1
# count=0;
# while guess:
#     input_num = int(input("请输入数字"))
#     count=count+1
#     if input_num == num:
#         guess = 0
#         print(f"您终于猜对了{num},总共才{count}次")
#     elif input_num > num:
#         print("猜大了")
#     else:
#         print("您猜小了")
# print("李国",end="\t")
# print("尝试",end="\t")
# i=1;
#
# while i<=9:
#     j=1;
#     while j<=i:
#       print("%d\t*\t%d\t=\t%d\t"%(i,j,i*j),end="\t")
#       j+=1
#     print("\n")
#     i+=1
# s=100
# for s in range(11):
#      print(s)
#
#
# print(s)
# def static():
#     """"
#     该函数用于计算工资
#     """
#     salary = 10000;
#     count = 0;
#     for s in range(1, 21):
#         s = random.randint(1, 10)
#         if salary > 0:
#             if s < 5:
#                 print("绩效小于五为%d" % s)
#                 continue
#             elif s >= 5:
#                 count += 1
#                 salary = salary - 1000
#                 print("此时的薪资为%d" % salary)
#         else:
#             print("薪资发完，已经发了%d名员工" % count)
#             break
# static()
# money = 1000000
# money = money + 1;
# name = input("请输入姓名")
#
#
# def print_infor(name,money) :
#     print(f"{name}您好，欢迎来到atm,余额为{money}")
#     print("查询余额，请按{1}")
#     print("存款，请按{2}")
#     print("取出，请按{3}")
#     print("退出程序，请按{4}")
#
#
# def serve(num, money):
#    money+=num
#    return money
#
# def decrease(num, money):
#    money-=num
#    return money
#
# while True:
#    print_infor(name,money);
#    inf=input("请求输入操作")
#    if inf=="2":
#       money= serve(int(input("请输入存金额")),money)
#    elif inf=="3":
#       money= decrease(int(input("请输入取金额")),money)
#    elif inf=="4":
#        break
#    elif inf=="1":
#        print(f"余额为{money}")
list_test=["tom",["jerry","haven"],"海绵包"]
print(list_test[1])
print("新建3")
