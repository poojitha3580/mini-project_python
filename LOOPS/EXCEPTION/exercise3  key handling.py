try:
    d={"name":"olive"}
    print(d["name"])
except keyError:
    print("Error:KeyError")