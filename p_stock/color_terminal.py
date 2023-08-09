from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# print(Fore.GREEN + "This is green text.")
# print(Style.RESET_ALL)  # Reset all styles and colors
def red_font(text):
    return Fore.RED +text
def green_font(text):
    return Fore.GREEN +text
