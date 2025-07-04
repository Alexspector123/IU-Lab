import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import recall_score
from sklearn.model_selection import train_test_split

# Đọc dữ liệu
df = pd.read_csv("SMSSpamCollection.csv", sep='\t', header=None, names=['label', 'message'])
df.columns = ['label', 'message']
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Chia dữ liệu
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.2, random_state=42)

# Tiền xử lý: chuyển văn bản thành ma trận số lượng từ
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

# Khởi tạo và huấn luyện mô hình MultinomialNB
clf = MultinomialNB()
clf.fit(X_train_counts, y_train)

# Dự đoán
y_pred = clf.predict(X_test_counts)

# Đánh giá recall
recall = recall_score(y_test, y_pred)
print("Recall of MultinomialNB:", recall)
