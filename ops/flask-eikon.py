import sys, os
sys.path.append( os.getenv( 'FLASKEIKON' ) )

from lib.daemon import Daemon


def main( command ):

    modulePath = os.path.join( os.getenv( 'FLASKEIKON' ), 'app' )
    processFile = os.path.realpath(
        os.path.join( modulePath, 'start.py' )
    )
    pidName = modulePath.split( '\\' )[ -1 ]

    try:
        if command == 'start':
            if os.path.isfile( Daemon.pidPath( pidName) ) == True:
                print( 'Process is already running.' )
            else:
                Daemon.start( processFile, pidName )

        elif command == 'stop':
            if os.path.isfile( Daemon.pidPath( pidName ) ) == True:
                Daemon.stop( pidName )
            else:
                print( 'There is no process before.' )

        elif command == 'restart':
            Daemon.stop( pidName )
            Daemon.start( processFile, pidName )

        elif command == 'status':
            pid = Daemon.status( pidName )
            print( pid )

    except Exception as err:
        print( err )
        return -1

    return 0


if __name__ == '__main__':

    if len( sys.argv ) != 2:
        print( 'Usage: python $FLASKEIKON\ops\\flask-eikon.py start | stop | status | restart' )

    sys.exit( main( sys.argv[ 1 ] ) )
