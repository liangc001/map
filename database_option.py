from pickle import NONE
import sqlite3

#判断是否存在此用户名(ps:传入字符串作为用户名，返回0/1（int）)
def check_user_name(user_id_now):
    dbpath = "My.db"   
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    sql = "SELECT 1 FROM user_mes WHERE id='%s' LIMIT 1"%(user_id_now)
    cur.execute(sql)
    data = cur.fetchone()
    conn.commit()
    conn.close()
    if data == None:
        return int(0)
    else:
        return int(1)

#返回一个包含当前用户名对应密码的元组(ps:传入形参为一个字符串)
#如果不存在此用户则返回0
def search_user_pass(user_id_now,user_key_now):
    if check_user_name(user_id_now)==0:
         return int(0)
    dbpath = "My.db"   
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    sql = "SELECT key_ from user_mes where id='%s'" %(user_id_now)
    cur.execute(sql)
    data = cur.fetchone()
    conn.commit()
    conn.close()
    data2 = (user_id_now,)
    data3=data+data2
    return data3

#若已存在返回0
#用户注册并将信息放入用户账户表中
def save_data_user(id_now,key_now):
    if check_user_name(id_now)==1:
        return int(0)
    else:
        conn = sqlite3.connect("My.db")
        cur = conn.cursor()
        sql = "insert INTO user_mes (id,key_) VALUES('%s','%s')" % (id_now,key_now)
        cur.execute(sql)
        conn.commit()
        conn.close()

#用户上传道路信息并储存(传入四个字符串分别为起点终点方向距离)
def save_data_road_user(be_now,en_now,dir_now,dis_now):
    conn = sqlite3.connect("My.db")
    cur = conn.cursor()
    sql = "insert INTO mes_road_user (begin_,end_,direction,distance) VALUES('%s','%s','%s',%d)" % (be_now,en_now,dir_now,dis_now)
    cur.execute(sql)
    conn.commit()
    conn.close()
    

#管理员查看用户上传的道路信息(ps:调用即可返回包含用户上传道路信息的二维元组并清空用户上传道路信息表)
def manager_check_user_road_mes():
    conn = sqlite3.connect("My.db")
    cur = conn.cursor()
    sql = "select * from mes_road_user"
    cur.execute(sql)
    data = cur.fetchall()
    sql2 = "delete from mes_road_user"
    cur.execute(sql2)
    conn.commit()
    conn.close()
    return data

#管理员储存道路
def save_data_road_manager(be_now,en_now,dir_now,dis_now):
    conn = sqlite3.connect("My.db")
    cur = conn.cursor()
    sql = "insert INTO mes_road_manager (begin_,end_,direction,distance) VALUES('%s','%s','%s',%d)" % (be_now,en_now,dir_now,dis_now)
    cur.execute(sql)
    conn.commit()
    conn.close()

#正式使用时地图调取manager_road表中的文件(ps:返回二维元组)
def read_manager_road():
    dbpath = "My.db"   
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    sql = "select * from mes_road_manager"
    cur.execute(sql)
    data = cur.fetchall()
    conn.commit()
    conn.close()
    return data

def change_key(user_name,test_key,now_key):
    dbpath = "My.db"   
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    sql = "SELECT key_ from user_mes where id='%s'" %(user_name)
    cur.execute(sql)
    data = cur.fetchone()
    if(data[0]!=test_key):
        return 0
    sql1 = "update user_mes set key_ = '%s' where id='%s'"%(now_key,user_name)
    cur.execute(sql1)
    conn.commit()
    conn.close()
    return 1
    
#创建数据库中的表(如果不存在这个表)
def create_table():
    conn = sqlite3.connect("My.db")
    c = conn.cursor()
#最终储存的道路信息
    sql = '''
        create table if not exists mes_road_manager(
                begin_ varchar(255),
                end_ varchar(255),
                direction varchar(255),
                distance int
            );      
    '''
    c.execute(sql)
#用户上传的道路信息
    sql1 = '''
        create table if not exists mes_road_user(
                begin_ varchar(255),
                end_ varchar(255),
                direction varchar(255),
                distance int
            );      
    '''
    c.execute(sql1)
#用户账号信息
    sql2 = '''
        create table if not exists user_mes(
                id varchar(255),
                key_ varchar(255)
            );
    '''
    c.execute(sql2)
#管理员账号信息
    sql3 = '''
        create table if not exists manager_mes(
                id varchar(255),
                key_ varchar(255)
            );
    '''
    c.execute(sql3)
    conn.commit()
    conn.close()    

