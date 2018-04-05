# pyBlockchain-basic
Basic blockchain implementation in Python3

PyBlockchain-Basic is a basic conceptual design for a blockchain to be used as a learning tool for the
technology and prototype for a production version. pyBlockChain-basic is NOT production level code rather a
playground for experimentation of concepts.

The Initial block structure is based on the following

1.Index
    Index being the location in the chain ( eg genesis block index=0)
2.Timestamp

3.Transactions

4.Contract

5.Link

6.Proof

7.PreviousHash



1.
2. Timestamp, when the block was completed
3. Transactions, saved value transactions ( like Bitcoin)
4. Contract, Code that can be saved and executed ( like Ethereum, smart contract)
5. Link, Link to external document store, not physically storing documents within the block itself due to
   size and implications.
6. Proof, Proof of work  and/or proof of state
7. PreviousHash, Hash of the previous block