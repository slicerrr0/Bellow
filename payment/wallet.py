
class Wallet:
    '''Wrapper for wallet files.'''
    def __init__(self, fname: str) -> None:
        '''Constructs and returns a new instance of `Wallet`.
        
        :param fname: Path or name of the wallet file.
        '''
        self.fname = fname


class Electrum(Wallet):
    '''Interface for executing and retrieving
    the results of electrum commands.
    '''
    def __init__(self, fname: str) -> None:
        super().__init__(fname)