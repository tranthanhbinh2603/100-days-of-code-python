#https://replit.com/@Tran-ThanhThanh/day-30-2-exercise#main.py
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
  try:
    if post['Likes'] != 0:
      total_likes = total_likes + post['Likes']
  except:
    pass


print(total_likes)