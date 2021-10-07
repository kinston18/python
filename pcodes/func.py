def computepay(h, r):
    if h>40:
        reg=40*r
        otp=(h-40.0)*1.5*r
        pay=reg+otp
        
    else:
        pay=h*r
    return pay  
        

hrs = input("Enter Hours:")
rate= input("Enter rate per hour:")
fh=float(hrs)
fr=float(rate)
p = computepay(fh,fr)
print("Pay", p)
