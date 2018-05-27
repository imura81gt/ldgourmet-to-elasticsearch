# coding: utf-8
import digdag
import pandas as pd

class Convert(object):
    def __init__( self):
        pass

    def transform( self, session_time = None, query_result = '0'):
        csv1 = pd.read_csv(digdag.env.params['csv_restaurants'])
        csv2 = pd.read_csv(digdag.env.params['csv_stations'])

        csv1 = csv1.rename(
            columns={
                'station_id1':   'id_station1',
                'station_id2':   'id_station2',
                'station_id3':   'id_station3',
                'station_time1': 'time_station1',
                'station_time2': 'time_station2',
                'station_time3': 'time_station3',
                'station_distance1': 'distance_station1',
                'station_distance2': 'distance_station2',
                'station_distance3': 'distance_station3',
                'category_id1':  'id_category1',
                'category_id2':  'id_category2',
                'category_id3':  'id_category3',
                'category_id4':  'id_category4',
                'category_id5':  'id_category5',
            }
        )

        combined = pd.merge(
            csv1,
            csv2,
            how ='left',
            left_on = ['id_station1'],
            right_on = ['id'],
            suffixes = ('', '_station1')
        )
        combined = pd.merge(
            combined,
            csv2,
            how ='left',
            left_on = ['id_station2'],
            right_on = ['id'],
            suffixes = ('', '_station2')
        )
        combined = pd.merge(
            combined,
            csv2,
            how ='left',
            left_on = ['id_station3'],
            right_on = ['id'],
            suffixes = ('', '_station3')
        )
        combined.to_csv(
            digdag.env.params['output_csv'],
            index = False,
            encoding = "utf-8"
        )

