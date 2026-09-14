def assign(list_of_items, task_to_be_added, item_type, item_type_plural):
    print(f"\nEnter {item_type_plural} assigned to the task, or press Enter to skip:")

    items_to_assign = []

    while True:

        item_to_append = input()

        if not item_to_append:
            task_to_be_added[item_type_plural] = items_to_assign
            break

        elif item_to_append.strip().lower() not in list_of_items:
            print(f"The {item_type} entered has not yet been saved in this session.")

        elif item_to_append.strip().lower() in items_to_assign:
            print(f"That {item_type} has already been assigned to this task")

        else:
            items_to_assign.append(item_to_append.strip().lower())