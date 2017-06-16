import os
from blockchain_parser.blockchain import Blockchain

# Instanciate the Blockchain by giving the path to the directory 
# containing the .blk files created by bitcoind
blockchain = Blockchain('/root/.bitcoin/blocks/')
height=0
if os.path.exists('./parse_result/block.csv'):
    os.remove('./parse_result/block.csv')
if os.path.exists('./parse_result/tx_header.csv'):
    os.remove('./parse_result/tx_header.csv')
if os.path.exists('./parse_result/tx_outpus.csv'):
    os.remove('./parse_result/tx_outpus.csv')
if os.path.exists('./parse_result/tx_input.csv'):
    os.remove('./parse_result/tx_input.csv')
for block in blockchain.get_unordered_blocks():
    block_header = block.header
    result = [height,block_header.version, block_header.previous_block_hash, block_header.merkle_root, block_header.timestamp, block_header.bits, block_header.difficulty, block_header.nonce, len(block.transactions)]
    result = [str(item) for item in result]
    
    with open('./parse_result/block.csv','a') as wf:
        wf.write(','.join(result)+'\n')    
    height += 1
    tx_index = 0
    tx_results = []
    inputs = []
    outputs = []
    for tx in block.transactions:
        tx_results.append([height, tx_index, tx.version, tx.locktime, tx.hash,tx.n_inputs, tx.n_outputs])
        tx_index+=1
        for input_no, tx_input in enumerate(tx.inputs):
            #inputs.append([height, tx_index, input_no, tx_input.transaction_hash, tx_input.transaction_index, tx_input.sequence_number, tx_input.script])
            inputs.append([height, tx_index, input_no, tx_input.transaction_hash, tx_input.transaction_index])
	for output_no, tx_output in enumerate(tx.outputs):
            #outputs.append([height, tx_index,output_no, tx_output.value, tx_output.script, tx_output.addresses, tx_output.type])
    	    try:
		outputs.append([height, tx_index,output_no, tx_output.value, str(tx_output.addresses).split('=')[1].split(')')[0], tx_output.type])
    	    except:
		pass
    with open('./parse_result/tx_header.csv','a') as wf:
        for tx_detail in tx_results:
            tx_detail = [str(item) for item in tx_detail]
            wf.write(','.join(tx_detail)+'\n')
    with open('./parse_result/tx_input.csv','a') as wf:
        for tx_input in inputs:
            tx_input = [str(item) for item in tx_input]
            wf.write(','.join(tx_input)+'\n')
    with open('./parse_result/tx_output.csv','a') as wf:
        for tx_output in outputs:
            tx_output = [str(item) for item in tx_output]
            wf.write(','.join(tx_output)+'\n')
           
