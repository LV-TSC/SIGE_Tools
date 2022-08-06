import os

try:
    os.remove("""C://Users//Public//Desktop//SIGE 2022.lnk""")
    os.remove("""C://Users//Public//Desktop//Refresca Sistemas.lnk""")
except OSError as e:
    print(f"Error:{ e.strerror}")