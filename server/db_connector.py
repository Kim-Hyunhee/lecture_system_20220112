import pymysql
from pymysql.cursors import DictCursor

class DBConnetor:
    def __init__(self):
        self.db = pymysql.connect(
            host='finalproject.cbqjwimiu76h.ap-northeast-2.rds.amazonaws.com',
            port=3306,
            user='admin',
            passwd='Vmfhwprxm!123',  # 프로젝트!123  첫글자만 대문자로.
            db='test_202112_python',
            charset='utf8',
            cursorclass=DictCursor
        )
        
        # 커서도 변수로 담아두자
        self.cursor = self.db.cursor()
        
    # 쿼리 실행 -> 목록을 리턴하는 메쏘드
    def excuteAll(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def excuteOne(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    
    # 하나의 데이터 추가/변경/삭제 등 DB 영향 쿼리 실행 -> DB 실제 기록 (별로 좋지 않은 방법)
    # 커밋은 한 번만 하는 것이 좋다. 
    def excuteQueryAndCommit(self, sql):
        self.cursor.execute(sql)
        self.db.commit()