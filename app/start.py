import sys, os
sys.path.append( os.getenv( 'FLASKEIKON' ) )
from app import webapp


def run():

    webapp.logger.info( 'flask-eikon is started.' )
    webapp.run( host = webapp.config[ 'IP' ], port = webapp.config[ 'PORT' ] )
    webapp.logger.info( 'flask-eikon is terminated.' )
    return 0


if __name__ == '__main__':

    sys.exit( run() )
