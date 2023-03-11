from sngtolib import sngto
cds = sngto.check_prime_number
ds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
dem = 0
for k in ds:
    if cds(k) == 1:
        dem += 1
        print(k)
print("So luong so nguyen to trong day la:", dem)
# """
# Step 6: Test your library
# Now that you have built your library, you want to test it. Make sure your present working directory is /path/to/mypythonlibrary (so the root folder of your project). In your command prompt, run:
# > python -m pytest
# https://stackoverflow.com/questions/13326673/is-there-a-python-library-to-list-primes
# """
"""n = int(input(">> nhap mot so n: "))
for i in range(n):
    check = check_prime_number(i)
    if( check == 1 ) :
        print(i)
ds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for k in ds:
    if check_prime_number(k) == 1:
        dem += 1
print("So luong so nguyen to trong day la:", dem)"""
