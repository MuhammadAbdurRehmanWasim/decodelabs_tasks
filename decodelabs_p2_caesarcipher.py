"""
DecodeLabs Industrial Training Kit | Batch: 2026
Project 2: Basic Encryption & Decryption
Submitted by: Muhammad Abd Ur Rehman
"""

def encrypt_caesar(plaintext, shift):
    """
    Encrypts user text using the Caesar Cipher mathematical formula:
    E_n(x) = (x + n) % 26
    """
    ciphertext = ""
    for char in plaintext:
        if char.isupper():
            cipher_char = chr((ord(char) - 65 + shift) % 26 + 65)
            ciphertext += cipher_char
        elif char.islower():
            cipher_char = chr((ord(char) - 97 + shift) % 26 + 97)
            ciphertext += cipher_char
        else:
            ciphertext += char
    return ciphertext


def decrypt_caesar(ciphertext, shift):
    """
    Decrypts ciphertext using the reverse engineering logic:
    D_n(x) = (x - n) % 26
    """
    return encrypt_caesar(ciphertext, -shift)


def main():
    print("=" * 60)
    print("        DECODELABS CYBERSECURITY ANALYST ENGINE v1.0        ")
    print("      Data Confidentiality - Analyst: M. Abd Ur Rehman      ")
    print("=" * 60)
    
    plaintext = input("[INPUT] Enter the raw plaintext message: ")
    
    while True:
        try:
            shift_input = input("[INPUT] Enter the rotation shift key (default is 3): ")
            shift = int(shift_input) if shift_input.strip() else 3
            break
        except ValueError:
            print("[ALERT] Invalid key! Please enter a valid integer.")
            
    print("-" * 60)
    
    print("[PROCESSING] Applying mathematical transformation rules...")
    encrypted_msg = encrypt_caesar(plaintext, shift)
    decrypted_msg = decrypt_caesar(encrypted_msg, shift)
    
    print(f"\n[OUTPUT] Original Text:  {plaintext}")
    print(f"[OUTPUT] Ciphertext:     {encrypted_msg}")
    print(f"[OUTPUT] Decrypted Text: {decrypted_msg}")
    
    if plaintext == decrypted_msg:
        print("\n[SUCCESS] Integrity Check Passed: Data is perfectly reversible.")
        print("[STATUS] Milestone Accomplished. Ready for Week 3 unlocks.")
    else:
        print("\n[CRITICAL] Integrity Check Failed: Mathematical logic mismatch.")
    print("=" * 60)


if __name__ == "__main__":
    main()
