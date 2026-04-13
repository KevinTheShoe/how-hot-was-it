import graphing
import temps
import pandas as pd

def clean(df):
	return df[df['temp'] > -50]

if __name__ == '__main__':
	df = temps.getJsonAsDF()
	df = clean(df)
	graphing.monthOverlaid(df, '03')
	graphing.monthBoxplot(df, '03')
	graphing.dayLineplot(df, '03-19')