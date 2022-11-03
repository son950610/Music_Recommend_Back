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
