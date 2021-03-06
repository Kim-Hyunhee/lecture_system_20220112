
class Lectures:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.max_count = data_dict['max_count']
        self.fee = data_dict['fee']
        self.campus = data_dict['campus']
     
        
    # 리뷰 목록이 추가된다면? => 강의의 하위 데이터로 reviews : [] 를 추가해보자
    # 기본값 : None => 리뷰를 다루지 않고 싶은 경우 (ex. 전체 강의 목록 조회)도 대응    
    def get_data_object(self, reviews=None, avg_score=None):
        
        # data {  } => dict를 만드는 행위
        data = {
            'id' : self.id,
            'name' : self.name,
            'max_count' : self.max_count,
            'fee' : self.fee,
            'campus' : self.campus
        }
        
        # 만약 reviews 파라미터에 실제 데이터가 들어왔다면? => 따로 추가
        if reviews:
            # dict에는 키를 새로 지정 => 새 변수를 추가 가능
            data['reviews'] = reviews
            
            # 모든 리뷰의 평점을 가지고 평균을 구해보자
            
            # sum_score = 0
            
            # for review in reviews:
            #     sum_score += review['score']
                
            # avg_score = sum_score / len(reviews)
            
            # data['avg_score'] = avg_score
        
        if avg_score:
            data['avg_score'] = avg_score
        
        return data