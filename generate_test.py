import numpy as np

NUM_EL = 100

with open("small_test.txt", "w+") as file:
    file.writelines([f"\t\ttree.insert({num});\n" for num in np.arange(NUM_EL)[np.random.permutation(NUM_EL)]] + ['\t\tSystem.out.println("VALID TREE: " + tree.checkValidRBT());'])