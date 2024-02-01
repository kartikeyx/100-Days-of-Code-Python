alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)


def caesar(st_direction, st_text, st_shift):
  output_text= ""
  if st_direction== "decode":
    st_shift *= -1
  for i in st_text:
    if i in alphabet:
      ind = alphabet.index(i)
      new_pos = ind + st_shift
      output_text += alphabet[new_pos]
    else:
      output_text += i
  print(f"The {st_direction}d text is {output_text}")

want_continue = True
while want_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift%26
  caesar(st_direction= direction, st_text=text,st_shift=shift)

  cont = input("Type 'Yes' to continue or 'No' to quit!").lower()
  if cont == "no":
    want_continue = False
    print("End of Caesar Cipher.")
