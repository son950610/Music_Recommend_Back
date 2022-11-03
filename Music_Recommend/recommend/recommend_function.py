import sys
import os
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Music_Recommend.settings')
django.setup()

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

from songs.models import Song

# DB에서 데이터 가져오기
data = pd.DataFrame(list(Song.objects.values()))


# lyrics에 대해서 tf-idf(Term Frequency - Inverse Document Frequency) 수행
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(data['lyrics'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)      # 코사인 유사도 계산
indices = pd.Series(data.index, index=data['title']).drop_duplicates()      # 노래 타이틀과 인덱스 받아오기


# 추천기능 함수 생성
def get_recommendations(idx, cosine_sim=cosine_sim):    
    sim_scores = list(enumerate(cosine_sim[int(idx)]))        # 모든 노래에 대해 해당 노래와의 유사도를 연산
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)    # 유사도에 따라 노래들을 정렬
    sim_list = sim_scores[1:21]                           # 가장 유사한 20개 노래의 인덱스와 score를 받아옵니다.
    new_list = []
    for i in sim_list:
        new_dict = dict()
        new_dict['pk'] = i[0]
        new_dict["title"] = data['title'].iloc[i[0]]
        new_dict["singer"] = data['singer'].iloc[i[0]]
        new_dict["image"] = data['image'].iloc[i[0]]
        new_list.append(new_dict)
    return new_list


# # 테스트
# x = int(input("입력하세요:"))
# result = get_recommendations(x)
# print(result)