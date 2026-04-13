import graphing
import temps
import pandas as pd


if __name__ == '__main__':
	bld_df = temps.getData('bld01', True)
	all_df = temps.getAllStationDataCSV().groupby('time', as_index=False)['tMax'].mean()

	graphing.monthBoxplot(bld_df, '03', 'tMax', 'Month of March Boulder High Temp Distributions Per Year', 'Year', 'High Temp (Fahrenheit)')
	graphing.monthOverlaid(bld_df, '03', 'tMax', 'Month of March Boulder Daily High Temps Overlaid', 'Day of March', 'High Temp (Fahrenheit)')

	graphing.monthBoxplot(all_df, '03', 'tMax', 'Month of March Colorado Average High Temp Distributions Per Year', 'Year', 'High Temp (Fahrenheit)')
	graphing.monthOverlaid(all_df, '03', 'tMax', 'Month of March Colorado Average Daily High Temps Overlaid', 'Day of March', 'High Temp (Fahrenheit)')

	# graphing.dayLineplot(df, '03-19', 'tMax', 'High Temp For March 19th of Each Year', 'Day', 'High Temp (Fahrenheit)')