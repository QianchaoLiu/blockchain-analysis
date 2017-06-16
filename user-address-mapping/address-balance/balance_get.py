import leveldb

balance_spend=leveldb.LevelDB("./analysis/pickle/address_balance")

with open('./revised_tx_output_handle_error.csv','r') as f:
	for line in f:
		line = line.split(',')
		try:
			address = line[4]
			value = int(line[3])/100000000.
		except:
			continue
		try:
			origin_value = float(balance_spend.Get(address))
			balance_spend.Put(address, str(origin_value + value))
		
		except:
			balance_spend.Put(address, str(value))
