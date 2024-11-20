import sys
from PIL import Image,ImageOps


def wear(input , output ):
    try:
        back_img = Image.open(input)
        shirt = Image.open("shirt.png")

        back_img= ImageOps.fit(back_img,shirt.size )
        back_img.paste(shirt,mask=shirt)

        back_img.save(output)
    except (IOError,FileNotFoundError) :
        sys.exit("Input does not exist")



def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    ext = ["jpg", "jpeg","png"]

    input  = sys.argv[1].split(".")
    output  = sys.argv[2].split(".")

    if  input[-1].lower() != output[-1].lower():
        sys.exit("Input and output have different extensions")
    elif (input[-1].lower() or output[-1].lower()) not in ext:
        sys.exit("Invalid output")

    #Call the after function with the input and output filenames
    wear( sys.argv[1],  sys.argv[2] )

if __name__ == "__main__":
    main()
