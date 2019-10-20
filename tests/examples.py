protocol = {
    # Sent from SP LINK to check there's a SP PRO at the other end
    'hello': {
        'sent': b'\x51\x00\x00\xa0\x00\x00\x9d\x4b',
        'read': b'\x51\x00\x00\xa0\x00\x00\x9d\x4b\x01\x00\xd8\x19',
    },
    # To calulate the hash for auth, we first request some data from the SP PRO
    # that I'm calling "init", which is hashed with the password for the actual
    # login.
    # The examples use the default password of "Selectronic SP PRO"
    'auth_init_0': {
        'sent': b'Q\x07\x00\x00\x1f\x00\xcfb',
        'read': b"Q\x07\x00\x00\x1f\x00\xcfbz\xb2\x9f\xdeh\x1a\xe0\xb1\'\'\x08\x8f\x80\xc4\xba\x8b\xa0@",
    },
    'auth_login_0': {
        'sent': b'W\x07\x00\x00\x1f\x005z\xb6\xd16\x04\x08\x0c\x87\xce\x81\xc1\x82\xc6o\xa5\xfb5w\xaa',
        'read': b'W\x07\x00\x00\x1f\x005z\xb6\xd16\x04\x08\x0c\x87\xce\x81\xc1\x82\xc6o\xa5\xfb5w\xaa',
    },
    'auth_init_1': {
        'sent': b'Q\x07\x00\x00\x1f\x00\xcfb',
        'read': b"Q\x07\x00\x00\x1f\x00\xcfb\xeb\xc5\x16o\x9a\xf4p\x83\xdcR\xd2W\'\x12\xbb>r\xbd",
    },
    'auth_login_1': {
        'sent': b"W\x07\x00\x00\x1f\x005z\xdf\'\x9d\\\x01\xfa=\xb9\xa3\xc8Rw\x1a\xbd\x05\xf86=",
        'read': b"W\x07\x00\x00\x1f\x005z\xdf\'\x9d\\\x01\xfa=\xb9\xa3\xc8Rw\x1a\xbd\x05\xf86=",
    },
}
