# Post-Quantum-Encrypted-File-Sharing-System
A quantum-resistant file encryption system combining Kyber-512 for secure key exchange and AES-256 for fast file encryption. Designed to ensure long-term data security against quantum attacks using Ring-LWE–based cryptography.


A secure and quantum-resistant file encryption tool combining **Kyber-512** (based on Ring-LWE) for post-quantum key exchange and **AES-256 (CBC mode)** for efficient symmetric encryption. This project demonstrates a practical implementation of cryptography that remains secure even in the presence of quantum computing capabilities.

---

## Introduction

With the rise of quantum computing, classical cryptographic schemes like RSA and ECC are becoming vulnerable to quantum attacks (e.g., Shor’s algorithm). This project implements a **post-quantum file encryption system** to future-proof data security. It leverages **Kyber-512**, a NIST-selected lattice-based cryptographic scheme, in conjunction with AES-256 for fast and reliable file encryption.

---

## Objective

The primary goal is to develop a robust, post-quantum secure file sharing system that:

- Utilizes **Kyber-512** (Ring-LWE) for key encapsulation and exchange.
- Applies **AES-256 (CBC mode)** for encrypting file contents.
- Ensures **data confidentiality** and **integrity verification**.
- Serves as a learning-friendly, transparent implementation of post-quantum encryption.

This solution is extendable to secure cloud storage systems, encrypted messaging platforms, and quantum-safe communication protocols.

---

## Features

- **Quantum-Safe Key Generation** using Kyber-512 (Ring-LWE).
- **Key Encapsulation Mechanism (KEM)** for secure key exchange.
- **Symmetric File Encryption** with AES-256 in CBC mode.
- **End-to-End Workflow**: Key generation → encryption → decryption → integrity verification.
- **Intermediate Output Display** for transparency and educational purposes.

---

## Cryptographic Details

| Component            | Description                                         |
|----------------------|-----------------------------------------------------|
| Post-Quantum Scheme  | Kyber-512 (Ring-LWE)                                |
| Symmetric Algorithm  | AES-256 (CBC mode)                                  |
| Key Derivation       | First 32 bytes of shared Kyber secret               |
| IV Handling          | Initialization vector stored in encrypted file     |
| Integrity Check      | Byte-wise comparison of original and decrypted files|

---

##  Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/post-quantum-encrypted-file-sharing.git
cd post-quantum-encrypted-file-sharing
```

### 2. Install Dependencies
```bash
pip install pycryptodome>=3.19.0 kyber_py>=1.0.1
```

## Usage
Run the main script and follow the prompts:
```bash
python main.py
```

You will be asked to provide a file path. The system will:
  - Generate Kyber key pair (public/private)
  - Perform secure key exchange (KEM)
  - Derive a shared AES key from the Kyber secret
  - Encrypt the file using AES-256
  - Decrypt the file
  - Validate that decrypted file matches the original


## Background Concepts

### Post-Quantum Cryptography (PQC)
PQC is a branch of cryptography that designs algorithms resilient to quantum attacks. Unlike RSA or ECC, PQC schemes remain secure against quantum algorithms such as Shor's or Grover’s.

### Lattice-Based Cryptography
Lattice-based schemes (such as Kyber) rely on the hardness of lattice problems:

Learning With Errors (LWE): Involves solving systems of linear equations with added noise.

Ring-LWE: A computationally efficient variant of LWE operating in structured algebraic rings.

### Kyber (Used in this Project)
Kyber is a NIST-selected key encapsulation mechanism based on Ring-LWE. It provides strong post-quantum security with efficient performance suitable for real-world applications.


## Future Enhancements
  - Digital Signature Integration for file authenticity verification.
  - Multi-User Key Exchange Protocols for group-based secure sharing.
  - Performance Optimizations for large file encryption and streaming.
  - Web/GUI Interface for non-technical end users.

## Requirements
```bash
Python ≥ 3.7

pycryptodome ≥ 3.19.0

kyber_py ≥ 1.0.1
```


## Example Workflow

```bash
$ python main.py
Enter the file path to encrypt & decrypt: sample.txt

Generating Kyber-512 Key Pair...
Encapsulating shared secret...
Encrypting file using AES-256...
Decrypting file...
Verification Successful: The decrypted file matches the original.
```
