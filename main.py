from Scrapying import scratchOnVijos
import pymysql


students_info = list()
user_sets = set()
# 得到题目的链接
L_task_urls = scratchOnVijos.get_vijos_tasks()
for urls in L_task_urls:
    # 得到提交页面的链接
    sub_url = scratchOnVijos.get_to_submit(urls)
    user_sets |= scratchOnVijos.get_user_sets(sub_url)


# 对于每个user tuple
all_users = list()
with open('msg.txt', 'w') as f:
    for users in user_sets:
        user_url = scratchOnVijos.get_per_url(users)
        msg = scratchOnVijos.load_student_data(user_url)
        # print(users, msg)
        if str(msg[1]) == '0.0':
            continue
        # f.write('用户 {} 排名{}, 解决了{}道题\n'.format(users[0], msg[2], msg[0]))
        all_users.append((users[0], msg[2], msg[0]))

pymysql.connect()
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd=None, db='mysql')
cur = conn.cursor()
cur.execute('USE scratch')


def store(content):
    sqls = "INSERT INTO vijos (name, rank, solve) VALUES (\"{}\", \"{}\", \"{}\")".format(content[0], content[1], content[2])
    print(sqls)
    cur.execute(sqls)
    cur.connection.commit()


try:
    for l in all_users:
        # print(l)
        store(l)
finally:
    cur.close()
    conn.close()


