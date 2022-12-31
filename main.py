first_square="U" # Does the thread across go under or over on the column of the first row

tartan_design_file = open("tartan_design.csv", 'r')
tartan_row = tartan_design_file.readline().replace('\n', '').split(',')
tartan_column = tartan_design_file.readline().replace('\n', '').split(',')

print(tartan_row, '\n', tartan_column)