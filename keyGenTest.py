import bitcoin

#Generate a random private key
valid_private_key = False
while not valid_private_key:
    private_key = bitcoin.random_key()
    decoded_private_key = bitcoin.decode_privkey(private_key, 'hex')
    valid_private_key = 0 < decoded_private_key < bitcoin.N

print "Private Key (hex) is:                    ", private_key
print "Private Key (decimal) is:                ", decoded_private_key

print ""

#Convert private key to WIF format
wif_encoded_private_key = bitcoin.encode_privkey(decoded_private_key, 'wif')
print "Private Key (WIF) is:                    " , wif_encoded_private_key

print ""

#Add suffix "01" to indicate a compressed private key
compressed_private_key = private_key + '01'
print "Private Key Compressed (hex) is:         ", compressed_private_key

# Generate a WIF format from the compressed private key
wif_compressed_private_key = bitcoin.encode_privkey(
    bitcoin.decode_privkey(compressed_private_key, 'hex'), 'wif')
print "Private Key (WIF-Compressed) is:         ", wif_compressed_private_key

# Multiply the EC Generator Point G with the private key to get a public key Point
public_key = bitcoin.fast_multiply(bitcoin.G, decoded_private_key)
print "Public Key (x,y) coordinates is:         ", public_key

print ""

# Encode as hex, prefix 04
hex_encoded_public_key = bitcoin.encode_pubkey(public_key, 'hex')
print "Public Key (hex) is:                     ", hex_encoded_public_key

# Compress Public Key, adjust prefix depending on whether y is even or odd
(public_key_x, public_key_y) = public_key
if (public_key_y % 2) == 0:
    compressed_prefix = '02'
else:
    compressed_prefix = '03'
hex_compressed_public_key = compressed_prefix + bitcoin.encode(public_key_x, 16)
print "Compressed Public Key (hex) is:          ", hex_compressed_public_key

#Generate Bitcoin Address from Public Key
print "Bitcoin Address (b58check) is:           ", bitcoin.pubkey_to_address(public_key)

# Generate compressed Bitcoin Address from compressed public key
print "Compressed Bitcoin Address (B58check) is:", \
    bitcoin.pubkey_to_address(hex_compressed_public_key)
