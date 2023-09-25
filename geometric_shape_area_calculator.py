#geometric_shape_area_calculator

import math # DO NOT MODIFY

def main():
    circle_pi = math.pi # DO NOT MODIFY, this line of code is assigning the variable 'circle_pi' equal to Pi ~3.14

    # TODO: In terminal, print Welcome to the geometric shape area calculator!
    print('Welcome to the geometric shape area calculator!')
    
    # User Options
    # Circle = 1
    # Rectangle = 2
    # Triangle = 3
    
    # TODO: Using one print statement, use string concatenation to print the options only 
    # as a single string (make sure to add a space between each option)
    print('Circle = 1' + ' ' + 'Rectangle = 2' + ' ' + 'Triangle = 3')

    # TODO: In terminal, ask the user "Select a shape by entering 1, 2, or 3' and assign the input to a new variable named 'choice'.
    choice = int(input('Select a shape by entering 1, 2, or 3'))

    # TODO: Convert the variable 'choice' to an integer data type.

    # TODO: With one line of code, verify the variable 'choice' is indeed the data type integer, use conditional logic and print the output.  If converted correctly, the output in Terminal should read 'True'.
    print(type(choice) == int)
  
    if choice == 1:  #DO NOT REMOVE THE 'IF'
        # Calculate the area of a circle

        # TODO: Assign a new variable named 'radius' and ask for the user's input for the radius of the circle.
        radius = input('Please enter the radius of the circle:')
        radius_1 = float(radius)
        # TODO: Convert 'radius' to float.
        # TODO: Assign a new variable named 'area' and implement the logic to calculate the area of a circle.
        area = (circle_pi) * (radius_1 ** 2)
        # HINT 1 : The formula to find area of a circle: 'circle_pi' times radius squared.  
        # Hint 2 : circle_pi is a variable that has been assigned on Line 9 and equals Pi in math.  

    elif choice == 2: # DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a rectangle
        # TODO: Assign new variables 'length' and 'width' and ask for the user's input for the length and width of the rectangle.
        length = input('Please enter the length of the rectangle:')
        width = input('Please enter the width of the rectangle:')
        # TODO: Convert both 'length' and 'width' to float.
        length_1 = float(length)
        width_1 = float(width)
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a rectangle.
        area = (length_1) * (width_1)
        # HINT: The formula to find the area of a rectangle: length times width

    elif choice == 3: #DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a triangle
        # TODO: Assign new variables 'base' and 'height' and ask for the user's input for the base length and height of the triangle.
        base = input('Please enter the base length of the triangle:')
        height = input('Please enter the height of the triangle:')
        # TODO: Convert both 'base' and 'height' to float.
        base_1 = float(base)
        height_1 = float(height)
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a triangle.
        area = (base_1/2) * (height_1)
        # HINT: The formula to find the area of a Triangle: half times base times height

    else:
        # TODO: If the user enters anything other than 1, 2 or 3, print statement "Invalid choice ."
        print('Invalid choice .')
    
    if choice in [1, 2, 3]: # DO NOT MODIFY
        print(f"The area is: {area:.2f} square units.") # DO NOT MODIFY

    # TODO: Print a statement explaining each step required to find and complete your technical assignments.  Be specific.
    print('The first step to finding the technical assignment is to log into Canvas, and access the assignments tab.\n Once there, you can scroll down to find the link to the assignment which corresponds to which day. \n You can also find the link to the assignment when selecting the modules tab - each module will have its own page, providing links to all content designated for that day. \n Once you find the assignment, you will click the link provided, which will take you to Github, and click accept assignment. \n You will need to refresh the page on Github to allow the repository to fully load. Once it is, you will see a green button that says CODE. Click the drop down arrow, and copy the repository link to your clipboard. \n You then have to clone the respository locally; create a designated directory either manually or with the mkdir command in your terminal. Use the git status command to check if its available \n When the repository is cloned, you can begin working on the .py file through VScode. Ensure you read the README file and explicitly follow all directions to complete it successfully, commenting out all function calls. \n When edits are made to the .py file, use the git add procedure; when the .py file passes the unittest, use the git commit command to commit the changes and prepare for local to remote transfer. Once these commands are used, use git push to send the .py file to the remote GitHub repository. \n A green check on the Github repository page will indicate if the assignment is successfully passed; otherwise, go back and troubleshoot and debug the code. ')


if __name__ == "__main__": # DO NOT MODIFY
    main() # DO NOT MODIFY
