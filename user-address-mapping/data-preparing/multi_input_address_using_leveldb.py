import leveldb
db1=leveldb.LevelDB("./analysis/pickle/txhash_heighttxindex.leveldb")
db2=leveldb.LevelDB("./analysis/pickle/height_txindex_outputindex_address_value.leveldb")

#from gevent import monkey
#monkey.patch_all()

#from gevent.pool import Pool
#pool = Pool(128)

def getaddress(info):
    [tx_hash, outputindex] = info
    address = ''
    try:
	    height_txindex = db1.Get(tx_hash)
            height_txindex = height_txindex.split(';')
            key = height_txindex[0] + ";" + str(int(height_txindex[1])+1) + ';' + outputindex
            address = db2.Get(key).split(';')[0] 
    except Exception as e:
            if tx_hash =='0000000000000000000000000000000000000000000000000000000000000000':
            	address = 'coinbase'
            else:
            	print e
    return address 


to_operation = []


tmp_heghit = ''
tmp_txindex = ''
with open('/mnt2/metadata/revised_sub_tx_input.csv','r') as f, open('/mnt2/metadata/multi_input_address_using_leveldb.csv','w') as wf:
        for line in f:
                line = line.split(',')
                origin_heghit = line[0]
                origin_txindex = line[1]
                origin_inputindx = line[2]
                outputindex = line[-2]
                tx_hash = line[3]
                if origin_inputindx == '0':
                	if len(to_operation)>1:
                		results = []
				for item in to_operation:
					results.append(getaddress(item))
                		wf.write(','.join([tmp_heghit, tmp_txindex] + results) + '\n')

                	to_operation = [[tx_hash, outputindex]]
                	
                else:
                	to_operation.append([tx_hash, outputindex])

                tmp_heghit = origin_heghit
                tmp_txindex = origin_txindex


