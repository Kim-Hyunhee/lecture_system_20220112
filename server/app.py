# 플라스크 자체를 로딩

from flask import Flask, request
from server.api.user.user import login_check

from server.db_connector import DBConnetor

from .api.user import login, sign_up
from .api.lectures import lecture_test

# DB 연결 정보를 관리하는 클래스 생성 => 객체를 변수에 담아두자
# db = DBConnetor()

def create_app():
    app = Flask(__name__)
    
    # 기본 로그인
    @app.post("/user")
    def user_post():
        # args : 쿼리 파라미터에 들어있는 데이터들
        # form : 폼데이터에 담겨있는 데이터들
        return login(request.form.to_dict())
    
    # 회원 가입
    @app.put("/user")
    def user_put():
        return sign_up(request.form.to_dict())
    
    @app.post("/lecture")
    def lecture_post():
        return lecture_test()
    
    @app.get("/user")
    def email_result_get():
        return login_check(request.args.to_dict())
       
    return app