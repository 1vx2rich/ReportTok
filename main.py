#
#
#
#                    1vx#1163 - https://discord.gg/FsewnnaUTv
#
#
#

f='\x1b[31mAccess denied'
e='\x1b[35mAcces key: \x1b[97m'
d='1vx'
c='\x1b[35mUser ID : \x1b[97m'
b='\x1b[35mUsername : @\x1b[97m'
a='Failed to get user id, please put the user id your self'
Z='id'
Y='user'
X='status_code'
W=True
V=int
U='clear'
T='made by -> \x1b[97mhttps://discord.gg/FsewnnaUTv'
S='@'
M=''
L='        \\/     \\/|__|                                        \\/'
K=' |____|_  /\\___  >   __/ \\____/|__|   |__|  |__|  \\____/|__|_ \\ '
J=' |    |   \\  ___/|  |_> >  <_> )  | \\/|  |  |  | (  <_> )    < '
I=' |       _// __ \\____ \\ /  _ \\_  __ \\   __\\   __\\/  _ \\|  |/ /'
H='\\______   \\ ____ ______   ____________/  |__/  |_  ____ |  | __'
G='\x1b[35m __________                             __    __          __ '
F=input
A=print
import os,requests as D,time as C
from random import randint as N
B=0
def E(ID):
	global B
	while W:
		try:
			E=N(0,12000);F=D.get(f"https://www.tiktok.com/aweme/v1/aweme/feedback/?report_type=user&object_id={ID}&owner_id={ID}&reason={E}");B+=1
			if F.json()[X]==0:A(f"[36m Reported {B} - Reason: {E}")
			elif not F.status_code==200:A(f"[31m ERROR {B} - Reason: {E}[97m");C.sleep(3)
			else:A(f"[31m ERROR {B} - Reason: {E}[97m");C.sleep(5)
		except:A(f"[31m ERROR {B} - Reason:  {E}[97m");C.sleep(5)
def O(Username):
	A=Username
	if not A.startswith(S):A=S+A
	try:B=D.get(f"https://www.tiktok.com/node/share/user/@{A}");return B.json()[Y][Z],1
	except:return a,0
def P():
	A(G);A(H);A(I);A(J);A(K);A(L);A(M);A(T);C=F(b);B=O(C)
	if B[1]==0:A(B[0]);B=V(F(c));E(B)
	else:E(B)
Q=d
A(G)
A(H)
A(I)
A(J)
A(K)
A(L)
A(M)
A(T)
R=F(e)
if Q==R:import os;os.system(U);P()
else:import os;os.system(U);A(G);A(H);A(I);A(J);A(K);A(L);A(M);A(f)
import os,requests as D,time as C
from random import randint as N
B=0
def E(ID):
	global B
	while W:
		try:
			E=N(0,12000);F=D.get(f"https://www.tiktok.com/aweme/v1/aweme/feedback/?report_type=user&object_id={ID}&owner_id={ID}&reason={E}");B+=1
			if F.json()[X]==0:A(f"[36m Reported {B} - Reason: {E}")
			elif not F.status_code==200:A(f"[31m ERROR {B} - Reason: {E}[97m");C.sleep(3)
			else:A(f"[31m ERROR {B} - Reason: {E}[97m");C.sleep(5)
		except:A(f"[31m ERROR {B} - Reason:  {E}[97m");C.sleep(5)
def O(Username):
	A=Username
	if not A.startswith(S):A=S+A
	try:B=D.get(f"https://www.tiktok.com/node/share/user/@{A}");return B.json()[Y][Z],1
	except:return a,0
def P():
	A(G);A(H);A(I);A(J);A(K);A(L);A(M);A(T);C=F(b);B=O(C)
	if B[1]==0:A(B[0]);B=V(F(c));E(B)
	else:E(B)
Q=d
A(G)
A(H)
A(I)
A(J)
A(K)
A(L)
A(M)
A(T)
R=F(e)
if Q==R:import os;os.system(U);P()
else:import os;os.system(U);A(G);A(H);A(I);A(J);A(K);A(L);A(M);A(f)
