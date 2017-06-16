import leveldb

balance_spend=leveldb.LevelDB("./analysis/pickle/address_spend")

with open('./revised_sub_tx_input_address_within.csv','r') as f:
	for line in f:
		line = line.split(',')
		address = line[3]
		if address!='coinbase':
			value = int(line[4])/100000000.
			try:
				origin_value = float(balance_spend.Get(address))
				balance_spend.Put(address, str(origin_value - value))

			except:
				balance_spend.Put(address, str(-value))
