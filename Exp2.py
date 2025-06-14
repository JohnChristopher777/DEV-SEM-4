import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

data = {
    'label': ['ham', 'spam', 'ham', 'spam', 'ham', 'spam'],
    'message': [
        "Hey, how are you doing?",
        "Congratulations! You've won a $1000 Walmart gift card. Go to http://bit.ly/12345",
        "I'll call you later, got stuck in traffic.",
        "URGENT! Your mobile number has been selected for a $5000 prize. Reply now!",
        "Are we still meeting for dinner tonight?",
        "You have been selected for a free entry in our contest. Text WIN to 12345."
    ]
}

df = pd.DataFrame(data)
df['message_length'] = df['message'].apply(len)

print(df.head())
print(df.info())

sns.countplot(x='label', data=df)
plt.title('Distribution of Spam vs Ham')
plt.show()

plt.figure(figsize=(10,5))
sns.histplot(data=df, x='message_length', hue='label', bins=10, kde=True)
plt.title('Histogram of Message Lengths by Label')
plt.show()

spam_messages = df[df['label'] == 'spam']['message']
ham_messages = df[df['label'] == 'ham']['message']

def plot_wordcloud(text, title):
    wordcloud = WordCloud(width=800, height=400, background_color='white',
                          stopwords=set(WordCloud().stopwords)).generate(" ".join(text))
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.show()

plot_wordcloud(spam_messages, 'Word Cloud for Spam Messages')
plot_wordcloud(ham_messages, 'Word Cloud for Ham Messages')

print(df.groupby('label')['message_length'].describe())
