import pandas as pd  

final_df = pd.DataFrame()

stats_df = pd.read_csv('Stats-2022.csv')

cols = stats_df.columns

column_string = '{'
for co in cols:
    if co not in ['season','event_date','nano','market','name','alias']:
        column_string = f'{column_string}  "opp_{co}":[opp_{co}],'
for co in cols:
    if co not in ['season','event_date','nano','market','name','alias']:
        column_string = f'{column_string}  "tm_{co}":[tm_{co}],'
column_string = column_string + '}'
print (column_string)

        
boxscore_stats_link_val = ''

for row in stats_df.iterrows():
    if boxscore_stats_link_val != row[1]['boxscore_stats_link']:
        opp_name = row[1][5]
        opp_rush_att = row[1][6]
        opp_rush_yds= row[1][7]
        opp_rush_tds= row[1][8]
        opp_pass_cmp= row[1][9]
        opp_pass_att= row[1][10]
        opp_pass_cmp_pct= row[1][11]
        opp_pass_yds= row[1][12]
        opp_pass_tds= row[1][13]
        opp_pass_int= row[1][14]
        opp_passer_rating= row[1][15]
        opp_net_pass_yds= row[1][16]
        opp_total_yds= row[1][17]
        opp_times_sacked= row[1][18]
        opp_yds_sacked_for= row[1][19]
        opp_fumbles= row[1][20]
        opp_fumbles_lost= row[1][21]
        opp_turnovers= row[1][22]
        opp_penalties= row[1][23]
        opp_penalty_yds= row[1][24]
        opp_first_downs= row[1][25]
        opp_third_down_conv= row[1][26]
        opp_third_down_att= row[1][27]
        opp_third_down_conv_pct= row[1][28]
        opp_fourth_down_conv= row[1][29]
        opp_fourth_down_att= row[1][30]
        opp_fourth_down_conv_pct= row[1][31]
        opp_time_of_possession= row[1][32]
        boxscore_stats_link_val = row[1][33]
    else:
        tm_rush_att = row[1][6]
        tm_rush_yds= row[1][7]
        tm_rush_tds= row[1][8]
        tm_pass_cmp= row[1][9]
        tm_pass_att= row[1][10]
        tm_pass_cmp_pct= row[1][12]
        tm_pass_yds= row[1][12]
        tm_pass_tds= row[1][13]
        tm_pass_int= row[1][14]
        tm_passer_rating= row[1][15]
        tm_net_pass_yds= row[1][16]
        tm_total_yds= row[1][17]
        tm_times_sacked= row[1][18]
        tm_yds_sacked_for= row[1][19]
        tm_fumbles= row[1][20]
        tm_fumbles_lost= row[1][21]
        tm_turnovers= row[1][22]
        tm_penalties= row[1][23]
        tm_penalty_yds= row[1][24]
        tm_first_downs= row[1][25]
        tm_third_down_conv= row[1][26]
        tm_third_down_att= row[1][27]
        tm_third_down_conv_pct= row[1][28]
        tm_fourth_down_conv= row[1][29]
        tm_fourth_down_att= row[1][30]
        tm_fourth_down_conv_pct= row[1][31]
        tm_time_of_possession= row[1][32]
        boxsore_stats_link = row[1][33]
        #print('-----------------------------------------')
        tm_name = row[1][4]
        #print(f'Away: {opp_name} {opp_total_yds} Home: {tm_name} {tm_total_yds}')
        tm_boxscore_stats_link_val = row[1][33]
        new_df = pd.DataFrame
        new_df = pd.DataFrame({  "opp_name":[opp_name],  "opp_rush_att":[opp_rush_att],  "opp_rush_yds":[opp_rush_yds],  
                               "opp_rush_tds":[opp_rush_tds],  "opp_pass_cmp":[opp_pass_cmp],  
                               "opp_pass_att":[opp_pass_att],  "opp_pass_cmp_pct":[opp_pass_cmp_pct],  
                               "opp_pass_yds":[opp_pass_yds],  "opp_pass_tds":[opp_pass_tds],  
                               "opp_pass_int":[opp_pass_int],  "opp_passer_rating":[opp_passer_rating], 
                               "opp_net_pass_yds":[opp_net_pass_yds],  "opp_total_yds":[opp_total_yds],  
                               "opp_times_sacked":[opp_times_sacked],  "opp_yds_sacked_for":[opp_yds_sacked_for],  
                               "opp_fumbles":[opp_fumbles],  "opp_fumbles_lost":[opp_fumbles_lost],  
                               "opp_turnovers":[opp_turnovers],  "opp_penalties":[opp_penalties],  
                               "opp_penalty_yds":[opp_penalty_yds],  "opp_first_downs":[opp_first_downs],  
                               "opp_third_down_conv":[opp_third_down_conv],  "opp_third_down_att":[opp_third_down_att],  
                               "opp_third_down_conv_pct":[opp_third_down_conv_pct],  "opp_fourth_down_conv":[opp_fourth_down_conv],  
                               "opp_fourth_down_att":[opp_fourth_down_att],  "opp_fourth_down_conv_pct":[opp_fourth_down_conv_pct],  
                               "opp_time_of_possession":[opp_time_of_possession],
                               "tm_name":[tm_name], "tm_rush_att":[tm_rush_att],  "tm_rush_yds":[tm_rush_yds],  "tm_rush_tds":[tm_rush_tds],  
                               "tm_pass_cmp":[tm_pass_cmp],  "tm_pass_att":[tm_pass_att],  "tm_pass_cmp_pct":[tm_pass_cmp_pct],  
                               "tm_pass_yds":[tm_pass_yds],  "tm_pass_tds":[tm_pass_tds],  "tm_pass_int":[tm_pass_int], 
                               "tm_passer_rating":[tm_passer_rating],  "tm_net_pass_yds":[tm_net_pass_yds],  
                               "tm_total_yds":[tm_total_yds],  "tm_times_sacked":[tm_times_sacked],  
                               "tm_yds_sacked_for":[tm_yds_sacked_for],  "tm_fumbles":[tm_fumbles],  
                               "tm_fumbles_lost":[tm_fumbles_lost],  "tm_turnovers":[tm_turnovers],  
                               "tm_penalties":[tm_penalties],  "tm_penalty_yds":[tm_penalty_yds], 
                               "tm_first_downs":[tm_first_downs],  "tm_third_down_conv":[tm_third_down_conv],
                               "tm_third_down_att":[tm_third_down_att],  "tm_third_down_conv_pct":[tm_third_down_conv_pct],  
                               "tm_fourth_down_conv":[tm_fourth_down_conv],  "tm_fourth_down_att":[tm_fourth_down_att],  
                               "tm_fourth_down_conv_pct":[tm_fourth_down_conv_pct],  
                               "tm_time_of_possession":[tm_time_of_possession],  
                               "boxscore_stats_link":[tm_boxscore_stats_link_val],})
        final_df = final_df.append(new_df, ignore_index=True)


meta_df = pd.read_csv('Metadata-2022.csv')
merged_df = pd.merge(final_df, meta_df, on='boxscore_stats_link')

pd.set_option('display.max_columns', 500)
pd.set_option('max_colwidth', None)
pd.set_option('display.max_rows', None)

season_df = pd.read_csv('Season-2022.csv')
ff_df = pd.merge(merged_df, season_df, on='boxscore_stats_link')

print(ff_df[['season_y','season_x','event_date_y','week','opp_name','opp_score','tm_name','tm_score']].to_string(index=False))

cols = ff_df.columns
for col in cols:
    if col.find("_x") != -1:
        print(f'{col} : {col.find("_x")}')

