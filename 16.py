hex_bits = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

def hex_to_bin(s):
    return "".join(hex_bits[c] for c in s)

def op(op, vals):
    if op == 0: return sum(vals)
    if op == 1:
        prod = 1
        for val in vals: prod *= val
        return prod
    if op == 2: return min(vals)
    if op == 3: return max(vals)
    if op == 5: return 1 if vals[0] > vals[1] else 0
    if op == 6: return 1 if vals[0] < vals[1] else 0
    if op == 7: return 1 if vals[0] == vals[1] else 0
    
def parse(bits):
    ver = int(bits[0:3], 2)
    typ = int(bits[3:6], 2)
    if typ == 4:
        # literal - see how many bits to take
        s = ""
        st = 6
        last = False
        while not last:
            last = bits[st] == "0"
            s += bits[st+1 : st+5]
            st += 5

        val = int(s, 2)
        
        return (ver, st, val)
    else: 
        # some kind of operator
        lentyp = int(bits[6], 2)
        if lentyp == 0:
            subbits = int(bits[7:22], 2)
            ofs = 22
        elif lentyp == 1:
            subpackets = int(bits[7:18], 2)
            ofs = 18
        consumed = 0
        pck = 0
        vals = []
        while (lentyp == 0 and consumed < subbits) or (lentyp == 1 and pck < subpackets):
            tup = parse(bits[consumed+ofs:])
            # print(tup)
            ver2, st2, val2 = tup
            ver += ver2
            consumed += st2
            pck += 1
            vals.append(val2)
        return (ver, consumed+ofs, op(typ, vals))
    return None
    
print(parse(hex_to_bin("C200B40A82")))
print(parse(hex_to_bin("04005AC33890")))
print(parse(hex_to_bin("CE00C43D881120")))
print(parse(hex_to_bin("9C0141080250320F1802104A08")))

input = """4054460802532B12FEE8B180213B19FA5AA77601C010E4EC2571A9EDFE356C7008E7B141898C1F4E50DA7438C011D005E4F6E727B738FC40180CB3ED802323A8C3FED8C4E8844297D88C578C26008E004373BCA6B1C1C99945423798025800D0CFF7DC199C9094E35980253FB50A00D4C401B87104A0C8002171CE31C41201062C01393AE2F5BCF7B6E969F3C553F2F0A10091F2D719C00CD0401A8FB1C6340803308A0947B30056803361006615C468E4200E47E8411D26697FC3F91740094E164DFA0453F46899015002A6E39F3B9802B800D04A24CC763EDBB4AFF923A96ED4BDC01F87329FA491E08180253A4DE0084C5B7F5B978CC410012F9CFA84C93900A5135BD739835F00540010F8BF1D22A0803706E0A47B3009A587E7D5E4D3A59B4C00E9567300AE791E0DCA3C4A32CDBDC4830056639D57C00D4C401C8791162380021108E26C6D991D10082549218CDC671479A97233D43993D70056663FAC630CB44D2E380592FB93C4F40CA7D1A60FE64348039CE0069E5F565697D59424B92AF246AC065DB01812805AD901552004FDB801E200738016403CC000DD2E0053801E600700091A801ED20065E60071801A800AEB00151316450014388010B86105E13980350423F447200436164688A4001E0488AC90FCDF31074929452E7612B151803A200EC398670E8401B82D04E31880390463446520040A44AA71C25653B6F2FE80124C9FF18EDFCA109275A140289CDF7B3AEEB0C954F4B5FC7CD2623E859726FB6E57DA499EA77B6B68E0401D996D9C4292A881803926FB26232A133598A118023400FA4ADADD5A97CEEC0D37696FC0E6009D002A937B459BDA3CC7FFD65200F2E531581AD80230326E11F52DFAEAAA11DCC01091D8BE0039B296AB9CE5B576130053001529BE38CDF1D22C100509298B9950020B309B3098C002F419100226DC"""
print(parse(hex_to_bin(input)))


        