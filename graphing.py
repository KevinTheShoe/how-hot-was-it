import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import mplcursors

def monthOverlaid(df, month, title, xlabel, ylabel):
	sns.set_theme()
	fig, ax = plt.subplots(figsize=(16, 9))

	for year in range(2003, 2027):
		new_df = df[df['time'].str.startswith(f'{year}-{month}')]
		fig = sns.lineplot(x=new_df['time'].str[8:], y=new_df['temp'], ax=ax, label=year, linewidth=(1 if year != 2026 else 3), alpha=(0.5 if year != 2026 else 1))

	mplcursors.cursor(highlight=True)

	ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
	ax.margins(x=0)

	plt.tight_layout()
	plt.show()

def monthBoxplot(df, month, title, xlabel, ylabel):
	sns.set_theme()
	fig, ax = plt.subplots(figsize=(16, 9))

	new_df = pd.DataFrame()
	new_df['time'] = df['time'].str[:7]
	new_df['temp'] = df['temp']
	# new_df = new_df.groupby('time', as_index=False)['temp'].max()
	new_df = new_df[new_df['time'].str.endswith(f'-{month}')]
	fig = sns.boxplot(data=new_df, x='time', y='temp')

	x_dates = sorted(list(set(new_df['time'].str[:4])))
	ax.set_xticklabels(labels=x_dates, ha='right')
	ax.set(title=title, xlabel=xlabel, ylabel=ylabel)

	plt.tight_layout()
	plt.show()

def dayLineplot(df, day, title, xlabel, ylabel):
	sns.set_theme()
	fig, ax = plt.subplots(figsize=(16, 9))

	new_df = df[df['time'].str.endswith(day)]
	fig = sns.lineplot(x=new_df['time'], y=new_df['temp'], ax=ax)

	x_dates = sorted(list(set(new_df['time'])))
	ax.set_xticklabels(labels=x_dates, rotation=45, ha='right')
	ax.set(title=title, xlabel=xlabel, ylabel=ylabel)

	plt.tight_layout()
	plt.show()