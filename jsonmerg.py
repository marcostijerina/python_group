import json
# test cases for jsonStringA and jsonStringB according to your data input
jsonStringA = '{"error_1395946244342":"valueA","error_1395952003":"valueB"}'
jsonStringB = '{"error_%d":"Error Occured on machine %s in datacenter %s on the %s of process %s"}' % (timestamp_number, host_info, local_dc, step, c)

# now we have two json STRINGS
import json
dictA = json.loads(jsonStringA)
dictB = json.loads(jsonStringB)

merged_dict = {key: value for (key, value) in (dictA.items() + dictB.items())}

# string dump of the merged dict
jsonString_merged = json.dumps(merged_dict)
