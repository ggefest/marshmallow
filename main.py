import os
import subprocess


def generate_ssh_key(key_path, comment="ggefest@gmail.com", key_type="ed25519", bits=None, passphrase=""):
    command = ["ssh-keygen", "-t", key_type, "-f", key_path, "-C", comment]
    if bits:
        command.extend(["-b", str(bits)])
    if passphrase:
        command.extend(["-N", passphrase])
    else:
        command.extend(["-N", ""])  # No passphrase
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("SSH key generated successfully:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error generating SSH key: {e}")
        print(e.stderr)


# Example usage:
#generate_ssh_key(os.getcwd(), comment="ggefest@gmail.com")
#generate_ssh_key(os.getcwd()+'/ssh/free-owl_key', key_type="rsa-sha2-256", bits=4096, passphrase="gfs33731")