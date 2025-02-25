def main():
    print_column(2)
    
def print_column(height):
    for _ in range(3):
        print("#\n" * height, end="")
        
main()