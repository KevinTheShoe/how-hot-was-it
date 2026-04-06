import graphing
import temps

if __name__ == '__main__':
	df = temps.getJsonAsDF()
	df_filtered = df[df['time'].str.endswith('-04-05')]
	df_filtered = df_filtered[df_filtered['temp'] != -999]
	print(df_filtered)
	graphing.graphDates(df_filtered['time'], df_filtered['temp'])