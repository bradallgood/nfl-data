import pandas as pd  

stats_df = pd.read_csv('Stats-2022.csv')
meta_df = pd.read_csv('Metadata-2022.csv')

print('---------------------------------------------')
print(stats_df.columns)
#merged_df = stats_df.merge(meta_df[['boxscore_stats_link', 'tm_nano', 'tm_market', 'tm_name', 'tm_alias',
#       'opp_nano', 'opp_market', 'opp_name', 'opp_alias', 'tm_spread',
#       'opp_spread', 'total', 'attendance', 'duration', 'roof_type',
#       'surface_type', 'won_toss', 'won_toss_decision', 'won_toss_overtime',
#       'won_toss_overtime_decision', 'temperature', 'humidity_pct',
#       'wind_speed', 'boxscore_stats_link']])
print('---------------------------------------------')
print(meta_df.columns)
print('---------------------------------------------')
#print(merged_df.columns)


print(stats_df.head(15))