import graphing
import temps
import pandas as pd


if __name__ == '__main__':
	ftc_df = temps.getDataCSV('ftc01', False)
	bld_df = temps.getData('bld01', True)
	
	graphing.monthOverlaid(ftc_df, '03', 'tMax', 'Month of March Fort Collins Daily High Temps Overlaid', 'Day of March', 'High Temp (Fahrenheit)')
	graphing.monthBoxplot(bld_df, '03', 'tMax', 'Month of March Boulder High Temp Distributions Per Year', 'Year', 'High Temp (Fahrenheit)')
	# graphing.dayLineplot(df, '03-19', 'tMax', 'High Temp For March 19th of Each Year', 'Day', 'High Temp (Fahrenheit)')
	graphing.monthOverlaid(bld_df, '03', 'tMax', 'Month of March Boulder Daily High Temps Overlaid', 'Day of March', 'High Temp (Fahrenheit)')