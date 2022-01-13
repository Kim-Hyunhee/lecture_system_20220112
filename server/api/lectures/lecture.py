from server.api import lectures
from server.model import Lectures
from server import db

def get_all_lectures(params):
    # 모든 강의 목록을 이름순으로 내려주자 => 당장은 params 활용 X
    
    sql = f"SELECT * FROM lectures ORDER BY name"
    
    db_list = db.excuteAll(sql)
    
    lectures = [Lectures(row).get_data_object() for row in db_list]
    
    return {
        'code' : 200,
        'message' : '모든 강의 목록 조회',
        'data' :{
            'lectures' : lectures
        }    
    }
    
# 수강 신청 기능
def select_lecture(params):
       
    # 중복 불가
    
    sql = f"SELECT * FROM lecture_user WHERE lecture_id={params['lecture_id']} AND user_id={params['user_id']}"
    duple_lecture = db.excuteOne(sql)
    
    sql = f"INSERT INTO lecture_user VALUES({params['lecture_id']}, {params['user_id']})"
    db.excuteOne(sql)
        
    
    if not duple_lecture :
        return{
            
            'code' : 200,
            'message' : '수강 신청 완료'
    }
    
    
    else:
        return {
            'code' :400,
            'message' :'이미 수강 신청을 했습니다.'
        }, 400