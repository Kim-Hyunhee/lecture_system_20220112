from server.model import Reviews
from server import db

def write_review(params):
    sql = f"""
    INSERT INTO lecture_review 
    (lecture_id, user_id, title, content, score) 
    VALUES 
    ({params['lecture_id']}, {params['user_id']}, '{params['title']}', '{params['content']}', {params['score']})"""
    
    db.excuteOne(sql)
    return {
        'code' :200,
        'message' :'리뷰 등록이 되었습니다.'
    }