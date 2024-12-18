import hashlib

def generate_int_from_random(random_value):

    random_bytes = str(random_value).encode('utf-8')
    hash_object = hashlib.sha256()
    hash_object.update(random_bytes)

    hash_hex =  hash_object.hexdigest()

    generate_int =  int(hash_hex,16)

    return generate_int

# print(generate_int_from_random("2341352413642634"))
# print(generate_int_from_random("35254563463456356"))
# print(generate_int_from_random("34563636536565666"))