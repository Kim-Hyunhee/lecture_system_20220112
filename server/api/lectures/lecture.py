from server.db_connector import DBConnetor
from server.model import Lectures

db = DBConnetor()

def lecture_test():
    sql = 'SELECT * FROM lectures'
    
    lecture_list = db.excuteAll(sql)
    
    lectures = [ Lectures(row).get_data_object() for row in lecture_list ]
    
    return{
        'lectures' : lectures
    }