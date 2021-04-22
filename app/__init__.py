from flask import Flask, request
from logging.handlers import TimedRotatingFileHandler
import os, logging, json, eikon

webapp = Flask( __name__ )

def init( app ):

    cfg = json.load(
        fp = open( os.path.join( os.getenv( 'FLASKEIKON' ), 'resource', 'config' ) )
    )
    eikon.set_app_key( cfg[ 'appid' ] )

    handler = TimedRotatingFileHandler(
        filename = cfg[ 'log' ], when = 'MIDNIGHT', encoding = 'utf-8'
    )
    handler.setFormatter( logging.Formatter(
        '[%(processName)s[%(process)d]|%(threadName)s[%(thread)d]|%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s'
    ) )
    app.logger.addHandler( handler )
    app.logger.setLevel( logging.DEBUG )

    app.config[ 'IP' ] = cfg[ 'ip' ]
    app.config[ 'PORT' ] = cfg[ 'port' ]

    from app.api import api as api_blueprint
    app.register_blueprint( blueprint = api_blueprint, url_prefix = '/api/' )


init( webapp )

@webapp.before_request
def beforeRequest():

    webapp.logger.debug( '{} | {} | {} | {} | {}'.format(
        request.remote_addr, request.user_agent.platform,
        request.user_agent.browser, request.method, request.path
    ) )


from app import view
