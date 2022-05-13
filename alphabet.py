lst = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
out = []
for lett in lst:
    for let in lst:
        for lt in lst:
            vys = lett + let + lt
            # print(vys)
            out.append(vys)
print(out)