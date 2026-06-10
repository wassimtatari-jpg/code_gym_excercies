def set_detector(*agres):
    for agr in (agres):
        if type(agr)==set:
            return True
    return False

print(set_detector({77,99}))

print(set_detector((99,150)))


print(set_detector("wassim"))


print(set_detector({1987}))