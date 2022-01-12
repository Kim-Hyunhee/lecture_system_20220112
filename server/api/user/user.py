# 로그인 / 회원가입 등, 사용자 정보 관련 기능 모아두는 모듈
# DB 연결정보 보관 변수를 import
from server.db_connector import DBConnetor
from server.model import Users

db = DBConnetor()

def login(params):
    sql = f"SELECT * FROM users WHERE email='{params['email']}' AND password='{params['pw']}'"
    
    login_user = db.excuteOne(sql)  # 있다면 인스턴스 없다면 None
    
    if login_user == None:
        return {
            'code' : 400,
            'message' : '이메일 또는 비밀번호가 잘못 되었습니다.'
        }, 400
    
    
    return {
        'code' : 200,
        'message' : '로그인 성공',
        'data' : {
            'user' : Users(login_user).get_data_object()
        }
    }
    
def sign_up(params):
    
    # 이메일이 중복이면 가입 불허 예정
    # 1. 회원 가입 시 - 중복된 이메일이면 400 처리
    # 2. GET /user
    #   => 파라미터로 email을 주면 해당 이메일이 일치하는 사용자 정보를 리턴
    #   => 같은 이메일이 없다면 400처리 (해당 사용자는 존재하지 않습니다.)
    
    sql = f"SELECT * FROM users WHERE email = '{params['email']}'"
    user_result = db.excuteOne(sql)
    if user_result :
        return {
            'code' : 400,
            'message' :'중복된 이메일이 존재합니다.'
        }, 400
    
    
    sql = f"INSERT INTO users (email, password, name) VALUES ('{params['email']}', '{params['pw']}', '{params['name']}')"
    
    db.insertAndCommit(sql)
    
    return {
        'code' : 200,
        'message' : '회원 가입 성공'
    }
    
def login_check(params):
    sql = f"SELECT * FROM users WHERE email = '{params['email']}'"

    login_user = db.excuteOne(sql)
    if login_user == None :
        return {
        'code' : 400,
        'message' :'해당 사용자는 존재하지 않습니다.'
    }, 400
        
    return {
        'code' : 200,
        'message' : '로그인 성공',
        'data' : {
            'user' : Users(login_user).get_data_object()
        }
    }