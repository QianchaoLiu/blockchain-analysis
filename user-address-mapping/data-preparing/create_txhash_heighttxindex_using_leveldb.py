import leveldb
db=leveldb.LevelDB("./analysis/pickle/txhash_heighttxindex.leveldb")

with open("/mnt2/metadata/revised_tx_header.csv","r") as f:
	for line in f:
		line=line.split(",")
		value =";".join(line[:2])
		key=line[4]
		db.Put(key,value)
