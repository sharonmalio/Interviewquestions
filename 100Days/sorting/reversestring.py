def reverse(numinp):
    revstring = ""
    numinp = str(numinp)
    for num in numinp:
        revstring= num%10 +revstring
    print(int(revstring))

print(reverse("1234"))