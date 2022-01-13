# 플라스크 자체를 로딩

from flask import Flask, request

from server.db_connector import DBConnetor

# DB 연결 정보를 관리하는 클래스 생성 => 객체를 변수에 담아두자
db = DBConnetor()

def create_app():
    app = Flask(__name__)
    
    # API 로직 함수 / 클래스 들은 create_app 함수에서만 필요함
    # 함수 내부에서 import 실행 => 순환 참조 회피 (정상 동작 유도)
    from .api.user import login, sign_up, find_user_by_email
    from .api.lectures import get_all_lectures, select_lecture, delete_lecture, write_review

    # 기본 로그인
    @app.post("/user")
    def user_post():
        # args : 쿼리 파라미터에 들어있는 데이터들 (GET / DELETE)
        # form : 폼데이터에 담겨있는 데이터들 (POST / PUT / PATCH)
        # cf) json body 첨부하는 경우도 있음.
        return login(request.form.to_dict())
    
    # 회원 가입
    @app.put("/user")
    def user_put():
        return sign_up(request.form.to_dict())
    
    # 사용자 조회
    @app.get("/user")
    def user_get():
        return find_user_by_email(request.args.to_dict())
    
    # 모든 강의 목록 조회
    @app.get("/lecture")
    def lecture_get():
        return get_all_lectures(request.args.to_dict())
    
    # 수강 신청
    @app.post("/lecture")
    def lecture_post():
        return select_lecture(request.form.to_dict())
    
    # 수강 취소
    @app.delete("/lecture")
    def lecture_delete():
        return delete_lecture(request.args.to_dict())
    
    # 리뷰 등록
    @app.post("/lecture/review")
    def review_post():
        return write_review(request.form.to_dict())
       
    return app