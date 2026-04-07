import os
import random
import string

from show_menu import show_menu
from vigenere import encrypt, decrypt
from generate_key import generate_key

def main():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    check_word = "AUTH_OK"
    vault_name = ".vault.txt"

    print("--- SECURE VAULT LOGIN ---")
    master = input("Enter MASTER password: ")
    my_key = generate_key(master)

    if not os.path.exists(vault_name):
        with open(vault_name, "w", encoding="utf-8") as f:
            f.write(encrypt(check_word, my_key) + "\n")
        print("[System]: New vault created successfully.")
    else:
        with open(vault_name, "r", encoding="utf-8") as f:
            first_line = f.readline().strip()

        if decrypt(first_line, my_key) != check_word:
            print("[Error]: Invalid MASTER password! Access denied.")
            return

        print("[System]: Access granted.")

    while True:
        show_menu()

        choice = input("Selection: ")

        if choice == "1":
            service_name = input("Enter service name: ")
            try:
                length = int(input("Enter password length: "))
                if length <= 0: raise ValueError
            except ValueError:
                print("[Error]: Invalid length.")
                continue

            password = "".join(random.choice(chars) for _ in range(length))
            encrypted_password = encrypt(password, my_key)

            with open(vault_name, "a", encoding="utf-8") as f:
                f.write(f"{service_name}:{encrypted_password}\n")

            print(f"\n[Success]: Saved for {service_name}: {password}")
            
        elif choice == "2":
            if not os.path.exists(vault_name):
                print("[Error]: Vault file missing.")
                continue

            print("\n--- Your credentials ---")
            with open(vault_name, "r", encoding="utf-8") as f:
                lines = f.readlines()[1:]

            if not lines:
                print("No passwords found in the vault.")
            else:
                for line in lines:
                    line = line.strip()
                    if ":" in line:
                        service, enc_pass = line.split(":", 1)
                        print(f"{service} -> {decrypt(enc_pass, my_key)}")

        elif choice == "3":
            if not os.path.exists(vault_name):
                print("[Error]: Vault file missing.")
                continue

            with open(vault_name, "r", encoding="utf-8") as f:
                all_lines = [line.strip() for line in f.readlines()]
            
            if len(all_lines) <= 1:
                print("Vault is empty (no passwords to delete)")
                continue

            header = all_lines[0]
            entries = all_lines[1:]

            print("\n-- DELETE PASSWORD ---")
            for i, line in enumerate(entries, 1):
                if ":" in line:
                    service, _ = line.split(":", 1)
                    print(f"{i}. {service}")
            
            try:
                selection = int(input("Enter number to delete (or 0 to cancel): "))
                if selection == 0:
                    continue

                if 1 <= selection <= len(entries):
                    removed_entry = entries.pop(selection - 1)
                    service_deleted = removed_entry.split(":")[0]

                    with open(vault_name, "w", encoding="utf-8") as f:
                        f.write(header + "\n")
                        for item in entries:
                            f.write(item + "\n")
                    
                    print(f"[Success]: Password for '{service_deleted}' deleted.")
                else:
                    print("[Error]: Invalid number")
            except ValueError:
                print("[Error]: Please enter a valid number.")


        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("[Error]: Invalid choice.")

if __name__ == "__main__":
    main()
