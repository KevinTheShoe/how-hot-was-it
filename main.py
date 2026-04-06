import graphing
import temps
import pandas as pd

def clean(df):
	return df[df['temp'] != -999]

def averageByMonth(df):
	new_df = pd.DataFrame()
	new_df['time'] = df['time'].str[:7]
	new_df['temp'] = df['temp']
	new_df = new_df.groupby('time', as_index=False)['temp'].mean()
	print(new_df)
	graphing.graphDates(new_df['time'], new_df['temp'])

def maxOfDay(df, day):
	new_df = df[df['time'].str.endswith(day)]
	graphing.graphDates(new_df['time'], new_df['temp'])

if __name__ == '__main__':
	df = temps.getJsonAsDF()
	df = clean(df)
	maxOfDay(df, '-04-05')
	averageByMonth(df)