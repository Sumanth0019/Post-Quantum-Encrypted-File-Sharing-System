def compare_files(file1, file2):
    print("Verifying File Integrity")

    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        original_data = f1.read()
        decrypted_data = f2.read()

    if original_data == decrypted_data:
        print("Verification Successful: The decrypted file matches the original.\n")
        return True
    else:
        print("Verification Failed: The decrypted file does not match the original.\n")
        return False
