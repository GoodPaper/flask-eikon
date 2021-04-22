import sys, os, json
cfg = json.load(
    fp = open( os.path.join( os.getenv( 'FLASKEIKON' ), 'resource', 'config' ) )
)
import eikon
eikon.set_app_key( cfg[ 'appid' ] )


def main():

    result = eikon.get_timeseries(
        [ '042000.KQ' ],
        start_date = '2000-01-01',
        end_date = '2018-10-31',
        interval = 'daily'
    )
    print( result )


if __name__ == '__main__':

    sys.exit( main() )
