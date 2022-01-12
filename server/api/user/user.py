# 로그인 / 회원가입 등 사용자 정보 관련 기능 모아두는 모듈
# DB 연결 정보 보관 변수를 import
from server.db_connector import DBConnetor

db = DBConnetor()

def test():
    
    # DB의 모든 users 조회 쿼리
    sql = f"SELECT * FROM users;"
    db.cursor.execute(sql)
    all_list = db.cursor.fetchall()
    
    print(all_list)    
    
    return {
        '임시' :'임시'
    }