num=int(input("ENTER THE NUMBER"))
NumLen=0
while num>0:
     NumLen = numLen + 1
t=int("t/10")
if NumLen>=4:
     NumLen=int(NumLen/2)
     chk=0
     while num>0:
          rem=num%10
if chk=="numLen":
  midOne=rem
elif chk==("numlen-1"):
 midTwo=rem
num=int(num/10)
chk = chk + 1
prod = midOne*midTwo
print("\n PRODUCT OF MID DIGITS (" + str(midOne)+ "*"   + str(midTwo)+ ")= ",prod)
else:
print("\n ITS A NOT A 4 OR MORE THAN 4 DIGIT NUMBER!")