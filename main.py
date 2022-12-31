from PIL import Image

first_square="U" # Does the thread across go under or over on the column of the first row
creation_mode="Q" # Is the tartan design file for a full 'tile' or a 'quadrant'?

tartan_design_file = open("tartan_design.csv", 'r')
tartan_column = tartan_design_file.readline().replace('\n', '').split(',')
tartan_row = tartan_design_file.readline().replace('\n', '').split(',')
tartan_design_file.close()

if creation_mode=="Q":
    tartan_column += tartan_column[::-1]
    tartan_row += tartan_row[::-1]

tartan_image = Image.new('RGB', (len(tartan_column), len(tartan_row)), (255,0,255))
tartan_image.save("tartan_image.png")