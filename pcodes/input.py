sh = input("Enter hours:")
sr = input ("Enter rate:")
fh = float(sh)
fr = float(sr)
#print(fh,fr)
if fh>40:
    #print("overtime")
    reg = fr*fh
    otp = (fh-40.0)*(fr*0.5)
    #print("reg,otp")
    xp=reg+otp
else:
    xp=fh*fr
print(xp)
