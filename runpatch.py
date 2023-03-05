from sngtolib import sngto
c_ds = sngto.check_prime_number
ds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print("Danh sách các số nguyên tố trong dãy số từ 1 đến 20 là:")
for i in ds:
    if c_ds(i) == 1:
        print(i, end=" ")
print("\n test_prime() passed")
# """
# Step 6: Test your library
# Now that you have built your library, you want to test it. Make sure your present working directory is /path/to/mypythonlibrary (so the root folder of your project). In your command prompt, run:
# > python -m pytest
# https://stackoverflow.com/questions/13326673/is-there-a-python-library-to-list-primes
# """
