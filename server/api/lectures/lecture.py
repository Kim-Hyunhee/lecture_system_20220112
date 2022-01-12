from server.db_connector import DBConnetor

db = DBConnetor()

def lecture_test():
    sql = 'SELECT * FROM lectures'
    
    db.cursor.execute(sql)
    letcture_list = db.cursor.fetchall()
    
    print(letcture_list)
    return{
        '임시' :'임시'
    }