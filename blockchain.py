#Basic definition of blockchain

class BlockChain(object):

    def __init__(self):                         # default constructor
        self.chain = []
        self.current_transactions = []          # value transactions
        self.smart_contract = []                # execute smart contract
        self.link = []                          # pointer/link to document physical storage


