import graphing
import temps
import pandas as pd

def clean(df):
	return df[df['temp'] > -50]

if __name__ == '__main__':
	df = temps.getJsonAsDF()
	df = clean(df)
	graphing.monthOverlaid(df, '03', 'Month of March Daily High Temps Overlaid', 'Day of March', 'High Temp (Fahrenheit)')
	graphing.monthBoxplot(df, '03', 'Month of March High Temp Distributions Per Year', 'Year', 'High Temp (Fahrenheit)')
	graphing.dayLineplot(df, '03-19', 'High Temp For March 19th of Each Year', 'Day', 'High Temp (Fahrenheit)')