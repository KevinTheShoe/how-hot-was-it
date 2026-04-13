import graphing
import temps
import pandas as pd


if __name__ == '__main__':
	df = temps.getData()
	graphing.monthOverlaid(df, '03', 'tMax', 'Month of March Daily High Temps Overlaid', 'Day of March', 'High Temp (Fahrenheit)')
	graphing.monthBoxplot(df, '03', 'tMax', 'Month of March High Temp Distributions Per Year', 'Year', 'High Temp (Fahrenheit)')
	graphing.dayLineplot(df, '03-19', 'tMax', 'High Temp For March 19th of Each Year', 'Day', 'High Temp (Fahrenheit)')