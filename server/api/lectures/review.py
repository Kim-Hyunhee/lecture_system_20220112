from server.model import Reviews
from server import db

def write_review(params):
    
    # 중복 불가
    sql = f"SELECT * FROM lecture_review WHERE lecture_id={params['lecture_id']} AND user_id={params['user_id']}"
    # 점수 1~5 사이
    # 제목 5자 이상
    # 내용 10자 이상
    sql = f"""
    INSERT INTO lecture_review 
    (lecture_id, user_id, title, content, score) 
    VALUES 
    ({params['lecture_id']}, {params['user_id']}, '{params['title']}', '{params['content']}', {params['score']})"""
    
    db.insertAndCommit(sql)
    return {
        'code' :200,
        'message' :'리뷰 등록이 되었습니다.'
    }