#question4:
    # Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
    # D 100
    # W 200
trans=int(input())#trans is the number of transations 
Overal=0
while trans!=0:
    wdet, d_w=input().split(',')#wdet is to determine whether it's a deposit or withdrawal 
    d_w=int(d_w)     #d_w is the amount of money deposited or withdrawn
    wdet=int(wdet)
    if wdet=='D':
        Overal+=d_w
    elif wdet=='W':
        Overal-=d_w
    else:
        trans-=1
print(Overal)
