/*This project is a simple C program that verifies whether a given Sudoku grid input follows the basic 45 Rule of Sudoku. 
The program prompts the user to input the values for the Sudoku grid, checks if the sum of the numbers in each row and column matches the expected sum (based on the number 
of rows and columns), and provides feedback on whether the input is correct or not. This project demonstrates the use of loops, arrays, and basic matrix operations in C to 
validate Sudoku inputs.
Key Features:
User input for Sudoku grid size and values.
Validation of each row and column based on Sudoku rules.
Displays whether the grid inputs are correct or not.*/


#include<stdio.h> // Required for input-output functions

int main() 
{
    // Variable declarations for row, column, and sum checks
    int i, j, n, s; // General loop and sum variables
    int k, l; // Variables for matrix size (rows and columns)
    
    int value[9][9]; // 2D array to store the Sudoku grid
    int total_row[9]; // Array to store the sum of each row
    int total_col[9]; // Array to store the sum of each column
    
    // Prompt user for inputs
    printf("'Enter the inputs of a Sudoku, and check whether it's correct or not'\n");
    printf("\nInput number of 'rows x columns': \n");

    // Get the size of the Sudoku grid from the user
    scanf("%d", &k); // Number of rows
    scanf("\n%d", &l); // Number of columns
   
    // Get values for the Sudoku grid
    printf("Enter the values for the Sudoku grid:\n");
    for(i = 0; i < k; i++)  // Loop through each row
    {
        total_row[i] = 0; // Initialize row sum to 0
        for(j = 0; j < l; j++) // Loop through each column
        {
            scanf("%d", &value[i][j]); // Get the value for the cell
           
            total_row[i] = total_row[i] + value[i][j]; // Add the cell value to the row sum
        }
    }
   
    // Calculate the sum for each column
    for(j = 0; j < l; j++) // Loop through each column
    {
        total_col[j] = 0; // Initialize column sum to 0
        for(i = 0; i < k; i++) // Loop through each row
        {
            total_col[j] = total_col[j] + value[i][j]; // Add the cell value to the column sum
        }
    }

    // Print the entered Sudoku grid
    for(i = 0; i < k; i++) // Loop through each row
    {
        printf("\n"); // Print new line for grid formatting
        for(j = 0; j < l; j++) // Loop through each column
        {
            printf("\t%d ", value[i][j]); // Print each cell value
        }
    }

    // Calculate the expected sum for each row and column using the 45 Rule
    // The sum of numbers 1 to k (if k is the size of the row/column) is given by k * (k + 1) / 2
    s = ((k * (k + 1)) / 2);

    // Validate the Sudoku grid
    for(n = 0; n < k; n++) 
    {
        // Check if the sum of the nth column matches the expected sum
        if((total_col[n]) != s) 
        {
            printf("\nIncorrect input in column %d", n + 1); // Print error for column
        }
        // Check if the sum of the nth row matches the expected sum
        else if((total_row[n]) != s)
        {
            printf("Incorrect input in row %d", n + 1); // Print error for row
        }
        // If both row and column sums are correct, print success message
        else if(total_row[n] == s && total_col[n] == s)
        {
            printf("\nCorrect input for both row and column %d", n + 1);
        }
        // If only the row sum is correct, print success message for row
        else if(total_row[n] == s)
        {
            printf("\nCorrect input for row %d", n + 1);
        }
        // If only the column sum is correct, print success message for column
        else if(total_col[n] == s)
        {
            printf("\nCorrect input for column %d", n + 1);
        }
    }

    return 0;
}
