import crypt
def test_password(hashed_password, algorithm_salt, plaintext_password):
    crypted_password = crypt.crypt(plaintext_password, algorithm_salt)
    #Compare hashed_password with the just created hash
    if hashed_password == crypted_password:
        return True
    return False


hashed_password = "$6$G.DTW7g9s5U7KYf5$QFcHx0/J88HV/Q0ab653gfYQ1KyNGx5HRhDQYyai2ZUy7Aw4tyfJ6/kI6kllfXl0DyS.LuaUJvqnlIn2fVM5F0"
algorithm_salt = "$6$G.DTW7g9s5U7KYf5$"

for password in range(100000):
    result = test_password(hashed_password, algorithm_salt, str(password) )
    if result:
        print("match found: {0}".format(password))
        break