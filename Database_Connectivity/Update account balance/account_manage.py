import mysql.connector
from customer import customer

class AccountManage:
    def __init__(self,db_config):
        self.conn=mysql.connector.connect(**db_config)

    def update_account_balance(self,acc_type):
        cursor=self.conn.cursor()
        query=f'''
        SELECT acc_no,cust_name,acc_type, acc_balance
        FROM customer
        WHERE acc_type=%s
        '''
        cursor.execute(query,[acc_type,])
        records=cursor.fetchall()

        result_list=[]
        if not records:
            return result_list
        
        #updatation logic
        for rec in records:
            acc_no,cust_name,acc_type, acc_balance=rec
            if acc_type.lower()=="savings":
                if acc_balance>15000:
                    acc_balance+=acc_balance*0.07
                else:
                    acc_balance+=acc_balance*0.05
            elif acc_type.lower() == "current":
                if acc_balance > 15000:
                    new_balance = acc_balance + (acc_balance * 0.06)
                else:
                    new_balance = acc_balance + (acc_balance * 0.04)
            #updated value assignment
            query='''
            UPDATE customer
            SET acc_balance=%s
            WHERE acc_no=%s
            '''
            cursor.execute(query,(acc_balance,acc_no))
            result_list.append(customer(acc_no,cust_name,acc_type, acc_balance))
        return result_list
    def close(self):
        self.conn.close()
