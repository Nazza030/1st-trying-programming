print("Benvenuto, Io mi chiamo TOBOT\nsono un BOT, ed il primo programma creato da NP.\n\nSono un semplice BOT che per adesso sa fare poche cose, mentre tu...")
nome = input("Come ti chiami?")
print(nome + ' è proprio un bel nome, complimenti ai tuoi genitori!')
eta = input("Quanti anni hai?")
if(int(eta) < 17):
      print("ahhh sei ancora un minorenne!")
print("Il giorno in cui compierai " + str(int(eta) + 1) + " anni ti farò gli auguri!...")
eta_silente = 150
print("... e quel giorno ti mancheranno solo " + str(150 - (int(eta) + 1)) + " anni per essere vecchio come Albus Silente!")
      
