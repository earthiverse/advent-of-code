import sys

versionSum = 0
with open("day16_input.csv") as file:
    hex = file.readline().strip()
    b = bin(int(hex, 16))[2:].zfill(len(hex) * 4)

    human = ""
    while True:
        version, b = int(b[0:3], 2), b[3:]
        versionSum += version
        type, b = int(b[0:3], 2), b[3:]

        if type == 4:
            # Number Packet
            value = ""
            while True:
                header, v, b = b[0:1], b[1:5], b[5:]
                value += v

                if header == "0":
                    break

            human += f"{int(value, 2)}"
        else:
            # Operator Packet
            length, b = b[0:1], b[1:]

            if length == "0":
                sub, b = int(b[0:15], 2), b[15:]
            else:
                sub, b = int(b[0:11], 2), b[11:]
                pass

        if "1" not in b:
            break

print(f"Version Sum: {versionSum}")


def parseSub(b):
    version, b = int(b[0:3], 2), b[3:]
    type, b = int(b[0:3], 2), b[3:]

    if type == 4:
        # Number Packet
        value = ""
        while True:
            header, v, b = b[0:1], b[1:5], b[5:]
            value += v

            if header == "0":
                break

        value = int(value, 2)
    else:
        # Operator Packet
        length, b = b[0:1], b[1:]

        if length == "0":
            sub, b = int(b[0:15], 2), b[15:]
            stopAtLength = sub
            stopAtNumPackets = None
        else:
            sub, b = int(b[0:11], 2), b[11:]
            stopAtLength = None
            stopAtNumPackets = sub

        if type == 0:
            # Sum Operator
            value = 0
            packetNum = 0
            packetLength = len(b)
            while True:
                [b, v] = parseSub(b)
                value += v
                packetNum += 1
                if stopAtNumPackets is not None and packetNum >= stopAtNumPackets:
                    break
                if stopAtLength is not None and stopAtLength <= packetLength - len(b):
                    break
        elif type == 1:
            # Product Operator
            value = 1
            packetNum = 0
            packetLength = len(b)
            while True:
                [b, v] = parseSub(b)
                value *= v
                packetNum += 1
                if stopAtNumPackets is not None and packetNum >= stopAtNumPackets:
                    break
                if stopAtLength is not None and stopAtLength <= packetLength - len(b):
                    break
        elif type == 2:
            # Minimum Operator
            value = sys.maxsize
            packetNum = 0
            packetLength = len(b)
            while True:
                [b, v] = parseSub(b)
                if v < value:
                    value = v
                packetNum += 1
                if stopAtNumPackets is not None and packetNum >= stopAtNumPackets:
                    break
                if stopAtLength is not None and stopAtLength <= packetLength - len(b):
                    break
        elif type == 3:
            # Maximum Operator
            value = -sys.maxsize - 1
            packetNum = 0
            packetLength = len(b)
            while True:
                [b, v] = parseSub(b)
                if v > value:
                    value = v
                packetNum += 1
                if stopAtNumPackets is not None and packetNum >= stopAtNumPackets:
                    break
                if stopAtLength is not None and stopAtLength <= packetLength - len(b):
                    break
        elif type == 5 or type == 6 or type == 7:
            [b, v1] = parseSub(b)
            [b, v2] = parseSub(b)

            if type == 5:
                if v1 > v2:
                    return [b, 1]
                else:
                    return [b, 0]
            elif type == 6:
                if v1 < v2:
                    return [b, 1]
                else:
                    return [b, 0]
            elif type == 7:
                if v1 == v2:
                    return [b, 1]
                else:
                    return [b, 0]
        else:
            print(f"Unknown Operator Type: {type}")

    return [b, value]


with open("day16_input.csv") as file:
    hex = file.readline().strip()
    print(hex)
    b = bin(int(hex, 16))[2:].zfill(len(hex) * 4)

    print(f"Value: {parseSub(b)[1]}")
