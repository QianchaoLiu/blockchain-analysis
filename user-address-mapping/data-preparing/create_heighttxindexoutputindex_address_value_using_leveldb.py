import leveldb 
db=leveldb.LevelDB("./analysis/pickle/height_txindex_outputindex_address_value.leveldb")
with open("/mnt2/metadata/revised_tx_output.csv","r") as f:
	for line in f:
		line=line.split(",")
		key =";".join(line[:3])
		try:
			value=line[-3].split('=')[1].split(')')[0]
			value = value + ';' + line[3]
		except:
			#print line
			continue
		db.Put(key,value)
db.close()
