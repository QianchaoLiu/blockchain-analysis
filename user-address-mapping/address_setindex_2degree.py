import leveldb
import os
try:
	os.system('rm -rf ./analysis/pickle/address_minsetindex_2degree')
except:
	pass

try:
    os.system('rm -rf ./analysis/pickle/minsetindex_address_2degree')
except:
    pass

address_minsetindex_leveldb = leveldb.LevelDB('./analysis/pickle/address_minsetindex_2degree')
minsetindex_address = leveldb.LevelDB('./analysis/pickle/minsetindex_address_2degree')


set_index = 0
address_minsetindex = {}
# second order mapping 
minsetindex_mapdict = {}
point_to_minsetindex_mapdict = {}
with open('multi_input_address_using_leveldb.csv','r') as f:
    for line in f:
        line = line.strip('\n').split(',')
        print line[0]
        addresses = line[2:]
        addresses = list(set(addresses))

        index_address = {}
        if len(addresses)>1:
            for address in addresses:
                try:
                    index = minsetindex_mapdict[address_minsetindex[address]]
                except:
                    try:
                        index_address[-1].append(address)
                    except:
                        index_address[-1]=[address]               
                else:
                    try:
                        index_address[index].append(address)
                    except:
                        index_address[index]=[address]
            keys = index_address.keys() 
            if keys == [-1]:
                # all new
                belong_to = set_index
                minsetindex_mapdict[belong_to] = belong_to
                point_to_minsetindex_mapdict[belong_to] = [belong_to]
                for address in addresses:
                    address_minsetindex[address] = belong_to
#                minsetindex_address.Put(str(belong_to), ';'.join(addresses))
            elif len(keys) == 1:
                # all have been handeled
                pass
            else:
                if -1 in keys:
                    keys.remove(-1)
                    target_key = min(keys)
                    keys.remove(target_key)
                    to_revise = [-1] + keys

                else:
                    target_key = min(keys)
                    keys.remove(target_key)
                    to_revise = keys
 #               origin_addresses = minsetindex_address.Get(str(target_key)).split(';')
                
    #            to_append = []
                for key in to_revise:
                    
                    if key == -1:
                        addresses = index_address[-1]
                        belong_to = target_key
                        
                        for address in addresses:
                            address_minsetindex[address] = belong_to
   #                     to_append.extend(addresses)

                    else:
  #                      addresses = minsetindex_address.Get(str(key)).split(';')
    
     #                   to_append.extend(addresses)
                        for item in point_to_minsetindex_mapdict[key]:
                            minsetindex_mapdict[item] = target_key
                            point_to_minsetindex_mapdict[target_key].append(item)                        
			del point_to_minsetindex_mapdict[key]
      #                  minsetindex_address.Delete(str(key))
       #         if to_append:
        #            minsetindex_address.Put(str(target_key), ';'.join(origin_addresses+to_append))      
            set_index += 1

for key in address_minsetindex.keys():
	address_minsetindex_leveldb.Put(key, str(minsetindex_mapdict[address_minsetindex[key]]))
