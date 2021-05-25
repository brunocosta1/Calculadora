import entry_values
import solver
import menu
from entry_values import grid
def main():

     opc = menu.menu()
     entry_values.InputValues(opc)
     solver.solve(grid)
main()
