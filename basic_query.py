import pymysql

#######################
## DB 데이터 가져오기 ##
######################

conn = pymysql.connect(host='localhost', user='root', password="rlacodms2ek.", db="world", charset="utf8")
curs = conn.cursor(pymysql.cursors.DictCursor)
sql = "select * from user where region =%s"  #region이 조건 스트링에 해당하면, user로부터 모든 변수 가져오기
curs.execute(sql, '대전')
rows = curs.fetchall()
print(rows)

for row in rows :
    print(row)
    print(row['no'], row['id'], row['name'])  #dictionary형태 key값 이용



########################
## 테이블에 데이터 추가 ##
#######################

conn = pymysql.connect(host='localhost', user='root', password="rlacodms2ek.", db="world", charset="utf8")
curs = conn.cursor()
sql = """insert into user(id, name, region, insdt)
        values(%s, %s, %s, now())"""

curs.execute(sql, ('test10', '테스트10', '울산'))
curs.execute(sql, ('test11', '테스트11', '부산'))
curs.execute(sql, ('test12', '테스트12', '대구'))

conn.commit()

sql2 = "select * from user order by no"
curs.execute(sql2)
rows = curs.fetchall()
print(rows)
conn.close()
exit()



#################
## 수정 쿼리문 ##
################

conn = pymysql.connect(host='localhost', user='root', password="rlacodms2ek.", db="world", charset="utf8")
curs = conn.cursor()
sql = """update user set region='서울특별시' where region='서울'"""
curs.execute(sql)
conn.commit()

sql2 = "select * from user order by no"
curs.execute(sql2)
rows = curs.fetchall()
print(rows)
conn.close()
exit()



#################
## 삭제 쿼리문 ##
################

conn = pymysql.connect(host='localhost', user='root', password="rlacodms2ek.", db="world", charset="utf8")
curs = conn.cursor()
sql = """delete from user where region=%s"""
curs.execute(sql,'광주')
conn.commit()

sql2 = "select * from user order by no"
curs.execute(sql2)
rows = curs.fetchall()
print(rows)
conn.close()
exit()



#################
## DB 닫아주기 ##
################

conn = pymysql.connect(host='localhost', user='root', password="rlacodms2ek.", db="world", charset="utf8")
try:
    curs = conn.cursor()
    sql = """delete from user where region=%s"""
    curs.execute(sql,'광주')
    conn.commit()

    sql2 = "select * from user order by no"
    curs.execute(sql2)
    rows = curs.fetchall()
    print(rows)
finally:
    conn.close()