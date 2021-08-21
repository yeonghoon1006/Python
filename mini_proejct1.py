# -*- coding: utf-8 -*-
import sqlite3

## 데이터베이스를 연결하는 코드
# conn = sqlite3.connect ...
# c = conn.cursor()
conn = sqlite3.connect('./mini_project1.db', isolation_level=None)
c = conn.cursor()

## 상품과 주문 테이블을 생성하는 코드
# c.execute("CREATE TABLE ...

c.execute("CREATE TABLE IF NOT EXISTS material(id INTEGER PRIMARY KEY, name TEXT, price INTEGER)")
c.execute("CREATE TABLE IF NOT EXISTS orders(order_number INTEGER PRIMARY KEY AUTOINCREMENT, id INTEGER, count INTEGER)")

## 상품 데이터를 추가하는 코드
# c.execute("INSERT INTO ...

c.execute("INSERT INTO material(id,name,price) VALUES(?,?,?)",(1,'apple',2000))
c.execute("INSERT INTO material(id,name,price) VALUES(?,?,?)",(2,'banana',3000))
c.execute("INSERT INTO material(id,name,price) VALUES(?,?,?)",(3,'tomato',1500))
c.execute("INSERT INTO material(id,name,price) VALUES(?,?,?)",(4,'watermelon',5000))
c.execute("INSERT INTO material(id,name,price) VALUES(?,?,?)",(5,'cherry',500))

## 상품 목록을 표시하는 코드
c.execute("select * from material")
index = []
price = []
name = []

for row in c.fetchall():
    print("상품번호 : %s \t 상품명 : %s \t 상품가격 : %s" %(str(row[0]),str(row[1]),str(row[2])))
    index.append(row[0])
    # price.append(row[2])
    # name.append(row[1])

## 상품 번호와 주문 수량을 입력받는 코드

while True:
    print('')
    print("구매하실 상품의 번호를 입력해주세요: (더 이상 구매하실 상품이 없으면 아무것도 입력하지 말고 ENTER을 누르세요)")
    id = input()
    print('')

    if(id==''):
        break
    elif(int(id) not in index):
        print("없는 상품입니다. 다시 입력해주세요.")
        continue

    print('')
    print("구매할 수량을 입력해주세요: ")
    count = input()

## 주문 데이터를 db에 추가하는 코드
# c.execute("INSERT INTO ...
    c.execute("INSERT INTO orders(id,count) values(?,?)",(id,count))
    


## 현재까지 주문 내역을 출력하는 코드

print('')
print("현재까지 구매한 내역 보기")
print('')

c.execute("SELECT id, SUM(count) FROM orders group by id")

order_index = []
order_count = []
for row in c.fetchall():
        order_index.append(row[0])
        order_count.append(row[1])

for i in range(0,len(order_index)):
    c.execute("SELECT id, name, price from material where id=%s" % (str(order_index[i])))
    for row in c.fetchall():
        print("상품 번호 : %s \t 상품명 : %s \t 주문 개수 : %s \t\t 총 가격 : %s" %(row[0], row[1], order_count[i], row[2]*order_count[i]))


# for row in c.fetchall():
#     for i in range(0,len(index)):
#         if index[i]==row[0]:
#             print("상품 번호 : %s \t 상품명 : %s \t 주문 개수 : %s \t\t 총 가격 : %s" %(row[0], name[i], row[1], row[1]*price[i]))
# print('')
