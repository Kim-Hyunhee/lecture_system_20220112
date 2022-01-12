# 로그인 / 회원가입 등, 사용자 정보 관련 기능 모아두는 모듈
# DB 연결정보 보관 변수를 import
from server.db_connector import DBConnetor
from server.model import Users

db = DBConnetor()

def test():
    
    # DB의 모든 users 조회 쿼리.
    sql = "SELECT * FROM users"
    all_list = db.excuteAll(sql)
    
    
    # 목록 for -> 한 줄 row로 추출 -> 추출된 row로 모델 클래스로 가공 / dict로 재가공을 한줄로 마무리
    
    # python for문을 list를 돌 때 => comprehension
    all_users = [ Users(row).get_data_object() for row in all_list ]


    return {
        'users': all_users
    } 