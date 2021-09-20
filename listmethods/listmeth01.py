#!/usr/bin/env python3
proto = ["ssh","http","https"]
protoa=proto

print("Proto is:", proto)
print("Protoa is:", protoa)

#proto.extend("dns")
proto.append("dns")
print("Proto is now (add dns):", proto)

proto2=[22,80,443,53]
print("proto2 is:",proto2)
proto.extend(proto2)
print("Proto is now (exend proto):", proto)
print("proto2 is:",proto2)

protoa.append("dns")
print("protoa is now (add dns):",protoa)
protoa.append(proto2)
print("protoa is now (append proto2):",protoa)
print("proto2 is:",proto2)

protoa.pop(4)
print("protoa is now (pop 4):",protoa)
