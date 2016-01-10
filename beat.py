import os
beep = lambda x: os.system("echo -n '\a';sleep .2;" * x)
beep(5)

beep_slow = lambda x: os.system("echo -n '\a';sleep .4;" * x)
beep_medium = lambda x: os.system("echo -n '\a';sleep .2;" * x)
beep_fast = lambda x: os.system("echo -n '\a';sleep .05;" * x)

beep_slow(3)
beep_medium(4)
os.system("echo -n;sleep 3;")
beep_fast(5)
