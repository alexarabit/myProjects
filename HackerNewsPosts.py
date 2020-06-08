#In this analysis, I will be analysing how the most common way to use the platform of Hacker News. Hacker News is extremely popular in technology and startup circles, and posts that make it to the top of Hacker News' listings can get hundreds of thousands of visitors as a result. Thus, it is useful to know what types of posts are most popular.
#There are two types of posts: posts that ask questions and posts that show projects and products. We can see which type of post is more popular by seeing which one gets more comments.
#Note that this dataset has been reduced from almost 300,000 rows to approximately 20,000 rows by removing all submissions that did not receive any comments, and then randomly sampling from the remaining submissions.

import csv as c

opened_file = open('/Users/alexarabit/Downloads/hacker_news (1).csv') #found in finder and right clicked below to 'copyaspath'
read_file = c.reader(opened_file)
hn = list(read_file)


headers = hn[0]
hn = hn[1:]


asks_posts = []
show_posts = []
other_posts = []

for row in hn:
    title = row[1] #defining what I'm looking for
    hn_posts = row[0:] #defining what to put into lists(I want all the attributes)
    if title.lower().startswith('ask hn'):
        asks_posts.append(hn_posts)
    elif title.lower().startswith('show hn'):
     show_posts.append(hn_posts)
    else: other_posts.append(hn_posts)

print('average ask comments')
total_ask_comments = 0

for p in asks_posts:
    num_comments = int(p[4])
    total_ask_comments = total_ask_comments + num_comments
    avg_ask_comments = total_ask_comments / len(asks_posts)

print(avg_ask_comments)

print('\n')
print('average show comments')


total_show_comments = 0

for p in show_posts:
    num_comments = int(p[4])
    total_show_comments = total_show_comments + num_comments
    avg_show_comments = total_show_comments / len(show_posts)

print(avg_show_comments)

#On average, there are more comments on ask posts. This could be due to the nature of an ask post reaching out to others for answers, and thus more people will be prompted to comment because the post seeks comments/answers. Due to this finding, I will look more into the ask posts.
#Do ask posts at a certain time attract more attention?

import datetime as dt

result_list = [] #list with final info I need

for row in asks_posts:
    created_at = row[6]
    comments = int(row[4])
    result_list.append([created_at,comments])
    #need lists of lists so I can call the hour for each section


counts_by_hour = {}
comments_by_hour = {}
string_format = "%m/%d/%Y %H:%M"

for row in result_list:
    created_at = row[0]
    comments = int(row[1])
    date = dt.datetime.strptime(created_at, string_format) #made it into a date object
    hour = dt.datetime.strftime(date,'%H') #extracted just the hour from the object
    if hour not in counts_by_hour: #then insert it as a new key in count dic
        counts_by_hour[hour] = 1 #and insert the comments section into comments dictionairy
        comments_by_hour[hour] = comments
    else:
        counts_by_hour[hour] += 1
        comments_by_hour[hour] += comments

avg_comments_hour = []

for hour in comments_by_hour:
    avg_comments_hour.append([hour, comments_by_hour[hour]/counts_by_hour[hour]])

swap_avg_by_hour = []

for row in avg_comments_hour:
    first_element = row[1]
    second_element = row[0]
    swap_avg_by_hour.append([first_element, second_element])

sorted_swap = sorted(swap_avg_by_hour, reverse=True)

print('\n')
print('Top 5 Hours to Ask Posts Comments')

for row in sorted_swap[0:5]:
    format_string = '%H'
    time = row[1]
    dt_object = dt.datetime.strptime(time, format_string) #made it an object
    hour = dt.datetime.strftime(dt_object, '%H') #took out specifically the hour in the objcet
    print(hour)