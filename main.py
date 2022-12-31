from PIL import Image

first_square="U" # Does the thread across go under or over on the column of the first row

tartan_design_file = open("tartan_design.csv", 'r')
tartan_column = tartan_design_file.readline().replace('\n', '').split(',')
tartan_row = tartan_design_file.readline().replace('\n', '').split(',')
tartan_design_file.close()

tartan_image = Image.new('RGB', (len(tartan_column), len(tartan_row)), (255,0,255))
tartan_image.save("tartan_image.png")