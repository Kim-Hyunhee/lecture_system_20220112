from server import db

# 강의의 리뷰에 대한 기능만 모아두는 별도의 파이썬 파일

def write_review(params):
 
    # 파라미터가 제대로 들어오는가? 검증 
    # 1. 평점을 1~5 사이로만 가능
    
    score = float(params['score'])  # 파라미터들은 기본적으로 str 형태로 들어옴 -> float로 변환해두고 사용
    
    if not (1 <= score and score <= 5) :
        return {
            'code' : 400,
            'message' : '평점은 1~5점 사이만 가능합니다.'
        }, 400
    
    # 2. 제목의 길이는 최소 5자 이상 -> srt의 길이 파라미터 자체의 길이 체크
    if len(params['title']) < 5:
        return {
            'code' : 400,
            'message' : '제목은 최소 5자 이상이어야 합니다.'
        }, 400
    
    # 3. 내용의 길이는 최소 10자 이상
    if len(params['content']) < 10:
        return {
            'code' : 400,
            'message' : '내용은 최소 10자 이상이어야 합니다.'
        }, 400
       
    # DB 내부 조회 결과 활용
    # 4. 수강을 했어야만 리뷰 작성 가능
    
    sql = f"SELECT * FROM lecture_user WHERE lecture_id={params['lecture_id']} AND user_id={params['user_id']}"
    
    query_result = db.excuteOne(sql)
    
    if not query_result:
        # 수강을 하지 않은 사람이 리뷰 등록
        return {
            'code' : 400,
            'message' : '수강을 한 인원만 리뷰 작성이 가능합니다.'
        }, 400
        
    # 5. 이미 리뷰를 등록했다면 추가 등록 불가
    
    sql = f"SELECT * FROM lecture_review WHERE lecture_id={params['lecture_id']} AND user_id={params['user_id']}"
    
    already_review_data = db.excuteOne(sql)
    
    if already_review_data :
        return {
            'code' : 400,
            'message' : '이미 리뷰를 등록한 강의입니다.'
        }, 400
    
    # 리뷰실제 등록
    
    sql = f"""
    INSERT INTO lecture_review
    (lecture_id, user_id, title, content, score)
    VALUES
    ({params['lecture_id']}, {params['user_id']}, '{params['title']}', '{params['content']}', {score})
    """
    
    db.insertAndCommit(sql)
    
    return{
        'code' : 200,
        'message' : '리뷰 등록에 성공했습니다.'
    }

# 특정 학목을 지정해서 해당 항목만 수정
def modify_review(params):
    
    # 파라미터 정리
    # field : 어느 학목을 바꿀지 알려주는 역할
    # value : 해당 항목에 실제로 넣어줄 값
    # user_id : 변경을 시도하느 ㄴ사람이 누구인지? 고유 번호
    # review_id : 변경해 줄 리뷰의 id
    
    # field라는 이름표로 어느 항목을 바꾸고 싶은지? 받아오자
    columm_name = params['field']
    
    # 제목 변경?
    
    if columm_name == 'title':
        sql = f"UPDATE lecture_review SET title='{params['value']}' WHERE id={params['review_id']}"
        
        # DB에 변경 발생 -> 쿼리 실행 / commit
        db.cursor.execute(sql)
        db.db.commit()
        
        # 제목 변경 성공 리턴
        return {
            'code' : 200,
            'message' : '제목을 수정했습니다'
        }
        
    # 내용 변경
    
    if columm_name == 'content':
        sql = f""
        
        db.cursor.execute(sql)
        db.db.commit()
        
        return {
            'code' : 200,
            'message' : '내용을 수정했습니다.'
        }
        
    # 점수 변경
    if columm_name == 'score':
        sql = f""
        
        db.cursor.execute(sql)
        db.db.commit()
        
        return {
            'code' : 200,
            'message' : '점수를 수정했습니다.'
        }
    
    
    # 여기까지 내려왔다? field 파라미터에 잘못된 값이 들어갔으므로 -> 수정 분기로 들어가지 않았다.
    return {
        'code': 400,
        'message' :'field에 잘못된 값이 입력되었습니다.'
    }, 400