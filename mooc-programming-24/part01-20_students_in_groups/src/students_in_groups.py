# Write your solution here
students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))

num_of_groups = students // group_size;
extra = students % group_size

if extra > 0:
    num_of_groups += 1

print(f"Number of groups formed: {num_of_groups}")