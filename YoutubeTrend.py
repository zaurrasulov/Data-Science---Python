import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#opening the file
df=pd.read_csv(r'C:\Users\Zaur\Desktop\USvideos.csv') 
#print(df)

Row, Col = df.shape # looking for the size of data
print("There are {} rows and {} columns in the file.".format(Row, Col))

df = df.drop(columns = {'video_id', 'thumbnail_link'}) # deleting the columns
# renaming the columns
df = df.rename(columns={'trending_date':'Trending_date', 'title':'Title',
                        'channel_title':'Channel_Title', 'category_id':'Category_ID',
                        'publish_time':'Publish_Time','tags':'Tags',
                        'views':'Views', 'likes':'Likes', 'dislikes': 'Dislikes',
                        'comment_count':'Comment_number', 'comments_disabled':
                            'Disabled_comments', 'ratings_disabled':"Disabled_Ratings",
                            'video_error_or_removed':'Error_or_removed video',
                            'description':'Description'})
# checking the missing values
print (df.isnull().sum().sort_values(ascending = False).to_frame('Counts'))
print('------------------------------------------------------------------')
# printing the missing values
print(df[(df.apply(lambda x: sum(x.isnull().values), axis = 1)>0)])
print('------------------------------------------------------------------')
# deleting missing values
df.dropna(inplace=True)

# count the number of each frequency of each Title
df_count1 = df.Title.value_counts().to_frame('Count')
print(df_count1)

# changing all titles to lower letter
df['Title'] = df['Title'].str.lower()

# looking for the first 4 elements of Title column
print(df.Title.head())

# plot the bar chart of top 5 most popular videos
top_5_videos = df.Title.explode().value_counts()[:5].plot.barh(color=['b','b','b','b','b'])
plt.xticks(rotation=0, horizontalalignment="center")
plt.title("Top 10 Most Popular Videos", fontweight='bold')
plt.xlabel("Number of people",fontweight = 'bold')
plt.ylabel("Title", fontweight = 'bold')
plt.show()


# open new dataframe with Title and Views columns
df2= df[['Title', 'Views']]
print(df2)
print('------------------------------------------------------------------')
# sort the values in ascending order
df2 = df2.sort_values('Views', ascending=False)[:5]
# delete the duplicated
df2 = df2.drop_duplicates()
# look for the size of new dataframe
print(df2.shape)
print('------------------------------------------------------------------')

# plot a bar chart of the most viewed videos
df2.plot.barh(x='Title', y='Views', color = 'crimson')
plt.xticks(rotation = 0, horizontalalignment = 'center')
plt.title("Top 5 Most Viewed Videos",fontweight='bold')
plt.xlabel("Number of Views", fontweight = 'bold')
plt.ylabel("Video Titles", fontweight = 'bold')
plt.show()

# Calculate the frequency of each Channel title
df_count2 = df.Channel_Title.value_counts().to_frame('count')
print(df_count2)

# plot the 5 most popular channels
top_5_channels = df.Channel_Title.explode().value_counts()[:5].plot.barh(color='seagreen')
plt.title("5 Most Popular Channels", fontweight='bold')
plt.xlabel("Number of people",fontweight = 'bold')
plt.ylabel("Channel Titles", fontweight = 'bold')
plt.show()

# plot 5 the least popular channels
least_5_channels = df.Channel_Title.explode().value_counts()[-5:].plot.barh(color='slateblue')
plt.title("5 Least Popular Channels ",fontweight='bold')
plt.xlabel("Number of people", fontweight = 'bold')
plt.ylabel("Channel Titles", fontweight = 'bold')
plt.show()

# write new csv
df.to_csv("USvideos1.csv")
