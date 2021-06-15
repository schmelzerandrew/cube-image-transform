# cube-image-transform
A python script that changes the colors of an image based on the RGB cube.

Primary usage is through the Python interactive intepreter, calling the various functions:

main() asks for a filename input through the interactive interpreter, as well as a numbered permutation to apply to the specified image.

permutefile() does the same, but applies all 48 unit symmetries to the image, creating a new folder at the destination.

topSix() applies only 6 permutations: the permutations with all positive entries. No colors are inverted, only shifted.
