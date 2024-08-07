# Schedule-Matcher

A program that takes 2 ordered schedules (sequences) and finds the longest sub-schedule where both parties can enjoy some common activities without betraying their ordering. Surprisingly useful for planning movie marathons, among other hobbies.

# Applications
1. You want to watch all the Star Wars movies in release order, but your friend wants to watch them in chronological order. You two would still like to watch
   as many of them as possible together, without betraying your respective orders.
   ![EX_movies](https://github.com/user-attachments/assets/4f8b3da9-f945-4cb4-b114-14430c53b943)

2. You and your friend are tagging alongside separate groups at a carnival. Each group has their own schedule of carnival rides that they'd like to get through. 
   However, you and your friend would like to enjoy some rides together without leaving your respective groups. The program returns the maximum number of rides
   you two can ride together without forcing your groups to change the order of their schedule.
   ![EX_carnival](https://github.com/user-attachments/assets/43ed465c-2cdd-40d1-a1e2-d50ecf40a8aa)

3.  Miscellaneous examples:
    ![EX_darksouls1](https://github.com/user-attachments/assets/ab85b547-881e-4b35-9231-8b0c3727209d)

    ![EX_symbols](https://github.com/user-attachments/assets/19c64f0b-a28f-41ee-b421-94c4c180edd4)

   ![EX_gym](https://github.com/user-attachments/assets/d4642ed0-9850-46e6-81e3-2bd379986cc5)



# How to Use (Simple Option):

* Download `Schedule Matcher.exe` from [releases page](https://github.com/rockygao2020/Schedule-Matcher/releases) and run.
* Python and dependencies not required.
* Slower than 2nd option.


# How to Use (Python Script Option):

* Requires Python and Pip. You can check if you have Python and Pip(usually comes with Python's installation) installed by typing the following into the command prompt and waiting for their version descriptions:
```
python
pip --version
```
* Download `main.py` and `schedule_matcher.py` and put them in the same directory.
* Download PyQt6 using Pip:
```
pip install PyQt6
```
* Run `main.py` using your environment, or open the command prompt in the directory that holds the `.py` files, and type the following:
```
python main.py
```
# What I Utilized/Learned/Analysis:
* Tabulation/Dynamic Programming Algorithm to solve the Longest Common Sequence(LCS) problem.
   * Runtime: O(n*m), where n is the length of the first sequence, and m the length of the second.  
* Python Modular Programming/Inheritance/Object-Oriented-Programming
* PyQt6 frontend basics.
* Pyinstaller app execution basics.

# Resources Used:
* PyQt6 (Frontend)
   * The following 2 PyQt functions `deleteItemsOfLayout` and `Window.boxDelete` in `main.py` are taken from The Trowser and Brendan          Abel [here](https://stackoverflow.com/questions/37564728/pyqt-how-to-remove-a-layout-from-a-layout). These 2 functions 
      helped me trememdously when it came to swapping layouts for the GUI
* Pyinstaller (Frontend/Making the  `.exe` file)
