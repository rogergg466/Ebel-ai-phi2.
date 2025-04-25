import os

# Cek apakah file udah ada biar ga download terus-terusan
if not os.path.exists("phi-2.Q4_K_S.gguf"):
    os.system("wget -O phi-2.Q4_K_S.gguf https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q4_K_S.gguf")

# lanjut jalanin model lu di bawah ini
print("Model siap dipakai!")