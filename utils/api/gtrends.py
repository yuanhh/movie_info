from __future__ import absolute_import
from __future__ import print_function

import pandas
from pytrends.request import TrendReq

class Gtrend:
	def __init__(self):
		self.api = TrendReq(hl = 'en-US', tz = 360)

	def top(self, **kwargs):
		# var
		movies = set()

		for date in range(kwargs['begin'], kwargs['end']):
			top_charts_df = self.api.top_charts(cid = 'films', date = date)
			
			for i, ele in enumerate(top_charts_df['title']):
				movies.add(ele)

		return movies			
