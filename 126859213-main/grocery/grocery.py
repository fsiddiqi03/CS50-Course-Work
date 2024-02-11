grocery_list = {

}

while True:
    try:
        item = input().upper().strip()
        grocery_list[item] = grocery_list.get(item, 0) + 1

    except EOFError:
            break

for item in sorted(grocery_list):
            amount = grocery_list[item]
            print(f"{amount} {item}")