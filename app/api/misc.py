from flask import request, jsonify, abort
from app import webapp
from app.api import api
import eikon

@api.route( "misc/reportdate", methods = [ 'POST' ] )
def reportdate():

    rics = request.get_json()

    try:
        result = eikon.get_data( instruments = rics, fields= 'TR.ExpectedReportDate' )[ 0 ]
        refined = dict( zip( result[ 'Instrument' ], result[ 'Expected Report Date' ] ) )
        webapp.logger.info( "{} | {}".format( len( rics ), len( refined ) ) )
        return jsonify( data = refined )
    except Exception as err:
        webapp.logger.warn( err )
        return abort( 500 )

@api.route( "misc/data", methods = [ 'POST' ] )
def getdata():

    rqst = request.get_json()
    try:
        rst = eikon.get_data(
            instruments = rqst[ 'instruments' ],
            fields = rqst[ 'fields' ],
            parameters = rqst[ 'parameters' ],
            raw_output = True
        )
        return jsonify( data = rst )
    except Exception as err:
        webapp.logger.warn( err )
        return abort( 500 )

@api.route( "misc/timeseries", methods = [ 'POST' ] )
def timeseries():

    rqst = request.get_json()
    try:
        rst = eikon.get_timeseries(
            rics = rqst[ 'rics' ],
            start_date = rqst[ 'start' ],
            end_date = rqst[ 'end' ],
            interval = rqst[ 'interval' ],
            raw_output = True
        )
        return jsonify( data = rst )
    except Exception as err:
        webapp.logger.warn( err )
        return abort( 500 )

@api.route( "misc/symbology", methods = [ 'POST' ] )
def symbology():

    rqst = request.get_json()
    try:
        rst = eikon.get_symbology(
            symbol = rqst[ 'symbol' ],
            from_symbol_type = rqst[ 'from' ],
            to_symbol_type = rqst[ 'to' ],
            raw_output = True
        )
        return jsonify( data = rst )
    except Exception as err:
        webapp.logger.warn( err )
        return abort( 500 )

@api.route( "misc/news", methods = [ 'POST' ] )
def news():

    rqst = request.get_json()
    try:
        rst = eikon.get_news_headlines(
            query = rqst[ 'query' ],
            count = 100,
            date_from = rqst[ 'from' ],
            date_to = rqst[ 'to' ],
            raw_output = True
        )
        for idx, val in enumerate( rst[ 'headlines' ] ):
            val[ 'news' ] = eikon.get_news_story( val[ 'storyId' ] )
        return jsonify( data = rst )
    except Exception as err:
        webapp.logger.warn( err )
        return abort( 500 )
