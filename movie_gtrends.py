import pandas
from pytrends.request import TrendReq

movies = set()

# Login to Google. Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq(hl='en-US', tz=360)

# Get Google Top Charts

# months in 2015
for m in range(201501, 201513):

    top_charts_df = pytrend.top_charts(cid='films', date=m)

    for i, ele in enumerate(top_charts_df['title']):
        movies.add(ele)

# months in 2016
for m in range(201601, 201613):

    top_charts_df = pytrend.top_charts(cid='films', date=m)

    for i, ele in enumerate(top_charts_df['title']):
        movies.add(ele)


# months in 2017
for m in range(201701, 201712):

    top_charts_df = pytrend.top_charts(cid='films', date=m)

    for i, ele in enumerate(top_charts_df['title']):
        movies.add(ele)

print(len(movies))
print(movies)
