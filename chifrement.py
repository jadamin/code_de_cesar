message_a_code = input("Entrez votre texte : ")
cle = int(input("Entrez votre cle :"))
message = [(ord(i)+cle) for i in message_a_code]
message_décodé = [chr(i)for i in message]

final = "".join(message_décodé)
print(final)        
