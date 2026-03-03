#main.py
from account_manage import AccountManage
#establish DB connection
db_config={
    'user':'root',
    'password':'jaganMysql@123',
    'host':'localhost',
    'database':'accenturepydb',
    }
accobj=AccountManage(db_config)
#user input for acc type
acc_tp=input("Enter the account type you want to update: ")
#update account balance and store the value
updatedValues=accobj.update_account_balance(acc_tp)
#display updated values if updated
if updatedValues:
    print("Account number \t Customer Name \t Account Type \t Available Balance",'\n','='*60)
    for cust in updatedValues:
        print(cust.get_acc_no(),'\t',cust.get_cust_name(),'\t\t',cust.get_acc_type(),'\t',cust.get_acc_balance(),'\t')
else:print("no data found")
#close the connection
accobj.close()
