import sys, subprocess, os, psutil, time
from subprocess import PIPE, DEVNULL


class Daemon( object ):

    FLAG_COMBINATION = 0x00000008 | 0x00000200 | 0x08000000

    @staticmethod
    def isOnWindow():

        return sys.platform == 'win32'

    @staticmethod
    def pidPath( pidName ):

        if Daemon.isOnWindow():
            return 'C:\\Temp\\' + pidName + '.pid'
        else:
            return '/tmp/' + pidName + '.pid'

    @staticmethod
    def start( processFile, pidName ):

        if Daemon.isOnWindow():
            prcs = subprocess.Popen(
                args = [ sys.executable, processFile, 'child' ],
                creationflags = Daemon.FLAG_COMBINATION,
                stdin = DEVNULL, stdout = DEVNULL, stderr = DEVNULL
            )
            pid = prcs.pid
        else:
            prcs = subprocess.Popen(
                args = [ sys.executable, processFile, 'child' ],
                stdout = PIPE, stderr = PIPE
            )
            pid = prcs.pid

        if pid is None:
            raise Exception( 'Process cannot be spawned.' )
        else:
            time.sleep( 3 )
            while not psutil.pid_exists( pid ):
                print( 'Wait for process[ {:d} ] is spawned...'.format( pid ) )
                time.sleep( 1 )
            print( 'Service [{}] is started as {}.'.format( pidName, pid ) )

        with open( Daemon.pidPath( pidName ), 'w' ) as f:
            f.write( str( pid ) )
        f.close()
        sys.exit( 0 )

    @staticmethod
    def stop( pidName ):

        pid = None
        try:
            with open( Daemon.pidPath( pidName ), 'r' ) as f:
                pid = f.readline()
            f.close()
        except IOError as err:
            print( err )

        if pid is None:
            raise Exception( 'Invalid pid.' )

        if Daemon.isOnWindow():
            try:
                killer = subprocess.Popen(
                    args = [ 'taskkill.exe', '/PID', pid, '/F' ],
                    stdout = PIPE, stderr = PIPE
                )
                result = killer.communicate()
            except Exception as err:
                print( err )
                print( 'Couldn\'t kill process ', pid )
            else:
                print( 'Service [{}] is terminated.'.format( pid ) )
        else:
            try:
                subprocess.Popen( args = [ 'kill', '-SIGTERM', pid ] )
            except Exception as err:
                print( err )
                print( 'Couldn\'t kill process ', pid )
            else:
                print( 'Service [{}] is terminated.'.format( pid ) )

        os.remove( Daemon.pidPath( pidName ) )

    @staticmethod
    def status( pidName ):

        try:
            with open( Daemon.pidPath( pidName ), 'r' ) as f:
                pid = f.readline()
            f.close()
            return pid
        except IOError as err:
            print( err )
