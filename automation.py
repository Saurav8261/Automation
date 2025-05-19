import re
appspathname= "C:\\Users\\emb-saurkum\\Desktop\\mqb\\apps"
swcname='\\lvem.idl'
nodename="CDCU"
filepathname= appspathname + swcname
with open(filepathname, 'r') as f:
    lines= f.readlines()
input_signals=[]
output_signals=[]
inside_input_section= False
inside_output_section=False
for line in lines:
    if re.match(r'\s*input\s*:', line):
        inside_input_section=True
        continue
    if inside_input_section:
        if not line.strip() or re.match(r'^\s*#',line):
            continue
        if re.match(r'\s*output\s*:', line):
            inside_input_section=False
            inside_output_section=True
            continue
        input_signals.append(line.split()[0][:-1])
    if inside_output_section:
        if not line.strip() or re.match(r'^\s*#',line):
            continue
        if re.match(r'\s*signal_types\s*:', line):
            inside_input_section=False
            inside_output_section=False
        output_signals.append(line.split()[0][:-1])
 
print("=========== Extracted Signals ===========\n")

print("🔵 Input Signals:")
for i, signal in enumerate(input_signals, 1):
    print(f"{i}. {signal}")

print("\n🟢 Output Signals:")
for i, signal in enumerate(output_signals, 1):
    print(f"{i}. {signal}")

print("\n=========================================")
