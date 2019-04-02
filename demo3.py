import os;
import MySQLdb;
#读取指定文件夹内的文件内容
def get_txt():
    dir="e:/xiaoshuo/";
    print(os.walk(dir));
    list = {};
    for root,dirs,files in os.walk(dir):
        # print(root)
        # print(dirs);
        # print(files);
        list = files;
    print(list);
    return list,dir,;
#解析数据
def amaz_content(list,dir):

    # 判断list是否为空
    if len(list):
        try:
            # 遍历循环list
            for name in list:
                # 打开文件
                with open(dir + name, "r") as f:
                    # 读取文件内容并打印
                    str = f.read();
                    print(name)
                    print(str);
                    print()
                f.close();
        except Exception as error:
            print(error);

#插入数据数据
def insert_mysql():
    # try:
        conn = MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='root',db='python',charset='utf8')
        cursor = conn.cursor();
        print(conn);
        print(cursor);
        #创建表
        cursor.execute("create table if not exists python_book(id int(11) primary  key ,book_name varchar(20) ,content text )")


        list,dir =  get_txt();
        if len(list):
            try:
                # 遍历循环list
                for name in list:
                    # 打开文件
                    with open(dir + name, "r") as f:
                        # 读取文件内容并打印
                        str = f.read();
                        print(name)
                        print(str);
                        print()
                        # 插入数据
                        sql = "insert into python_book(book_name,content)values ('"+name+"','"+str+"')";
                        print(sql)
                        cursor.execute(sql);
                    f.close();
            except Exception as error:
                print(error);


        #自动提交
        conn.commit()
        #关闭实例
        cursor.close();
        #关闭连接
        conn.close();
    # except Exception as error:
    #     print(error)

if __name__ == '__main__':
    get_txt();
    insert_mysql();