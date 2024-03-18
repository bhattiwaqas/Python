#account class
class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f"{self.owner} {self.balance}"
    def deposit(self, amt): #deposit amt into account
        self.balance = self.balance + amt
        print(self.owner, "After deposit of", amt, "the balance is now", self.balance)
    def withdraw(self, amt): #deposit amt into account
        self.balance = self.balance - amt
        print(self.owner, "After withdrawal of ",amt, ", the balance is now", self.balance)

def deposit2(thing, ownerr, amtt):
        for i in thing:
            if i.owner == ownerr:
                i.deposit(amtt)
def withdraw2(thing,ownerr,amtt):
        for i in thing:
            if i.owner == ownerr:
                i.withdraw(amtt)
                

bank = []

acct1 = Account( 'tom', 344)
acct2 = Account('jane', 88)
acct3 = Account('mike', 82)

#print(acct1)
#acct1.deposit(20)
#acct1.withdraw(200)

bank.append(acct1)            #add single 
bank.extend( [acct2, acct3] ) #add one large list as multiple 

acct4 = Account('ellen', 879)
acct5 = Account('joe', 99)
bank.extend( [acct4,acct5] )


for i in bank:
    print(i)
print('\n')

deposit2(bank, 'jane', 12)
withdraw2(bank, 'mike', 33)

acct6 = Account('gaga', 522)
bank.insert(0,acct6) #put in front of list at 0


for i in bank:
    print(i)
    sum = 0
    sum = sum + i.balance
print("sum of all account balances is currently", sum)
acct7 = Account('alan',34)
acct8 = Account('sarah',77)
acct9 = Account('toni',104)

bank.insert(-1,acct7)
bank.insert(1,acct8)
bank.insert(3,acct9)

count =0
for i in bank:
    if i.balance>170:
        i.balance = i.balance - 43
        count = count+1
print("There were",count,"accounts that were affected by the $42 deduction")
print(bank[0],bank[1],bank[2],bank[3])

del bank[1]

avg = 0
sum = 0
count = 0
for i in bank:
    sum = sum + i.balance
    count = count+1
avg = (sum/count)
print("Average is", avg)

acct10 = Account('slow', 337)
acct11 = Account('michelle', 625)
bank.extend( [acct10, acct11] )

count = 0
for i in bank:
    if i.balance < 200:
        i.balance + 12
    if i.balance >120:
        count = count+1
print("There are",count,"accounts with a balance over 120")
bank.append(Account('elliot',32))
bank.append(Account('stephanie',992))
bank.insert(2,Account('hunter',552))


for i in bank:
    if i.owner == 'toni':
        i.owner = 'sabrina'
        i.balance = 43
        #bank.insert(i+1,Account('lee',24) )
    print(i)
    


#acct4.owner = 'lady ellen' 
for i in bank: #change ellen to lady ellen
    if i.owner == 'ellen':
        i.owner = 'lady ' + i.owner


for i in bank: #change jane to sister jane
    if i.owner == 'jane':
        i.owner = 'sister jane'
        
#for i in bank: #deposits
#    if i.owner == 'gaga':
#        i.deposit(52)
#    if i.owner == 'tom':
#        i.deposit(89)
#    if i.owner == 'sister jane':
#        i.deposit(100)

# make a method that takes owner and deposits values^
#do all of that with method deposit2^^

#deposit2(bank, 'gaga', 52)
#deposit2(bank, 'tom', 89)
#deposit2(bank, 'sister jane', 100)

#del bank[1]
#delete second element


print('\n')

print("We have", len(bank), "objects")
