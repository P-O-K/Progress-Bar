
class ProgressionBar:

    _totalIteration     :int;
    _barLength          :int;
    _bIcon              :str    ='█'


    def __init__( self, totalIterations:int, barLength:int=10 ) -> None:
        self._totalIteration    = totalIterations;
        self._barLength         = barLength;


    def progress( self, currentIteration:int ) -> None:
        complete = ( self._barLength *currentIteration ) //self._totalIteration;
        progressBar = ( self._bIcon *complete ) +( ' ' *( self._barLength -complete -1 ) );
        print( f"Executing: |{ progressBar }| { currentIteration /self._totalIteration :.2%}", end='\r' );
        if currentIteration+1 >= self._totalIteration: print( );



if __name__ == '__main__':
    from time import sleep

    maxIter = 100;
    bar = ProgressionBar( totalIterations=maxIter, barLength=20 );
    for i in range( 1, maxIter ):
        bar.progress( i );
        sleep( 0.01 )
