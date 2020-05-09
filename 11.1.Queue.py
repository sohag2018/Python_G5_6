from collections import deque   #Auto import command=alt+sh+ent
#Queue-->follows FIFO

bank=deque(["Monir","Tofayel","Sharif","Sohag","Orfat"]) # for queue we need to import deque (inside a list)
print(bank)
print("----------------------------------------")

#remove
bank.pop()# to remove last index (top)
print(bank)
print("----------------------------------------")
bank.popleft() # remove 0 index (FIFO)
print(bank)
print("----------------------------------------")

if not bank:
    print("No queue left")

